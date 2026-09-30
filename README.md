# 2026 디지털혁신 백서 검색

웹페이지는 장데이터.json을 자동으로 읽고 제목 또는 본문을 검색합니다. 외부 이미지로 Wikimedia Commons 태극기를 표시합니다.

## Python 실행
solution.py와 장데이터.json을 같은 폴더에 두고 실행합니다.

```bash
python solution.py "사업"
```

본문에 키워드가 포함된 장을 결과_사업.csv로 저장합니다. 헤더는 장, 제목, 본문이며 UTF-8 BOM으로 저장합니다. Python 표준 라이브러리만 사용합니다.
