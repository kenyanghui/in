# coding: utf-8
import re

with open("D:/Git/website/in/悦洋教育_竞赛产品矩阵分析_v3_10赛事.html", "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# ===== 1. Replace table rows 8-10 =====
old_start = '<td><b>CTB 全球青年研究创新论坛</b>'
old_end_10 = '<td>夏季</td>\n      </tr>'

idx_start = content.find(old_start)
if idx_start == -1:
    print("ERROR: table row 8 not found")
else:
    # Find the start of row 8 (<tr> before our match)
    tr8_start = content.rfind('<tr>', idx_start - 50, idx_start)
    # Find the end of row 10
    idx_end = content.find(old_end_10, idx_start)
    if idx_end != -1:
        idx_end += len(old_end_10)
        tr10_end = content.find('</tr>', idx_end) + len('</tr>')
        print(f"Found table rows 8-10: {tr8_start}-{tr10_end}")

        new_rows = '''      <tr>
        <td>8</td>
        <td><b>腾讯青少年人工智能大赛</b></td>
        <td><span class="tag tag-blue">企业</span></td>
        <td>8-18岁</td>
        <td class="score score-4">★★★★</td>
        <td>AI应用创新</td>
        <td>秋季</td>
      </tr>
      <tr>
        <td>9</td>
        <td><b>百度AI创意挑战赛</b></td>
        <td><span class="tag tag-blue">企业</span></td>
        <td>10-18岁</td>
        <td class="score score-4">★★★★</td>
        <td>AI创意/应用</td>
        <td>秋季</td>
      </tr>
      <tr>
        <td>10</td>
        <td><b>华为云青少年AI大赛</b></td>
        <td><span class="tag tag-blue">企业</span></td>
        <td>10-18岁</td>
        <td class="score score-3">★★★</td>
        <td>AI开发/创新</td>
        <td>夏季</td>
      </tr>'''

        content = content[:tr8_start] + new_rows + content[tr10_end:]
        changes += 1
        print("Table rows 8-10 replaced")

# ===== 2. Replace analysis cards 8-10 =====
# Find each card by its comment marker and replace the entire comp-card block
card_markers = [
    ("<!-- 8. CTB -->", "<!-- 9. ICW -->"),
    ("<!-- 9. ICW -->", "<!-- 10. 全球AI峰会 -->"),
    ("<!-- 10. 全球AI峰会 -->", "</section>"),
]

new_cards = [
    # Card 8 - 腾讯
    '''  <!-- 8. 腾讯 -->
  <div class="comp-card">
    <div class="comp-header">
      <div class="comp-name">8&#65039;&#8419; 腾讯青少年人工智能大赛</div>
      <div class="comp-badges">
        <span class="tag tag-blue">企业</span>
        <span class="tag tag-yellow" style="background:#fefcbf;">★★★★ 适合</span>
      </div>
    </div>
    <div class="comp-meta">
      <span><strong>主办</strong>：腾讯科技</span>
      <span><strong>年龄</strong>：8-18岁（小学/初中/高中）</span>
      <span><strong>费用</strong>：¥0</span>
    </div>
    <p style="font-size:14px;">由腾讯主办，面向全国青少年的AI创新大赛，涵盖AI编程、AI应用开发、AI创意方案等赛项。评审注重AI技术的创新应用与社会价值。腾讯云AI平台提供技术支持，获奖者可获得腾讯官方证书及参访机会。</p>
    <div class="comp-match" style="background:#f0fff4;border:1px solid #c6f6d5;">
      ✅ <b>悦洋匹配</b>：腾讯AI大赛的AI应用赛项与悦洋的AI商科课程高度匹配。一日创造营AI项目可直接投递。大厂背书对家长有吸引力。<br>
      📦 产品：一日营/3天备赛营 → 腾讯AI赛专项（&#165;3,980-&#165;5,980）
    </div>
  </div>''',
    # Card 9 - 百度
    '''  <!-- 9. 百度 -->
  <div class="comp-card">
    <div class="comp-header">
      <div class="comp-name">9&#65039;&#8419; 百度AI创意挑战赛</div>
      <div class="comp-badges">
        <span class="tag tag-blue">企业</span>
        <span class="tag tag-yellow" style="background:#fefcbf;">★★★★ 适合</span>
      </div>
    </div>
    <div class="comp-meta">
      <span><strong>主办</strong>：百度科技</span>
      <span><strong>年龄</strong>：10-18岁</span>
      <span><strong>费用</strong>：¥0</span>
    </div>
    <p style="font-size:14px;">百度主办，以AI改变生活为核心主题的青少年创意竞赛。参赛者需使用百度AI开放平台工具完成创新项目，含AI创意方案、AI应用开发等方向。评审聚焦创意性、技术实现和社会影响力。</p>
    <div class="comp-match" style="background:#f0fff4;border:1px solid #c6f6d5;">
      ✅ <b>悦洋匹配</b>：百度AI平台工具易用，学员可快速上手。AI商科项目可无缝接入。适合作为ICC/NOC学员的补充赛事，增加获奖机会。<br>
      📦 产品：一日营/3天备赛营 → 百度AI赛专项辅导（&#165;3,980-&#165;5,980）
    </div>
  </div>''',
    # Card 10 - 华为
    '''  <!-- 10. 华为 -->
  <div class="comp-card">
    <div class="comp-header">
      <div class="comp-name">&#x1F51F; 华为云青少年AI大赛</div>
      <div class="comp-badges">
        <span class="tag tag-blue">企业</span>
        <span class="tag tag-purple" style="background:#e9d8fd;">★★★ 可选</span>
      </div>
    </div>
    <div class="comp-meta">
      <span><strong>主办</strong>：华为云</span>
      <span><strong>年龄</strong>：10-18岁</span>
      <span><strong>费用</strong>：¥0</span>
    </div>
    <p style="font-size:14px;">华为云主办的青少年AI创新竞赛，聚焦AI应用开发与产业实践。参赛者使用华为云AI平台完成项目，含AI应用开发、智能硬件创新等方向。评审注重技术实现和产业落地潜力。</p>
    <div class="comp-match" style="background:#fffff0;border:1px solid #fefcbf;">
      ✅ <b>悦洋匹配</b>：高阶赛道，适合L3-L4学员。华为品牌背书对家长有较强吸引力。建议从ICC/NOC获奖学员中筛选推荐。<br>
      📦 产品：竞赛营5天（&#165;12,800-&#165;19,800）或VIP冲奖
    </div>
  </div>'''
]

for i, (start_marker, end_marker) in enumerate(card_markers):
    s = content.find(start_marker)
    if s == -1:
        print(f"ERROR: card marker {i+8} not found: {start_marker}")
        continue

    # Find the end of this comp-card
    # After the start_marker, find the next <!-- comment or </section>
    e = content.find(end_marker, s)
    if e == -1:
        print(f"ERROR: end marker for card {i+8} not found")
        continue

    # The card block starts at the comment line and ends at the last </div> before the next marker
    # Actually, let's find the full comp-card div
    card_start = content.find('<div class="comp-card">', s)
    if card_start == -1:
        card_start = s  # fallback

    # Find the closing </div> of this card
    # It's the </div> that closes comp-card, followed by newline+space+<!-- or newline+</section>
    # Let's find the last </div> before the next marker
    section_before_e = content[:e]
    last_div = section_before_e.rfind('</div>')
    if last_div != -1 and last_div > s:
        card_end = last_div + len('</div>')
    else:
        print(f"ERROR: could not find end of card {i+8}")
        continue

    # Replace content
    content = content[:s] + new_cards[i] + content[card_end:]
    changes += 1
    print(f"Card {i+8} replaced ({start_marker.strip()})")

# ===== 3. Update Part 3 (赛事分类) =====
# Replace the AI创新赛道 table
# Find the AI innovation table section
if '全球青少年AI峰会竞赛' in content:
    content = content.replace(
        '全球青少年AI峰会竞赛',
        '腾讯青少年人工智能大赛'
    )
    changes += 1
    print("Updated AI summit reference in Part 3")

# Add 百度 and 华为 lines after 腾讯 in the AI table
ai_table_pos = content.find('腾讯青少年人工智能大赛')
if ai_table_pos != -1:
    # Find next </tr>
    tr_end = content.find('</tr>', ai_table_pos)
    if tr_end != -1:
        extra = '\n        <tr><td>百度AI创意挑战赛</td><td><span class="tag tag-yellow">★★★★</span></td></tr>\n        <tr><td>华为云青少年AI大赛</td><td><span class="tag tag-purple">★★★</span></td></tr>'
        content = content[:tr_end+5] + extra + content[tr_end+5:]
        changes += 1
        print("Added 百度 and 华为 to AI table")

# Remove CTB from 商业创新 and ICW from 高阶/IP
for remove_str in [
    '<tr><td>CTB 全球青年研究创新论坛</td><td><span class="tag tag-purple">★★★</span></td></tr>\n',
    '<tr><td>ICW 世界青少年发明展</td><td><span class="tag tag-purple">★★★</span></td></tr>\n',
]:
    if remove_str in content:
        content = content.replace(remove_str, '')
        changes += 1
        print(f"Removed: {remove_str[:40]}")

# ===== 4. Update funnel =====
old_funnel = '全部赛事+ICW+全球AI峰会+留学'
new_funnel = '全部赛事+腾讯AI赛+百度AI赛+华为云AI赛+留学'
if old_funnel in content:
    content = content.replace(old_funnel, new_funnel)
    changes += 1
    print("Funnel updated")

# ===== 5. Update product coverage table =====
table_replacements = [
    ('<tr><td>CTB</td><td>—</td><td>—</td><td>—</td><td>✅ 陪跑</td></tr>',
     '<tr><td>腾讯AI大赛</td><td>✅ 一日营</td><td>✅ 3天营</td><td>✅ 竞赛营</td><td>✅ 陪跑</td></tr>'),
    ('<tr><td>ICW</td><td>—</td><td>—</td><td>—</td><td>✅ 陪跑</td></tr>',
     '<tr><td>百度AI挑战赛</td><td>✅ 一日营</td><td>✅ 3天营</td><td>✅ 竞赛营</td><td>✅ 陪跑</td></tr>'),
    ('<tr><td>全球AI峰会</td><td>—</td><td>—</td><td>—</td><td>✅ 陪跑</td></tr>',
     '<tr><td>华为云AI大赛</td><td>—</td><td>✅ 3天营</td><td>✅ 竞赛营</td><td>✅ 陪跑</td></tr>'),
]
for old, new in table_replacements:
    if old in content:
        content = content.replace(old, new)
        changes += 1
        print(f"Table row updated: {old[:30]}")

# ===== 6. Update execution strategy =====
content = content.replace(
    "悦洋海外集团客户直接对接口AI峰会/ICW",
    "对接腾讯/百度/华为等企业生态资源"
)
changes += 1
print("Execution strategy updated")

# ===== 7. Update highlight box =====
content = content.replace(
    "科创大赛+CTB+ICW+全球AI峰会为高阶及国际化差异化产品",
    "科创大赛+腾讯AI赛+百度AI挑战赛+华为云AI赛为企业背书差异化产品"
)
changes += 1
print("Highlight box updated")

with open("D:/Git/website/in/悦洋教育_竞赛产品矩阵分析_v3_10赛事.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n=== ALL DONE: {changes} changes made ===")
