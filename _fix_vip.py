# coding: utf-8
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("D:/Git/website/in/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find and replace lines containing VIP冲奖营 and 比赛孵化服务
new_lines = []
skip_next = False
replaced = False

for i, line in enumerate(lines):
    if 'VIP冲奖营' in line and '比赛孵化服务' in lines[i+1] if i+1 < len(lines) else False:
        # Replace these two lines with one new line
        new_lines.append('\t      <tr><td>VIP冲奖教练辅导</td><td>1对1教练</td><td>有项目基础</td><td><span class="tag draft">待启动</span></td><td>¥20,000+</td></tr>\n')
        skip_next = True
        replaced = True
    elif skip_next:
        skip_next = False
    else:
        new_lines.append(line)

if replaced:
    with open("D:/Git/website/in/index.html", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("SUCCESS: replaced")
else:
    print("NOT FOUND - trying line-by-line")
    # Try line-by-line approach
    for i, line in enumerate(lines):
        if 'VIP冲奖营' in line:
            print(f"Found VIP冲奖营 at line {i+1}: {repr(line[:60])}")
        if '比赛孵化服务' in line:
            print(f"Found 比赛孵化服务 at line {i+1}: {repr(line[:60])}")
