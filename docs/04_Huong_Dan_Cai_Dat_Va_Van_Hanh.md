# TÀI LIỆU 04: HƯỚNG DẪN CÀI ĐẶT, VẬN HÀNH VÀ THỰC THI BENCHMARK

---

## 1. Yêu cầu Môi trường Hệ thống (Prerequisites)

Hệ thống yêu cầu các công cụ và môi trường thực thi sau:

| Thành phần | Phiên bản yêu cầu | Mục đích sử dụng |
| :--- | :--- | :--- |
| **Java Development Kit (JDK)** | **OpenJDK 21 LTS** (hoặc cao hơn) | Thực thi và biên dịch lõi thuật toán SPMF (EFIM & HUI-Miner) |
| **Python** | **Python 3.10+** (đã test trên 3.13) | Chạy harness kiểm thử tự động `benchmark.py` |
| **.NET SDK** | **.NET 8.0 SDK** | Phát triển và chạy Backend Web API |
| **Node.js** | **Node.js v20+** / npm | Phát triển và build giao diện Frontend ReactJS |
| **MySQL Server** | **MySQL 8.0+** | Lưu trữ danh mục sản phẩm, đơn hàng và kết quả HUI |
| **Git** | Mọi phiên bản hiện đại | Quản lý mã nguồn và nhánh thực nghiệm |

---

## 2. Cấu trúc Thư mục Dự án

```
research-high-utility-itemset/
├── autoresearch.sh             # Entrypoint thực thi kiểm chuẩn tự động
├── benchmark.py                # Script Python điều phối đo đạc và đối chiếu kết quả
├── .gitignore                  # Cấu hình bỏ qua file build và cache
├── lib/
│   └── spmf.jar                # Thư viện SPMF chuẩn đã build cho Java 21 LTS (7.0 MB)
├── data/
│   ├── foodmart.txt            # Tập dữ liệu mẫu Foodmart (4.141 đơn hàng)
│   ├── ecommerce.txt           # Tập dữ liệu Ecommerce gốc (mã ID thưa)
│   └── ecommerce_dense.txt     # Tập dữ liệu Ecommerce đã chuẩn hóa Dense ID (14.975 đơn)
├── src_spmf/                   # Toàn bộ mã nguồn mở rộng SPMF (hơn 3.000 file Java)
│   └── ca/pfv/spmf/algorithms/frequentpatterns/
│       ├── efim/               # Lõi thuật toán EFIM đã được tối ưu hóa
│       │   ├── AlgoEFIM.java
│       │   ├── Dataset.java
│       │   └── Transaction.java
│       └── hui_miner/          # Thuật toán HUI-Miner dùng để đối chứng
│           └── AlgoHUIMiner.java
└── docs/                       # Thư viện tài liệu kỹ thuật toàn diện của dự án
    ├── 01_Tong_Quan_Va_Co_So_Ly_Thuyet.md
    ├── 02_Bao_Cao_Thuc_Nghiem_So_Sanh_EFIM_HUIMiner.md
    ├── 03_Kien_Truc_He_Thong_Va_Thiet_Ke_Phan_Mem.md
    ├── 04_Huong_Dan_Cai_Dat_Va_Van_Hanh.md
    └── 05_Tong_Quan_Tai_Lieu_Tham_Khao_Literature_Review.md
```

---

## 3. Hướng dẫn Chạy Kiểm chuẩn Tự động (Running Benchmark)

Hệ thống được trang bị kịch bản kiểm chuẩn tự động một lệnh (`one-command benchmark`), cho phép:
1. Tự động biên dịch mọi thay đổi trong mã nguồn Java của EFIM vào thư mục `build/`.
2. Chạy thuật toán EFIM trên 2 tập dữ liệu chuẩn (`foodmart.txt` và `ecommerce_dense.txt`).
3. Chạy thuật toán HUI-Miner trên cùng 2 tập dữ liệu để lấy điểm đối chứng.
4. Tự động kiểm tra tính đúng đắn toán học: Đảm bảo 100% itemset và giá trị utility khớp nhau.
5. In ra các chỉ số đo lường hiệu năng chuẩn hóa.

### Lệnh thực thi trên Terminal (Linux / macOS / Windows Git Bash):
```bash
# 1. Di chuyển vào thư mục dự án
cd research-high-utility-itemset

# 2. Thực thi benchmark harness
bash autoresearch.sh
```

### Kết quả đầu ra mẫu trên Console:
```text
[FOODMART] EFIM: 191ms / 9.5MB | HUI-Miner: 301ms / 65.2MB | HUIs: 428
[ECOMMERCE] EFIM: 985ms / 22.9MB | HUI-Miner: 2057ms / 44.0MB | HUIs: 1051
METRIC efim_exec_time_ms=1177
METRIC huiminer_exec_time_ms=2355
METRIC efim_memory_mb=22.92
METRIC huiminer_memory_mb=64.98
METRIC hui_count=1479
METRIC speedup_ratio=2.001
```

---

## 4. Hướng dẫn Định dạng Dữ liệu Giao dịch (Data Format Guide)

Dữ liệu đầu vào của thuật toán khai phá sử dụng **định dạng chuẩn SPMF** (*Standard SPMF Format*), mỗi dòng đại diện cho một đơn hàng gồm 3 trường ngăn cách nhau bởi dấu hai chấm (`:`):

```
<Danh sách ID sản phẩm>:<Tổng lợi nhuận đơn hàng>:<Danh sách lợi nhuận từng sản phẩm>
```

### Ví dụ minh họa:
```text
1 3 5 7:27:6 6 10 5
```
- **`1 3 5 7`**: Đơn hàng mua 4 sản phẩm có mã ID là 1, 3, 5, và 7.
- **`27`**: Tổng giá trị lợi nhuận của toàn bộ đơn hàng ($6 + 6 + 10 + 5 = 27$).
- **`6 6 10 5`**: Lợi nhuận riêng lẻ của từng mặt hàng tương ứng ($u(1) = 6$, $u(3) = 6$, $u(5) = 10$, $u(7) = 5$).

---

## 5. Hướng dẫn Thiết lập Tầng Ứng dụng Web (ASP.NET Core & ReactJS)

### 5.1. Thiết lập Cơ sở dữ liệu MySQL
1. Khởi động MySQL Server.
2. Mở MySQL Workbench hoặc CLI và chạy toàn bộ mã DDL trong file `docs/03_Kien_Truc_He_Thong_Va_Thiet_Ke_Phan_Mem.md` (Mục 3).
3. Đảm bảo database `OnlineRetailDSS` được tạo thành công.

### 5.2. Cấu hình Backend ASP.NET Core
1. Mở file `appsettings.json` trong dự án backend và cấu hình chuỗi kết nối:
   ```json
   {
     "ConnectionStrings": {
       "DefaultConnection": "Server=localhost;Port=3306;Database=OnlineRetailDSS;User=root;Password=your_password;"
     },
     "MiningEngine": {
       "JarPath": "./lib/spmf.jar",
       "JavaExecutable": "java",
       "TempDirectory": "./temp/mining"
     }
   }
   ```
2. Khởi chạy Web API:
   ```bash
   dotnet restore
   dotnet run
   ```
   Swagger UI sẽ sẵn sàng tại địa chỉ `http://localhost:5000/swagger`.

### 5.3. Khởi chạy Frontend ReactJS
1. Cài đặt các gói phụ thuộc và chạy Vite dev server:
   ```bash
   npm install
   npm run dev
   ```
2. Truy cập hệ thống tại `http://localhost:5173`.

---

## 6. Xử lý Lỗi Thường gặp (Troubleshooting Guide)

### Lỗi 1: `OutOfMemoryError: Java heap space` khi đọc file giao dịch lớn
- **Nguyên nhân**: Mã sản phẩm trong file giao dịch có giá trị rời rạc quá lớn (ví dụ SKU `8512311`), làm mảng `utilityBinArrayLU = new int[maxItem + 1]` yêu cầu vượt quá RAM máy chủ.
- **Khắc phục**: Chạy script tiền xử lý Dense ID Mapping (`data/ecommerce_dense.txt`) để đưa các ID sản phẩm về dãy số liên tục $1, 2, \dots, N$.

### Lỗi 2: `java.lang.UnsupportedClassVersionError (class file version 69.0)`
- **Nguyên nhân**: File `spmf.jar` ban đầu của Philippe Fournier-Viger được build trên Java 25 không tương thích với máy cài Java 21 hoặc Java 17.
- **Khắc phục**: Dự án đã tích hợp sẵn `lib/spmf.jar` được recompile chuẩn xác trên OpenJDK 21 LTS (`target 21`, class version 65.0).
