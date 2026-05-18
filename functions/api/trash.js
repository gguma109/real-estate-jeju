export async function onRequestGet(context) {
    const { request, env } = context;
    const authHeader = request.headers.get('Authorization') || '';
    const token = authHeader.replace(/bearer /i, '').trim();

    if (!token) {
        return new Response(JSON.stringify({ error: "Unauthorized" }), { status: 401 });
    }

    try {
        // Fetch trashed items from all tables
        const rentals = await env.DB.prepare("SELECT id, 'rental' as type, type as title_hint, date as info, deleted_at FROM rentals WHERE user_id = ? AND is_deleted = 1").bind(token).all();
        const notes = await env.DB.prepare("SELECT id, 'note' as type, title as title_hint, content as info, deleted_at FROM notes WHERE user_id = ? AND is_deleted = 1").bind(token).all();
        const ads = await env.DB.prepare("SELECT id, 'ad' as type, category as title_hint, data as info, deleted_at FROM ads WHERE user_id = ? AND is_deleted = 1").bind(token).all();

        const allTrash = [
            ...(rentals.results || []),
            ...(notes.results || []),
            ...(ads.results || [])
        ];

        // Sort by deleted_at descending
        allTrash.sort((a, b) => {
            const dateA = new Date(a.deleted_at || 0);
            const dateB = new Date(b.deleted_at || 0);
            return dateB - dateA;
        });

        return new Response(JSON.stringify(allTrash), {
            headers: { 'Content-Type': 'application/json' }
        });
    } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), { status: 500 });
    }
}

export async function onRequestPut(context) {
    // Restore item
    const { request, env } = context;
    const authHeader = request.headers.get('Authorization') || '';
    const token = authHeader.replace(/bearer /i, '').trim();

    if (!token) {
        return new Response(JSON.stringify({ error: "Unauthorized" }), { status: 401 });
    }

    try {
        const body = await request.json();
        const { id, type } = body;

        if (!id || !type) {
            return new Response(JSON.stringify({ error: "Missing ID or type" }), { status: 400 });
        }

        let tableName = '';
        if (type === 'rental') tableName = 'rentals';
        else if (type === 'note') tableName = 'notes';
        else if (type === 'ad') tableName = 'ads';
        else return new Response(JSON.stringify({ error: "Invalid type" }), { status: 400 });

        const query = `UPDATE ${tableName} SET is_deleted = 0, deleted_at = NULL WHERE id = ? AND user_id = ?`;
        const result = await env.DB.prepare(query).bind(id, token).run();

        if (result.meta.changes === 0) {
            return new Response(JSON.stringify({ error: "Not found or unauthorized" }), { status: 404 });
        }

        return new Response(JSON.stringify({ success: true }));
    } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), { status: 500 });
    }
}

export async function onRequestDelete(context) {
    // Permanently delete
    const { request, env } = context;
    const authHeader = request.headers.get('Authorization') || '';
    const token = authHeader.replace(/bearer /i, '').trim();

    if (!token) {
        return new Response(JSON.stringify({ error: "Unauthorized" }), { status: 401 });
    }

    try {
        const url = new URL(request.url);
        const id = url.searchParams.get('id');
        const type = url.searchParams.get('type');

        if (id && type) {
            let tableName = '';
            if (type === 'rental') tableName = 'rentals';
            else if (type === 'note') tableName = 'notes';
            else if (type === 'ad') tableName = 'ads';
            else return new Response(JSON.stringify({ error: "Invalid type" }), { status: 400 });

            const result = await env.DB.prepare(
                `DELETE FROM ${tableName} WHERE id = ? AND user_id = ? AND is_deleted = 1`
            ).bind(id, token).run();

            if (result.meta.changes === 0) {
                return new Response(JSON.stringify({ error: "Not found or unauthorized" }), { status: 404 });
            }
        } else {
            // Empty trash
            await env.DB.prepare("DELETE FROM rentals WHERE user_id = ? AND is_deleted = 1").bind(token).run();
            await env.DB.prepare("DELETE FROM notes WHERE user_id = ? AND is_deleted = 1").bind(token).run();
            await env.DB.prepare("DELETE FROM ads WHERE user_id = ? AND is_deleted = 1").bind(token).run();
        }

        return new Response(JSON.stringify({ success: true }));
    } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), { status: 500 });
    }
}
