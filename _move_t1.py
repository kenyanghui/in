# coding: utf-8
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("D:/Git/website/in/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
removed = False
for line in lines:
    if '海外华裔寻根研学营' in line and '$2,000' in line:
        removed = True
        print(f"Removed: {repr(line[:60])}")
        continue
    new_lines.append(line)

if removed:
    with open("D:/Git/website/in/index.html", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Old line removed successfully")
else:
    print("No line found to remove")

print("DONE")
