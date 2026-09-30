import csv
import json
import sys
from pathlib import Path

# 스크립트와 같은 폴더의 장데이터.json을 읽습니다.
if len(sys.argv) != 2 or not sys.argv[1].strip():
    sys.exit('사용법: python solution.py "키워드"')
keyword = sys.argv[1]
if any(c in keyword for c in '<>:"/\\|?*') or any(ord(c) < 32 for c in keyword):
    sys.exit('키워드에 파일명으로 사용할 수 없는 문자가 있습니다.')
base = Path(__file__).resolve().parent
chapters = json.loads((base / '장데이터.json').read_text(encoding='utf-8-sig'))
selected = [chapter for chapter in chapters if keyword in chapter['본문']]
output = base / f'결과_{keyword}.csv'
# UTF-8 BOM을 넣어 엑셀에서도 한글이 깨지지 않게 저장합니다.
with output.open('w', encoding='utf-8-sig', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['장', '제목', '본문'])
    writer.writeheader()
    writer.writerows(selected)
print(f'[OK] {len(selected)}건 저장 → {output.name}')
