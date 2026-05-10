# VoIP Python Lab

Repo cá nhân để học Python theo roadmap 30 ngày và áp dụng trực tiếp vào VoIP (Asterisk/FreePBX) và hướng Solutions Engineer.

## Cấu trúc thư mục

```text
voip-python-lab/
  README.md
  .gitignore
  roadmap/
  app/
  practice/
  asterisk_lab/
  docs/
  tests/
```

- `roadmap/`: chứa lộ trình 30 ngày (`python-voip-roadmap.md`).
- `app/`: project "thật" – FastAPI + AGI + AMI, dần refactor thành giải pháp SE.
- `practice/`: bài tập theo tuần (week01_core, week02_files_http, …).
- `asterisk_lab/`: dialplan mẫu, AGI đã deploy, ghi chú riêng cho tổng đài.
- `docs/`: notes hàng tuần, ý tưởng giải pháp.
- `tests/`: test cho các module xử lý logic (để dành phase sau).

## Bắt đầu

1. Tạo virtualenv và cài thư viện:

   ```bash
   python -m venv .venv
   # Windows: .\.venv\Scripts\activate
   # Linux/macOS: source .venv/bin/activate
   pip install fastapi uvicorn[standard]
   ```

2. Chạy API skeleton:

   ```bash
   uvicorn app.main:app --reload
   ```

   Mở http://127.0.0.1:8000/health để kiểm tra.

3. Học theo roadmap:

   - Mỗi ngày xem mục tương ứng trong `roadmap/python-voip-roadmap.md`.
   - Viết bài tập vào `practice/weekXX_*/`.
   - Khi một đoạn code đủ hữu ích cho "production", refactor nó vào `app/`.

4. Gắn với Asterisk:

   - Lưu dialplan mẫu vào `asterisk_lab/dialplan_samples/`.
   - Lưu AGI script đã deploy vào `asterisk_lab/agi/deployed/`.

## Gợi ý workflow

- Sáng/tối: 15–20 phút đọc roadmap + tài liệu ngắn.
- 60 phút code bài tập trong `practice/` hoặc thêm tính năng nhỏ cho `app/`.
- 10 phút ghi note tuần trong `docs/notes/` và tick checklist trong roadmap.
