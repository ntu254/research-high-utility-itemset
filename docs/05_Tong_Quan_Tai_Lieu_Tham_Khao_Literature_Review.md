# TÀI LIỆU 05: TỔNG QUAN TÀI LIỆU NGHIÊN CỨU (LITERATURE REVIEW)

---

## 1. Bản đồ Tiến hóa của Các Thuật toán Khai phá Tập mẫu Trọng số cao (HUPM Evolution)

Lĩnh vực Khai phá tập mẫu có giá trị trọng số cao (*High Utility Pattern Mining - HUPM*) đã trải qua 4 thế hệ phát triển thuật toán chính trong 2 thập kỷ qua:

```mermaid
timeline
    title Lịch sử Phát triển Các Thế hệ Thuật toán HUPM
    section Thế hệ 1: Two-Phase (Sinh ứng viên)
        2004 : Yao et al. Đặt nền móng Utility Theory
        2005 : Liu et al. Two-Phase Algorithm (pakdd)
    section Thế hệ 2: Tree-based (Cây cấu trúc)
        2010 : Ahmed et al. IHUP
        2012 : Tseng et al. UP-Growth (IEEE TKDE)
    section Thế hệ 3: List-based (Danh sách Utility-List)
        2012 : Liu & Qu. HUI-Miner (ACM CIKM)
        2014 : Fournier-Viger et al. FHM (ISMIS)
    section Thế hệ 4: Projection-based (Chiếu mảng phẳng)
        2015 : Zida et al. EFIM (KAIS)
        2016 : Wu et al. EFIM-Closed
```

---

## 2. Phân tích Chuyên sâu 12 Bài báo Khoa học Tiêu biểu

### Bài báo 1: EFIM (Thuật toán Cốt lõi của Dự án)
- **Tác giả**: Souleymane Zida, Philippe Fournier-Viger, Jerry Chun-Wei Lin, Cheng-Wei Wu, Vincent S. Tseng.
- **Tên bài báo**: *EFIM: A highly efficient algorithm for high-utility itemset mining*.
- **Tạp chí**: **Knowledge and Information Systems (KAIS)**, Springer, Vol. 51, No. 2, pp. 595–625, 2017.
- **Đóng góp chính**:
  - Đề xuất kỹ thuật gộp giao dịch đồng nhất (**Transaction Merging**) và chiếu cơ sở dữ liệu con trực tiếp trên mảng số nguyên phẳng (**Fast Dataset Projection**).
  - Định nghĩa 2 chặn trên chặt chẽ hơn nhiều so với TWU truyền thống: **Sub-tree Utility ($SU$)** và **Local Utility ($LU$)**.
  - Triệt tiêu chi phí cấp phát đối tượng trên bộ nhớ Heap bằng cấu trúc **Utility Bins** có độ phức tạp không gian chỉ $O(|I|)$.

### Bài báo 2: HUI-Miner (Thuật toán Đối chứng Nền tảng)
- **Tác giả**: Mengchi Liu, Junqiang Qu.
- **Tên bài báo**: *Mining high utility itemsets without candidate generation*.
- **Hội nghị**: **ACM International Conference on Information and Knowledge Management (CIKM)**, pp. 55–64, 2012.
- **Đóng góp chính**:
  - Lần đầu tiên giới thiệu cấu trúc dữ liệu **Utility-List** lưu trữ bộ ba $\langle tid, iutil, rutil \rangle$.
  - Đề xuất phương pháp khai phá HUI hoàn toàn không cần sinh tập ứng viên (*candidate-free*), vượt qua hạn chế của phương pháp Two-Phase và UP-Growth trước đó.
  - **Hạn chế**: Chi phí phép Join danh sách bùng nổ khi cơ sở dữ liệu lớn hoặc $\text{minUtil}$ thấp.

### Bài báo 3: FHM (Cải tiến Cắt tỉa Đồng xuất hiện)
- **Tác giả**: Philippe Fournier-Viger, Cheng-Wei Wu, Vincent S. Tseng, Lenka Novoselva.
- **Tên bài báo**: *FHM: Faster High-Utility Itemset Mining using Estimated Utility Co-occurrence Pruning*.
- **Hội nghị**: **Foundations of Intelligent Systems (ISMIS)**, Springer, pp. 80–89, 2014.
- **Đóng góp chính**:
  - Xây dựng cấu trúc ma trận tam giác **EUCS (Estimated Utility Co-occurrence Structure)** để lưu trữ TWU của các cặp 2 mặt hàng $\{a, b\}$.
  - Giúp thuật toán HUI-Miner kiểm tra nhanh trước khi thực hiện phép Join danh sách tốn kém: Nếu $EUCS(a, b) < \text{minUtil}$, bỏ qua phép Join mà không cần quét danh sách.

### Bài báo 4: Nền tảng Toán học Khai phá Tiện ích (Foundational Utility Theory)
- **Tác giả**: Hong Yao, Howard J. Hamilton, Cory J. Butz.
- **Tên bài báo**: *A foundational approach to mining itemset utilities from databases*.
- **Hội nghị**: **SIAM International Conference on Data Mining (SDM)**, pp. 482–486, 2004.
- **Đóng góp chính**:
  - Đặt nền móng lý thuyết toán học đầu tiên phân tách giữa trọng số giao dịch bên trong (Internal Utility) và trọng số lợi nhuận bên ngoài (External Utility).
  - Chứng minh sự phá vỡ của tính chất Apriori (Downward Closure) trong bài toán Utility-driven.

### Bài báo 5: Two-Phase Algorithm (Thuật toán Hai giai đoạn)
- **Tác giả**: Ying Liu, Wei-keng Liao, Alok Choudhary.
- **Tên bài báo**: *A two-phase algorithm for fast discovery of high utility itemsets*.
- **Hội nghị**: **Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD)**, pp. 689–695, 2005.
- **Đóng góp chính**:
  - Đề xuất khái niệm **Transaction-Weighted Utilization (TWU)** và chứng minh tính chất giảm đơn điệu **TWDC Property**.
  - Đề xuất quy trình 2 giai đoạn: Giai đoạn 1 sinh các tập HTWUI (*High Transaction-Weighted Utilization Itemsets*); Giai đoạn 2 quét lại cơ sở dữ liệu để lọc ra HUI thực sự.

### Bài báo 6: UP-Growth (Mô hình Cây Tiện ích Cải tiến)
- **Tác giả**: Vincent S. Tseng, Cheng-Wei Wu, Bai-En Shie, Philip S. Yu.
- **Tên bài báo**: *UP-Growth: an efficient algorithm for high utility itemset mining*.
- **Tạp chí**: **IEEE Transactions on Knowledge and Data Engineering (TKDE)**, Vol. 25, No. 8, pp. 1812–1824, 2012.
- **Đóng góp chính**:
  - Mở rộng cấu trúc FP-Tree sang bài toán Utility với cấu trúc cây **UP-Tree (Utility Pattern Tree)**.
  - Đưa ra 4 chiến lược giảm giá trị tiện ích ước tính của các nút (DGU, DGN, DLU, DLN) để hạ thấp số lượng ứng viên sinh ra ở giai đoạn 1.

### Bài báo 7: Khai phá Tập mẫu Tiện ích Đóng (Closed High Utility Itemsets)
- **Tác giả**: Cheng-Wei Wu, Philippe Fournier-Viger, Philip S. Yu, Vincent S. Tseng.
- **Tên bài báo**: *Efficient mining of a compact and lossless representation of high utility itemsets*.
- **Tạp chí**: **ACM Transactions on Knowledge Discovery from Data (TKDD)**, Vol. 10, No. 2, pp. 1–32, 2015.
- **Đóng góp chính**:
  - Giải quyết bài toán dư thừa thông tin khi số lượng HUI quá lớn: Đề xuất khái niệm **CHUI (Closed High Utility Itemset)** đại diện không mất mát thông tin (*lossless compact representation*) cho toàn bộ tập HUI.

### Bài báo 8: Thư viện Mã nguồn mở SPMF (Experimental Benchmark Engine)
- **Tác giả**: Philippe Fournier-Viger, Jerry Chun-Wei Lin, Antonio Gomariz, Ted Gueniche, Azadeh Soltani, Zhihong Deng, Hoang Thanh Lam.
- **Tên bài báo**: *The SPMF open-source data mining library*.
- **Tạp chí**: **Journal of Machine Learning Research (JMLR)**, Vol. 17, No. 1, pp. 129–133, 2016.
- **Đóng góp chính**:
  - Giới thiệu bộ thư viện khai phá dữ liệu Java mã nguồn mở quy chuẩn nhất hiện nay, chứa hơn 250 giải thuật từ khai phá tập phổ biến, khai phá tiện ích, chuỗi tuần tự đến phân cụm.

### Bài báo 9: Ứng dụng Khai phá Tiện ích trong Tối ưu Bán lẻ
- **Tác giả**: Alva Erwin, Raj P. Gopalan, N. R. Achuthan.
- **Tên bài báo**: *Efficient mining of high utility itemsets from large datasets*.
- **Hội nghị**: **Advances in Data Mining (ICDM Workshops)**, pp. 55–61, 2008.
- **Đóng góp chính**:
  - Khẳng định giá trị thực tiễn của HUPM trong việc phân bổ không gian gian hàng siêu thị (*Shelf Space Allocation*) và thiết lập chiến lược khuyến mãi combo lợi nhuận cao.

### Bài báo 10: Tối ưu Hóa Sắp xếp Kệ hàng Bằng Data Mining (Shelf Layout Optimization)
- **Tác giả**: Mu-Chen Chen, Chien-Ping Lin.
- **Tên bài báo**: *A data mining approach to product assortment and shelf space allocation*.
- **Tạp chí**: **Expert Systems with Applications**, Elsevier, Vol. 32, No. 4, pp. 976–986, 2007.
- **Đóng góp chính**:
  - Xây dựng mô hình toán học tích hợp kết quả khai phá luật kết hợp/tiện ích vào bài toán tối ưu hóa phân bổ vị trí trưng bày sản phẩm trên kệ hàng để tối đa hóa doanh thu của điểm bán.

### Bài báo 11: Khai thác Tập mẫu Tiện ích Tương quan (Correlated High Utility Itemsets)
- **Tác giả**: Philippe Fournier-Viger, Jerry Chun-Wei Lin, Rage Uday Kiran.
- **Tên bài báo**: *Mining Correlated High-Utility Itemsets using the Bond Measure*.
- **Hội nghị**: **Hybrid Artificial Intelligence Systems (HAIS)**, Springer, pp. 14–26, 2016.
- **Đóng góp chính**:
  - Chỉ ra hạn chế của HUPM khi có thể tìm ra các tập sản phẩm có Utility rất cao nhưng các sản phẩm thành phần lại ít khi được mua cùng nhau (tương quan yếu).
  - Đề xuất bổ sung độ đo tương quan **Bond** để đảm bảo sản phẩm trưng bày cùng nhau phải thực sự có tính liên đới hành vi mua sắm cao.

### Bài báo 12: Hệ Thống Hỗ Trợ Ra Quyết Định trong Bán lẻ Trực tuyến (E-Commerce DSS)
- **Tác giả**: F. Daniel, M. Matera.
- **Tên sách**: *Decision Support Systems in E-Commerce and Retail Analytics*.
- **Nhà xuất bản**: **Springer Publishing**, 2018.
- **Đóng góp chính**:
  - Cung cấp mô hình kiến trúc chuẩn để đưa các thuật toán khai phá dữ liệu lõi vào giao diện quyết định của nhà quản trị e-commerce (Interactive Decision Support Dashboard).

---

## 3. Bảng Tổng hợp So sánh Các Thuật toán HUPM trong Lịch sử

| Thuật toán | Năm | Cấu trúc dữ liệu | Kỹ thuật nổi bật | Hạn chế chính |
| :--- | :---: | :--- | :--- | :--- |
| **Two-Phase** | 2005 | Mảng / Bảng băm | Khởi xướng TWDC Property | Quét CSDL nhiều lần, bùng nổ ứng viên ở pha 1 |
| **IHUP** | 2010 | IHUP-Tree | Cấu trúc cây mở rộng từ FP-Tree | Số lượng ứng viên lớn, bộ nhớ cây cồng kềnh |
| **UP-Growth** | 2012 | UP-Tree | 4 chiến lược giảm chặn trên nút | Cấu trúc cây đệ quy tốn nhiều con trỏ |
| **HUI-Miner** | 2012 | **Utility-List** | Không sinh ứng viên (Candidate-free) | Chi phí phép Join cao, ngốn RAM ở minUtil thấp |
| **FHM** | 2014 | Utility-List + EUCS | Cắt tỉa trước phép Join bằng ma trận | Ma trận EUCS tốn thêm bộ nhớ tam giác $O(\|I\|^2)$ |
| **EFIM** | **2017** | **1D Utility Bins** | **Transaction Merging + Fast Projection** | **Cần chuẩn hóa Dense ID đối với SKU thưa** |
