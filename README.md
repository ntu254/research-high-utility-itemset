# Hệ Thống Hỗ Trợ Sắp Xếp Hàng Hóa Trưng Bày Trực Tuyến Qua So Sánh Thuật Toán Khai Phá Tập Mẫu Trọng Số Cao
*(Research and Development of an Online Product Arrangement Support System through a Comparative Study of High Utility Pattern Mining Algorithms)*

[![Java](https://img.shields.io/badge/Java-OpenJDK_21_LTS-orange.svg)](https://adoptium.net/)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![SPMF](https://img.shields.io/badge/SPMF-v2.66_Optimized-green.svg)](http://www.philippe-fournier-viger.com/spmf/)
[![License](https://img.shields.io/badge/License-GPL_v3-lightgrey.svg)](LICENSE_AGREEMENT_GPL3.txt)

---

## 1. Giới thiệu Dự án

Dự án thực hiện theo phương pháp **Nghiên cứu dựa trên học tập (Research-Based Learning - RBL)** nhằm giải quyết câu hỏi nghiên cứu khoa học cốt lõi:
> *"Thuật toán khai thác tập mẫu có giá trị trọng số cao nào giữa **HUI-Miner** và **EFIM** phù hợp hơn để hỗ trợ đề xuất sắp xếp hàng hóa trưng bày trong hệ thống bán lẻ trực tuyến?"*

Dự án kết hợp chặt chẽ giữa:
1. **Nghiên cứu thực nghiệm so sánh thuật toán**: Tối ưu hóa sâu mã nguồn thuật toán (CPU registers, zero-allocation scanner, memory page pre-touching) và kiểm chuẩn tự động trên các tập dữ liệu thương mại điện tử thực tế.
2. **Phát triển hệ thống phần mềm hỗ trợ ra quyết định (DSS)**: Thiết kế và tích hợp thuật toán tối ưu vào ứng dụng web thương mại điện tử 3 tầng (**ReactJS + ASP.NET Core 8 Web API + MySQL**).

---

## 2. Kết luận Nghiên cứu Cốt lõi (Key Findings)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SO SÁNH HIỆU NĂNG EFIM VS HUI-MINER                  │
├───────────────────────────────┬───────────────────┬────────────────────┤
│ Chỉ số đo lường               │ HUI-Miner (Gốc)   │ EFIM (Tối ưu hóa)  │
├───────────────────────────────┼───────────────────┼────────────────────┤
│ Thời gian chạy (15.000 đơn)   │ 2.057 ms          │   985 ms (Dưới 1s) │
│ Tổng thời gian thực thi       │ 2.355 ms          │ 1.177 ms (Nhanh 2x)│
│ Dung lượng bộ nhớ RAM đỉnh    │ 64.98 MB          │  22.92 MB (-65%)   │
│ Cấu trúc dữ liệu chính        │ Utility-Lists     │ 1D Utility Bins    │
│ Kỹ thuật nén dữ liệu          │ Không có          │ Transaction Merging│
│ Độ trùng khớp kết quả         │ 1.479 HUIs        │ 1.479 HUIs (100%)  │
└───────────────────────────────┴───────────────────┴────────────────────┘
```

- **EFIM là thuật toán tối ưu vượt trội**: Nhanh gấp đôi (**2.00x speedup**) và tiêu thụ lượng RAM chỉ bằng **$1/3$** đối thủ HUI-Miner.
- **Phá vỡ rào cản 1 giây**: Đạt thời gian xử lý **985 ms** cho gần 15.000 giao dịch e-commerce thực tế, đảm bảo khả năng phản hồi tức thời (*near real-time*) cho các ứng dụng web.
- **Phát hiện thực chiến về mã SKU thưa (Sparse SKU ID)**: EFIM yêu cầu tiền xử lý **Dense ID Mapping** ($1 \dots N$) để tránh tràn bộ nhớ khi đọc mã barcode/SKU dài từ database.

---

## 3. Hệ Thống Tài Liệu Kỹ Thuật Toàn Diện (`docs/`)

Toàn bộ tài liệu chi tiết phục vụ báo cáo tiến độ và luận văn tốt nghiệp được cấu trúc đầy đủ trong thư mục `docs/`:

| Tài liệu | Nội dung chi tiết |
| :--- | :--- |
| [**01. Tổng quan & Cơ sở Lý thuyết**](docs/01_Tong_Quan_Va_Co_So_Ly_Thuyet.md) | Bối cảnh, công thức toán học HUPM ($TU$, $TWU$, $TWDC$), nguyên lý HUI-Miner và EFIM. |
| [**02. Báo cáo Thực nghiệm So sánh**](docs/02_Bao_Cao_Thuc_Nghiem_So_Sanh_EFIM_HUIMiner.md) | Bảng theo dõi 18 lượt chạy, phân tích tối ưu hóa Zero-allocation parser, register caching. |
| [**03. Kiến trúc Hệ thống & Phần mềm**](docs/03_Kien_Truc_He_Thong_Va_Thiet_Ke_Phan_Mem.md) | Kiến trúc 3 tầng, ERD & DDL MySQL, đặc tả REST API, thuật toán chuyển đổi HUI sang layout kệ hàng. |
| [**04. Hướng dẫn Cài đặt & Vận hành**](docs/04_Huong_Dan_Cai_Dat_Va_Van_Hanh.md) | Yêu cầu môi trường, cấu trúc thư mục, lệnh chạy benchmark harness, cấu hình backend/frontend. |
| [**05. Tổng quan Tài liệu Tham khảo**](docs/05_Tong_Quan_Tai_Lieu_Tham_Khao_Literature_Review.md) | Phân tích 12 bài báo khoa học chuẩn IEEE/ACM/KAIS/SDM, bảng tiến hóa thuật toán 2004–2017. |

---

## 4. Chạy Nhanh Kiểm Chuẩn (Quickstart Benchmark)

Chỉ cần một lệnh duy nhất để tự động biên dịch mã nguồn Java tối ưu và chạy benchmark đối chứng:

```bash
# Clone và chuyển vào thư mục dự án
cd research-high-utility-itemset

# Chạy kiểm chuẩn đối chiếu EFIM vs HUI-Miner
bash autoresearch.sh
```

Kết quả in trên màn hình hiển thị đầy đủ thời gian chạy, bộ nhớ đỉnh và xác minh khớp chính xác 100% của 1.479 High Utility Itemsets.

---

## 5. Công Nghệ Áp Dụng (Tech Stack)

- **Frontend**: ReactJS 18, Vite, TailwindCSS, Ant Design, Lucide Icons.
- **Backend**: ASP.NET Core 8.0 Web API, Entity Framework Core 8, Dapper ORM.
- **Database**: MySQL 8.0 Community Server.
- **Core Mining Engine**: SPMF Data Mining Library (Java 21 LTS Hotspot).
- **Automation & Test Harness**: Python 3.13, Bash script, Git.
