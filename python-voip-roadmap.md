# Roadmap 30 Ngày Python cho VoIP & Solutions Engineer

## Mục tiêu tổng thể

- Xây nền tảng Python đủ dùng trong công việc vận hành tổng đài Asterisk/FreePBX.
- Biết đọc/ghi CDR, thao tác file/CSV, gọi REST API (CRM, SMS, AI…).
- Kết nối Python với Asterisk qua AGI/AMI, có 1 mini‑project end‑to‑end.
- Thời lượng: khoảng 1.5–2 giờ/ngày trong 30 ngày.

---

## Tuần 1 – Core Python & môi trường

**Mục tiêu tuần 1**

- Nắm: biến, kiểu dữ liệu cơ bản, if/for/while, function, list/dict, import module.
- Setup môi trường dev chuẩn: Python 3.11, venv, VS Code, pip, requirements.
- Viết được script CLI nhỏ xử lý text/log đơn giản.

### Ngày 1–2 – Setup & cú pháp cơ bản

- Cài Python 3.11, tạo virtualenv, cài đặt VS Code/IDE, pip, requirements.
- Làm quen:
  - Kiểu dữ liệu: int, float, str, bool.
  - Toán tử: +, -, *, /, %, //, ==, !=, >, <, in.
  - Cấu trúc điều kiện: if/elif/else.
  - Vòng lặp: for, while, range.
- Bài tập gợi ý:
  - Viết script hỏi người dùng nhập số phút gọi, tính tiền cước theo 1–2 mức đơn giản.

### Ngày 3–4 – List, dict, function

- List, tuple, dict, set, list/dict comprehension.
- Function: tham số, giá trị mặc định, return, unpack.
- Bài tập gợi ý (mô phỏng CDR):
  - Tạo list các dict CDR đơn giản: `[{"src": "101", "dst": "090...", "duration": 60}, ...]`.
  - Viết function `total_duration(cdr_list)` tính tổng thời lượng.
  - Viết function `filter_long_calls(cdr_list, min_sec=30)` trả về danh sách cuộc gọi dài hơn min_sec.

### Ngày 5–6 – Module, package, error handling

- Cách chia code thành nhiều file `.py`, import module khác nhau.
- Error handling: try/except/finally, một số exception hay gặp (ValueError, KeyError, FileNotFoundError…).
- Dùng thêm: datetime, pathlib, os, sys.
- Bài tập gợi ý:
  - Script đọc file log (vd: copy 1 file log Asterisk ra máy local) và đếm số dòng chứa "WARNING" hoặc "ERROR".
  - Thêm xử lý khi file không tồn tại (try/except).

### Ngày 7 – Ôn & mini‑project 1 (CDR Stats)

- Mini‑project: `cdr_stats.py`.
  - Input: file CSV CDR export từ FreePBX/Asterisk.
  - Output:
    - Tổng số cuộc gọi.
    - Tổng thời lượng.
    - Top 5 số gọi ra nhiều nhất theo `src`.
  - Áp dụng: for, if, dict để đếm, đọc file bằng `csv` module.

---

## Tuần 2 – File, CSV, JSON, HTTP, logging & config

**Mục tiêu tuần 2**

- Đọc/ghi file text, CSV, JSON.
- Gọi REST API với requests.
- Logging chuẩn với module logging.
- Dùng biến môi trường (.env) cho config.

### Ngày 8–9 – File & CSV

- `open`, context manager `with open(...) as f`, encoding.
- `csv.reader`, `csv.DictReader`, ghi CSV mới.
- Bài tập:
  - Merge 2 file CDR (vd: ngày 1 + ngày 2) thành 1 file, tránh trùng `uniqueid`.
  - Tách CDR thành nhiều file theo ngày dựa trên trường `start` (YYYY‑MM‑DD).

### Ngày 10–11 – JSON & REST API

- JSON:
  - `json.load`, `json.dump`, `json.loads`, `json.dumps`.
- HTTP client (`requests`):
  - Gửi GET/POST với params, headers, payload JSON.
  - Xử lý timeout, status code ≠ 200.
- Bài tập gợi ý:
  - Script đọc CDR, lọc missed call, gửi JSON summary lên 1 endpoint test (httpbin hoặc mock server).

### Ngày 12 – Logging & config

- Module logging:
  - Level: DEBUG, INFO, WARNING, ERROR.
  - Format log: thời gian, level, module, message.
- Config:
  - Đọc env (`os.getenv`) hoặc dùng `.env` + `python-dotenv`.
  - Tách file `config.py` riêng chứa AMI_HOST, AMI_USER, AMI_PASS, API_URL…

### Ngày 13–14 – Mini‑project 2: Missed Call Reporter (offline)

- Mini‑project:
  - Script đọc file CDR.
  - Lọc cuộc gọi `disposition = "NO ANSWER"`.
  - Gửi summary (JSON) tới 1 REST endpoint (CRM giả lập hoặc log file).
  - Ghi log:
    - Bao nhiêu record gửi thành công.
    - Bao nhiêu lỗi, retry tối thiểu 1 lần khi request fail.

---

## Tuần 3 – Python ↔ Asterisk qua AGI/AMI

**Mục tiêu tuần 3**

- Hiểu kiến trúc AGI, AMI.
- Dùng Python viết AGI script đơn giản.
- Dùng Python kết nối AMI để login, ping, sau đó mở rộng sang action khác.

### Ngày 15 – Kiến trúc AGI/AMI

- Ôn/bổ sung khái niệm:
  - AGI: script được gọi từ dialplan, giao tiếp qua stdin/stdout.
  - AMI: TCP socket tới port 5038, gửi action/nhận event để giám sát, originate, quản lý call.
- Đọc 1–2 ví dụ AGI Python từ tài liệu/communities.

### Ngày 16–17 – AGI Python cơ bản

- Cài thư viện hỗ trợ AGI (vd: pyst2/asterisk-agi) hoặc tự parse stdin.
- Viết AGI script:
  - Đọc env AGI (`agi_callerid`, `agi_uniqueid`, `agi_channel`…).
  - Ghi log bằng `VERBOSE` hoặc print.
  - Tùy CallerID, chọn file âm thanh playback khác nhau.
- Dialplan: dùng `AGI(your_script.py)` trong `extensions.conf` hoặc FreePBX Custom Destination.

### Ngày 18–19 – AMI bằng Python

- Tạo user AMI trong `manager.conf` (hoặc qua FreePBX GUI) với quyền phù hợp.
- Dùng Python + socket hoặc thư viện AMI (vd: starpy, pystrix):
  - Kết nối tới host:port AMI.
  - Gửi action `Login`, xử lý response.
  - Gửi action `Ping`, log kết quả.
- Bài tập:
  - Script `ami_ping.py` ping 5 lần, log thời gian response.

### Ngày 20–21 – Mini‑project 3: CallerID Enricher AGI

- Mini‑project:
  - File CSV phonebook: `Number, Name, InternalNumber`.
  - AGI script:
    - Lấy CallerID từ env.
    - Lookup CSV.
    - Nếu tìm thấy: set `CALLERID(name)` thành tên tương ứng, có thể thêm prefix [VIP]/[SPAM].
    - Nếu không: log unknown caller.
  - Dialplan: trước khi đổ chuông cho agent, gọi AGI, sau đó dùng CallerID mới.

---

## Tuần 4 – Mini‑project end‑to‑end Python ↔ VoIP

**Mục tiêu tuần 4**

- Gom toàn bộ skill: Python core + file/CSV + HTTP + logging + AGI/AMI.
- Xây 1 project nhỏ có thể show cho sếp/khách hàng như PoC.

### Chọn 1 trong 2 hướng

1. Missed Call Notifier Service
   - Flow:
     - Asterisk/AGI gửi thông tin call khi kết thúc.
     - Python service (FastAPI/Flask) nhận request, lưu vào DB/CSV.
     - Gửi tiếp webhook/Telegram/Zalo/Email báo missed call.

2. Auto Tagging & Routing Service
   - Flow:
     - Asterisk gửi CDR/event tới Python service.
     - Service gán tag (VIP/SPAM/Internal) bằng rule hoặc AI.
     - Dùng tag để phục vụ routing hoặc báo cáo.

### Ngày 22–24 – Thiết kế & skeleton project

- Thiết kế project:
  - Danh sách endpoint (vd: `POST /cdr`, `POST /missed-call`).
  - Cấu trúc thư mục (app/, agi/, ami/, core/…).
- Tạo skeleton (có thể dùng project skeleton đã cung cấp):
  - `core/config.py`: đọc env (AMI_HOST, AMI_USER, API_URL…).
  - `core/logging.py`: hàm `get_logger(name)`.
  - `main.py`: FastAPI app + `/health`.

### Ngày 25–27 – Kết nối với Asterisk

- Gắn AGI:
  - Deploy AGI script vào `agi-bin`.
  - `chmod +x` và bật `agi set debug on` để debug.
- Gắn AMI (nếu dùng):
  - Login AMI, subscribe event cần thiết (Newchannel, Hangup…).
- Kiểm thử end‑to‑end:
  - Gọi test từ softphone.
  - Xem log Python + log Asterisk.

### Ngày 28–30 – Hardening & tài liệu

- Thêm:
  - Retry khi gọi HTTP fail.
  - Timeout hợp lý cho API.
  - Correlation id: gắn `uniqueid` vào log để trace.
- Viết README:
  - Mô tả kiến trúc và flow.
  - Cách chạy project local.
  - 1–2 use‑case demo cụ thể.

---

## Gợi ý cách học hàng ngày

- 20–30 phút: xem tài liệu/video ngắn về chủ đề ngày hôm đó.
- 60–90 phút: code bài tập nhỏ gắn với VoIP (CDR, AGI, AMI, REST API…).
- 10 phút cuối: commit code, ghi lại hôm nay làm gì, mai làm tiếp gì.

Bạn có thể dùng file .md này trong Obsidian/Notion hoặc GitHub README để track tiến độ từng ngày (thêm checklist [ ] trước từng dòng).