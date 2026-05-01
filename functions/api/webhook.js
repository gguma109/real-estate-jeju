export async function onRequestGet(context) {
    const { searchParams } = new URL(context.request.url);
    const mode = searchParams.get('hub.mode');
    const token = searchParams.get('hub.verify_token');
    const challenge = searchParams.get('hub.challenge');

    const VERIFY_TOKEN = context.env.VERIFY_TOKEN;

    if (mode && token) {
        if (mode === 'subscribe' && token === VERIFY_TOKEN) {
            console.log('WEBHOOK_VERIFIED');
            return new Response(challenge, { status: 200 });
        } else {
            return new Response('Forbidden', { status: 403 });
        }
    }
    return new Response('Invalid Request', { status: 400 });
}

export async function onRequestPost(context) {
    const body = await context.request.json();
    const PAGE_ACCESS_TOKEN = context.env.PAGE_ACCESS_TOKEN;

    if (body.object === 'instagram' || body.object === 'page') {
        for (const entry of body.entry) {
            if (entry.changes) {
                for (const change of entry.changes) {
                    if (change.field === 'comments') {
                        const commentId = change.value.id;
                        const messageText = change.value.text;
                        const fromId = change.value.from.id;

                        console.log(`New comment: "${messageText}" from ${fromId}`);

                        // Send DM (Private Reply)
                        await sendPrivateReply(commentId, "안녕하세요! 부동산 통합 관리 앱입니다. 문의하신 내용에 대해 곧 답변 드리겠습니다!", PAGE_ACCESS_TOKEN);
                    }
                }
            }
        }
        return new Response('EVENT_RECEIVED', { status: 200 });
    } else {
        return new Response('Not Found', { status: 404 });
    }
}

async function sendPrivateReply(commentId, message, accessToken) {
    const url = `https://graph.facebook.com/v19.0/${commentId}/private_replies`;
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: message,
            access_token: accessToken
        })
    });

    const result = await response.json();
    if (!response.ok) {
        console.error('Error sending DM:', result);
    } else {
        console.log(`Successfully sent DM to comment ${commentId}`);
    }
}
