import sys

path = r'C:\Users\xyz30\.gemini\antigravity\scratch\real_estate_lite\public\index.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find the corruption start (line 2117 in 1-indexed is index 2116)
# But let's find it by content to be sure.
start_index = -1
for i, line in enumerate(lines):
    if 'alue="${data.maintenance' in line and i > 2000:
        start_index = i
        break

end_index = -1
for i in range(len(lines)-1, 0, -1):
    if 'return \'<p class="text-center py-10 text-gray-400">지원되지 않는 카테고리입니다.</p>\';' in lines[i]:
        end_index = i + 1
        break

if start_index != -1 and end_index != -1:
    # Remove everything from line 2115 (index 2114) to end_index
    # We want to keep up to line 2114 (which is "`;") and the next "}" (closing the if)
    # Wait, line 2114 is index 2113.
    # Lines:
    # 2113:                     </div>
    # 2114:                 `;
    # 2115:             }
    
    # We want to replace from index 2115 (line 2116) to end_index
    
    new_content = """            } else if (category === '상가') {
                return `
                    <div class="space-y-4">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매물 번호</label>
                                <input type="text" id="ad-field-ad_no" value="${data.ad_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">상호명</label>
                                <input type="text" id="ad-field-biz_name" value="${data.biz_name || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <label class="text-xs font-bold text-gray-500">소재지</label>
                                <div class="flex gap-1">
                                    <button onclick="openNaverMap()" class="text-[10px] bg-[#03C75A] text-white px-2 py-0.5 rounded font-bold shadow-sm">네이버</button>
                                    <button onclick="openKakaoMap()" class="text-[10px] bg-[#FEE500] text-[#191919] px-2 py-0.5 rounded font-bold shadow-sm">카카오</button>
                                </div>
                            </div>
                            <input type="text" id="ad-field-address" value="${data.address || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">유형</label>
                                <select id="ad-field-usage_type" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 bg-white">
                                    <option value="월세" ${data.usage_type === '월세' ? 'selected' : ''}>월세</option>
                                    <option value="년세" ${data.usage_type === '년세' ? 'selected' : ''}>년세</option>
                                    <option value="전세" ${data.usage_type === '전세' ? 'selected' : ''}>전세</option>
                                    <option value="매매" ${data.usage_type === '매매' ? 'selected' : ''}>매매</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">평수</label>
                                <input type="text" id="ad-field-area" value="${data.area || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">보증금</label>
                                <input type="text" id="ad-field-deposit" value="${data.deposit || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">년/월세</label>
                                <input type="text" id="ad-field-rent" value="${data.rent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매매가</label>
                                <input type="text" id="ad-field-sale_price" value="${data.sale_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">권리금</label>
                                <input type="text" id="ad-field-premium" value="${data.premium || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">구조</label>
                                <input type="text" id="ad-field-structure" value="${data.structure || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">담당자</label>
                                <input type="text" id="ad-field-agent" value="${data.agent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">용도</label>
                            <input type="text" id="ad-field-purpose" value="${data.purpose || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">특이사항</label>
                            <textarea id="ad-field-notes" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 resize-none h-24">${data.notes || ''}</textarea>
                        </div>
                    </div>
                `;
            } else if (category === '주택&건물 통매매') {
                return `
                    <div class="space-y-4">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매물 번호</label>
                                <input type="text" id="ad-field-ad_no" value="${data.ad_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">상호명</label>
                                <input type="text" id="ad-field-biz_name" value="${data.biz_name || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">종류</label>
                                <input type="text" id="ad-field-type" value="${data.type || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500" placeholder="예: 단독주택, 빌딩">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">유형</label>
                                <select id="ad-field-usage_type" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 bg-white">
                                    <option value="월세" ${data.usage_type === '월세' ? 'selected' : ''}>월세</option>
                                    <option value="년세" ${data.usage_type === '년세' ? 'selected' : ''}>년세</option>
                                    <option value="전세" ${data.usage_type === '전세' ? 'selected' : ''}>전세</option>
                                    <option value="매매" ${data.usage_type === '매매' ? 'selected' : ''}>매매</option>
                                </select>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <label class="text-xs font-bold text-gray-500">소재지</label>
                                <div class="flex gap-1">
                                    <button onclick="openNaverMap()" class="text-[10px] bg-[#03C75A] text-white px-2 py-0.5 rounded font-bold shadow-sm">네이버</button>
                                    <button onclick="openKakaoMap()" class="text-[10px] bg-[#FEE500] text-[#191919] px-2 py-0.5 rounded font-bold shadow-sm">카카오</button>
                                </div>
                            </div>
                            <input type="text" id="ad-field-address" value="${data.address || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">동호수</label>
                                <input type="text" id="ad-field-room_no" value="${data.room_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">가구수</label>
                                <input type="text" id="ad-field-household_count" value="${data.household_count || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">대지면적</label>
                                <input type="text" id="ad-field-land_area" value="${data.land_area || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">연면적</label>
                                <input type="text" id="ad-field-total_floor_area" value="${data.total_floor_area || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매매가</label>
                                <input type="text" id="ad-field-sale_price" value="${data.sale_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">보증금</label>
                                <input type="text" id="ad-field-deposit" value="${data.deposit || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">년/월세</label>
                                <input type="text" id="ad-field-rent" value="${data.rent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">관리비</label>
                                <input type="text" id="ad-field-maintenance" value="${data.maintenance || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">현관 비번</label>
                                <input type="text" id="ad-field-common_pwd" value="${data.common_pwd || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">담당자</label>
                                <input type="text" id="ad-field-agent" value="${data.agent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">특이사항</label>
                            <textarea id="ad-field-notes" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 resize-none h-24">${data.notes || ''}</textarea>
                        </div>
                    </div>
                `;
            } else if (category === '토지') {
                return `
                    <div class="space-y-4">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매물 번호</label>
                                <input type="text" id="ad-field-ad_no" value="${data.ad_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">소유주</label>
                                <input type="text" id="ad-field-owner" value="${data.owner || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">유형</label>
                                <select id="ad-field-usage_type" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 bg-white">
                                    <option value="월세" ${data.usage_type === '월세' ? 'selected' : ''}>월세</option>
                                    <option value="년세" ${data.usage_type === '년세' ? 'selected' : ''}>년세</option>
                                    <option value="전세" ${data.usage_type === '전세' ? 'selected' : ''}>전세</option>
                                    <option value="매매" ${data.usage_type === '매매' ? 'selected' : ''}>매매</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">평수</label>
                                <input type="text" id="ad-field-area" value="${data.area || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <label class="text-xs font-bold text-gray-500">소재지</label>
                                <div class="flex gap-1">
                                    <button onclick="openNaverMap()" class="text-[10px] bg-[#03C75A] text-white px-2 py-0.5 rounded font-bold shadow-sm">네이버</button>
                                    <button onclick="openKakaoMap()" class="text-[10px] bg-[#FEE500] text-[#191919] px-2 py-0.5 rounded font-bold shadow-sm">카카오</button>
                                </div>
                            </div>
                            <input type="text" id="ad-field-address" value="${data.address || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매매가</label>
                                <input type="text" id="ad-field-sale_price" value="${data.sale_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">광고금액</label>
                                <input type="text" id="ad-field-ad_price" value="${data.ad_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">평단가</label>
                                <input type="text" id="ad-field-unit_price" value="${data.unit_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">보증금</label>
                                <input type="text" id="ad-field-deposit" value="${data.deposit || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">임대료</label>
                                <input type="text" id="ad-field-rent" value="${data.rent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">지목</label>
                                <input type="text" id="ad-field-land_type" value="${data.land_type || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">용도지역</label>
                                <input type="text" id="ad-field-zoning" value="${data.zoning || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">담당자</label>
                                <input type="text" id="ad-field-agent" value="${data.agent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">특이사항</label>
                            <textarea id="ad-field-notes" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 resize-none h-24">${data.notes || ''}</textarea>
                        </div>
                    </div>
                `;
            } else {
                // 기타 카테고리
                return `
                    <div class="space-y-4">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매물 번호</label>
                                <input type="text" id="ad-field-ad_no" value="${data.ad_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">상호명</label>
                                <input type="text" id="ad-field-biz_name" value="${data.biz_name || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">종류</label>
                                <input type="text" id="ad-field-type" value="${data.type || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">유형</label>
                                <select id="ad-field-usage_type" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 bg-white">
                                    <option value="월세" ${data.usage_type === '월세' ? 'selected' : ''}>월세</option>
                                    <option value="년세" ${data.usage_type === '년세' ? 'selected' : ''}>년세</option>
                                    <option value="전세" ${data.usage_type === '전세' ? 'selected' : ''}>전세</option>
                                    <option value="매매" ${data.usage_type === '매매' ? 'selected' : ''}>매매</option>
                                </select>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <label class="text-xs font-bold text-gray-500">소재지</label>
                                <div class="flex gap-1">
                                    <button onclick="openNaverMap()" class="text-[10px] bg-[#03C75A] text-white px-2 py-0.5 rounded font-bold shadow-sm">네이버</button>
                                    <button onclick="openKakaoMap()" class="text-[10px] bg-[#FEE500] text-[#191919] px-2 py-0.5 rounded font-bold shadow-sm">카카오</button>
                                </div>
                            </div>
                            <input type="text" id="ad-field-address" value="${data.address || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">동호수</label>
                                <input type="text" id="ad-field-room_no" value="${data.room_no || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">평수</label>
                                <input type="text" id="ad-field-area" value="${data.area || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">입금가</label>
                                <input type="text" id="ad-field-cost_price" value="${data.cost_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">매매가</label>
                                <input type="text" id="ad-field-sale_price" value="${data.sale_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">전세</label>
                                <input type="text" id="ad-field-jeonse_price" value="${data.jeonse_price || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">보증금</label>
                                <input type="text" id="ad-field-deposit" value="${data.deposit || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">년/월세</label>
                                <input type="text" id="ad-field-rent" value="${data.rent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">관리비</label>
                                <input type="text" id="ad-field-maintenance" value="${data.maintenance || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">권리금</label>
                                <input type="text" id="ad-field-premium" value="${data.premium || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 mb-1">담당자</label>
                                <input type="text" id="ad-field-agent" value="${data.agent || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                            </div>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">구조</label>
                            <input type="text" id="ad-field-structure" value="${data.structure || ''}" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-gray-500 mb-1">특이사항</label>
                            <textarea id="ad-field-notes" class="w-full border border-gray-200 rounded-lg px-3 py-2 outline-none focus:border-orange-500 resize-none h-24">${data.notes || ''}</textarea>
                        </div>
                    </div>
                `;
            }
            return '<p class="text-center py-10 text-gray-400">지원되지 않는 카테고리입니다.</p>';
        }
"""
    
    # We replace from lines[2115] to lines[end_index-1]
    # Wait, lines[2115] is line 2116.
    
    final_lines = lines[:2115] + [new_content] + lines[end_index:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("SUCCESS")
else:
    print(f"FAILED: start={start_index}, end={end_index}")
