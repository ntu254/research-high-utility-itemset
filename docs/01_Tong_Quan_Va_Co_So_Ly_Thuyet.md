# TÀI LIỆU 01: TỔNG QUAN DỰ ÁN VÀ CƠ SỞ LÝ THUYẾT KHAI PHÁ TẬP MẪU CÓ GIÁ TRỊ TRỌNG SỐ CAO (HUPM)

---

## 1. Bối cảnh Nghiên cứu và Câu hỏi Nghiên cứu (Research Context & Question)

### 1.1. Bối cảnh thực tiễn
Sự bùng nổ của thương mại điện tử (E-commerce) tạo ra khối lượng dữ liệu giao dịch khổng lồ (*Transactional Big Data*). Trong mỗi đơn hàng, hành vi mua sắm của khách hàng không chỉ phản ánh mối liên hệ kết hợp giữa các mặt hàng mà còn phản ánh giá trị thặng dư kinh tế (doanh thu và lợi nhuận) đóng góp cho doanh nghiệp.

Tuy nhiên, phần lớn các cửa hàng trực tuyến hiện nay vẫn sắp xếp, trưng bày sản phẩm trên website (gợi ý trang chi tiết sản phẩm, gợi ý giỏ hàng, banner trang chủ) dựa trên **kinh nghiệm chủ quan của người quản lý** hoặc các tiêu chí đơn giản như mặt hàng bán chạy nhất (*bestseller*). Cách tiếp cận này bỏ sót cơ hội bán chéo (*cross-selling*) và bán gia tăng (*upselling*) các cụm sản phẩm có lợi nhuận biên cao nhưng tần suất mua ở mức trung bình.

### 1.2. Giới hạn của Khai thác tập phổ biến truyền thống (Frequent Itemset Mining - FIM)
Các giải thuật khai phá luật kết hợp cổ điển như **Apriori** (Agrawal & Srikant, 1994) và **FP-Growth** (Han et al., 2000) dựa trên độ hỗ trợ (*Support*) và độ tin cậy (*Confidence*):
- **Xem mọi sản phẩm có giá trị như nhau**: Mỗi mặt hàng chỉ được biểu diễn nhị phân ($1$ nếu xuất hiện trong đơn hàng, $0$ nếu không).
- **Nghịch lý mặt hàng giá trị thấp**: Những mặt hàng thông dụng giá rẻ (như túi nilon, kẹo que, gia vị) có tần suất mua rất cao nhưng lợi nhuận biên gần bằng 0. Ngược lại, các cụm sản phẩm giá trị cao (như laptop kèm bàn phím cơ và màn hình đồ họa) xuất hiện ít hơn ngưỡng $\text{min\_sup}$ nên bị loại bỏ hoàn toàn.

### 1.3. Khai phá tập mẫu có giá trị trọng số cao (High Utility Pattern Mining - HUPM)
HUPM ra đời nhằm khắc phục triệt để hạn chế trên bằng cách tích hợp đồng thời hai yếu tố:
1. **Trọng số bên trong (Internal Utility - $q$)**: Số lượng mua của từng mặt hàng trong từng giao dịch cụ thể.
2. **Trọng số bên ngoài (External Utility - $p$)**: Lợi nhuận đơn vị, biên lợi nhuận, hoặc mức độ ưu tiên chiến lược kinh doanh của mặt hàng.

### 1.4. Câu hỏi nghiên cứu (Research Question)
Trong số các thuật toán HUPM hiện đại, **HUI-Miner** (Liu & Qu, CIKM 2012) và **EFIM** (Zida et al., KAIS 2017) là hai thuật toán tiêu biểu nhất đại diện cho hai trường phái cấu trúc dữ liệu khác nhau (danh sách liên kết Utility-List vs mảng phẳng Utility Bins). Đề tài tập trung giải quyết câu hỏi:

> **"Which High Utility Pattern Mining algorithm (HUI-Miner or EFIM) is more suitable for supporting product arrangement recommendations in online retail systems?"**  
> *(Thuật toán khai thác tập mẫu có giá trị trọng số cao nào giữa HUI-Miner và EFIM phù hợp hơn để hỗ trợ đề xuất sắp xếp hàng hóa trưng bày trong hệ thống bán lẻ trực tuyến?)*

---

## 2. Nền tảng Toán học của High Utility Pattern Mining

Cho tập hữu hạn các mặt hàng $I = \{i_1, i_2, \dots, i_n\}$ và một cơ sở dữ liệu giao dịch $D = \{T_1, T_2, \dots, T_m\}$. Mỗi giao dịch $T_q \in D$ ($1 \le q \le m$) là một tập con của $I$ ($T_q \subseteq I$) kèm theo mã định danh duy nhất $TID$.

Mỗi mặt hàng $i \in I$ có một trọng số lợi nhuận đơn vị $p(i) \in \mathbb{R}^+$ (External Utility).  
Trong mỗi giao dịch $T_q$, mặt hàng $i$ có số lượng mua $q(i, T_q) \in \mathbb{Z}^+$ (Internal Utility).

### 2.1. Các định nghĩa toán học cốt lõi

#### Định nghĩa 1: Giá trị Utility của một mặt hàng trong giao dịch
Giá trị lợi nhuận của mặt hàng $i$ trong giao dịch $T_q$, ký hiệu là $u(i, T_q)$, được định nghĩa:
$$u(i, T_q) = p(i) \times q(i, T_q)$$

#### Định nghĩa 2: Giá trị Utility của một tập mặt hàng (Itemset) trong giao dịch
Cho tập mặt hàng $X \subseteq I$. Utility của $X$ trong giao dịch $T_q$, ký hiệu là $u(X, T_q)$, được tính bằng:
$$u(X, T_q) = \begin{cases} 
\sum_{i \in X} u(i, T_q) & \text{nếu } X \subseteq T_q \\ 
0 & \text{nếu } X \not\subseteq T_q 
\end{cases}$$

#### Định nghĩa 3: Tổng giá trị Utility của một tập mặt hàng trong cơ sở dữ liệu
Tổng giá trị lợi nhuận của $X$ trong toàn bộ cơ sở dữ liệu $D$, ký hiệu là $u(X)$, được tính bằng:
$$u(X) = \sum_{T_q \in D, X \subseteq T_q} u(X, T_q)$$

#### Định nghĩa 4: Tập mẫu có giá trị trọng số cao (High Utility Itemset - HUI)
Cho trước một ngưỡng lợi nhuận tối thiểu do người quản lý quy định là $\text{minUtil} > 0$. Một tập mặt hàng $X$ được gọi là một **High Utility Itemset (HUI)** nếu và chỉ nếu:
$$u(X) \ge \text{minUtil}$$

---

### 2.2. Vấn đề mất tính đơn điệu và Kỹ thuật TWU Pruning

#### Thách thức: Hàm Utility không thỏa mãn Apriori Property
Trong khai thác tập phổ biến (FIM), hàm Support thỏa mãn tính chất giảm đơn điệu (*Downward Closure Property*): nếu $X \subset Y$ thì $\text{support}(Y) \le \text{support}(X)$. Do đó, nếu $X$ không phổ biến thì mọi tập cha $Y$ chắc chắn không phổ biến.

Tuy nhiên, hàm Utility $u(X)$ **không có tính chất giảm đơn điệu**:
- Ví dụ: Bán một cây bút bi có $u(\{Bút\}) = 5.000$ VNĐ. Nhưng khi bán kèm sổ da cao cấp, tập $\{Bút, Sổ\}$ có thể mang lại $u(\{Bút, Sổ\}) = 200.000$ VNĐ $> u(\{Bút\})$.
- **Hệ quả**: Không thể loại bỏ một mặt hàng chỉ vì lợi nhuận độc lập của nó nhỏ hơn $\text{minUtil}$, dẫn đến không gian tìm kiếm bùng nổ tổ hợp $2^{|I|}$.

#### Giải pháp: Transaction-Weighted Utilization (TWU)
Để thiết lập chặn trên (*upper bound*) có tính chất giảm đơn điệu, các nhà nghiên cứu đưa ra khái niệm **TWU**:

#### Định nghĩa 5: Transaction Utility (TU)
Tổng lợi nhuận của toàn bộ đơn hàng $T_q$:
$$TU(T_q) = \sum_{i \in T_q} u(i, T_q)$$

#### Định nghĩa 6: Transaction-Weighted Utilization (TWU)
Tổng TU của tất cả các giao dịch có chứa tập mặt hàng $X$:
$$TWU(X) = \sum_{T_q \in D, X \subseteq T_q} TU(T_q)$$

#### Định lý: Tính chất Transaction-Weighted Downward Closure (TWDC Property)
Cho hai tập mặt hàng $X$ và $Y$. Nếu $X \subset Y$, thì:
$$TWU(X) \ge TWU(Y) \ge u(Y)$$

**Hệ quả cắt tỉa quan trọng nhất:**  
Nếu $TWU(X) < \text{minUtil}$, thì với mọi tập cha $Y \supset X$, ta chắc chắn có $u(Y) < \text{minUtil}$. Do đó, toàn bộ không gian nhánh con mở rộng từ $X$ có thể bị **cắt tỉa hoàn toàn** ngay lập tức mà không sợ bỏ sót bất kỳ HUI nào.

---

## 3. Phân tích Nguyên lý Hoạt động của Thuật toán HUI-Miner

### 3.1. Ý tưởng cốt lõi
HUI-Miner (Liu & Qu, 2012) là thuật toán đầu tiên khai thác HUI theo phương pháp **không sinh ứng viên (candidate-free)** thông qua một cấu trúc dữ liệu mới gọi là **Utility-List**.

### 3.2. Cấu trúc dữ liệu Utility-List
Với mỗi tập mặt hàng $X$, `UtilityList(X)` lưu trữ danh sách các bộ ba phần tử (*elements*) tương ứng với các giao dịch chứa $X$:
$$\text{Element} = \langle tid, iutil, rutil \rangle$$
- **$tid$**: Mã định danh của giao dịch $T_{tid}$ chứa $X$.
- **$iutil$**: Lợi nhuận thực của $X$ trong giao dịch đó: $iutil = u(X, T_{tid})$.
- **$rutil$** (*Remaining Utility*): Lợi nhuận còn lại của các mặt hàng đứng sau $X$ trong giao dịch $T_{tid}$ theo một thứ tự sắp xếp cố định $\succ$ (thường là thứ tự tăng dần của TWU):
  $$rutil = \sum_{i \in T_{tid} \setminus X, i \succ x_k, \forall x_k \in X} u(i, T_{tid})$$

### 3.3. Cơ chế duyệt và Cắt tỉa của HUI-Miner
Thuật toán duyệt không gian tìm kiếm theo chiều sâu (Depth-First Search - DFS) trên cây tiền tố:
1. **Kiểm tra HUI**: Nếu $\sum_{e \in elements} e.iutil \ge \text{minUtil}$, kết luận $X$ là một HUI.
2. **Cắt tỉa nhánh con (Pruning Strategy)**:
   Nếu tổng lợi nhuận thực tế cộng với lợi nhuận tiềm năng còn lại nhỏ hơn ngưỡng:
   $$\sum_{e \in elements} (e.iutil + e.rutil) < \text{minUtil}$$
   thì toàn bộ các tập mở rộng của $X$ chắc chắn không thể là HUI $\rightarrow$ **Cắt tỉa toàn bộ nhánh DFS của $X$**.
3. **Phép kết nối Utility-List Join**:
   Để tạo Utility-List cho tập $Pxy$ từ hai tập con $Px$ và $Py$, thuật toán duyệt đồng thời hai danh sách phần tử và tìm các giao dịch chung ($tid$).

---

## 4. Phân tích Nguyên lý Hoạt động của Thuật toán EFIM

### 4.1. Ý tưởng đột phá
EFIM (*Efficient High-Utility Itemset Mining*, Zida et al., 2017) được thiết kế nhằm khắc phục nhược điểm tiêu tốn RAM và chi phí phép Join lớn của HUI-Miner. EFIM không sử dụng danh sách liên kết con trỏ phức tạp mà hoạt động trực tiếp trên **mảng bộ nhớ phẳng (array-based)** và cơ chế chiếu cơ sở dữ liệu nhanh (*Fast Dataset Projection*).

### 4.2. Bốn kỹ thuật cốt lõi của EFIM

#### Kỹ thuật 1: Mảng tiện ích tuyến tính (Utility Bins - $O(|I|)$)
EFIM không lưu trữ cấu trúc đối tượng cho từng ứng viên mà chỉ dùng các mảng 1 chiều có kích thước bằng số lượng mặt hàng ($|I|$):
- `utilityBinArraySU`: Lưu trữ Subtree Utility.
- `utilityBinArrayLU`: Lưu trữ Local Utility.
Quá trình tính toán chỉ là phép cộng dồn giá trị vào ô chỉ số của mảng trong một lần quét tuyến tính, đạt độ phức tạp không gian tối ưu $O(|I|)$.

#### Kỹ thuật 2: Hai chặn trên chặt hơn (Sub-tree Utility & Local Utility)
Thay vì chỉ dùng một chặn trên lỏng lẻo như TWU hay $rutil$, EFIM tính toán 2 chặn trên cực kỳ chặt chẽ trong mỗi không gian chiếu:
1. **Sub-tree Utility ($SU$)**: Chặn trên cho tất cả các tập con mở rộng của $P \cup \{e\}$ trong nhánh DFS hiện tại. Nếu $SU(e) < \text{minUtil}$, không cần đệ quy xuống nhánh con của $e$.
2. **Local Utility ($LU$)**: Chặn trên cục bộ cho việc mở rộng $P$ với bất kỳ mặt hàng nào khác trong cùng mức. Giúp loại bỏ các mặt hàng không tiềm năng khỏi không gian chiếu ngay lập tức.

#### Kỹ thuật 3: Nén gộp giao dịch (Transaction Merging)
Trong quá trình chiếu cơ sở dữ liệu con, nhiều giao dịch sau khi loại bỏ các mặt hàng không tiềm năng sẽ trở nên **hoàn toàn giống hệt nhau về danh sách mặt hàng**.  
EFIM sắp xếp cơ sở dữ liệu theo thứ tự từ điển đảo ngược và **gộp các giao dịch trùng nhau thành một giao dịch duy nhất** với giá trị lợi nhuận cộng dồn:
$$T_{new} = T_a + T_b$$
Kỹ thuật này giúp cơ sở dữ liệu co cụm lại cực nhanh ở các tầng đệ quy sâu, giảm số lần quét từ hàng chục nghìn xuống chỉ còn vài trăm giao dịch.

#### Kỹ thuật 4: Chiếu cơ sở dữ liệu trực tiếp trong bộ nhớ (Fast Dataset Projection)
EFIM không tạo bản sao của giao dịch mà chỉ dịch chuyển con trỏ vị trí `offset`:
$$\text{offset}_{new} = \text{position}(e) + 1$$
Dữ liệu được chiếu tại chỗ mà không cần cấp phát thêm bộ nhớ Heap, triệt tiêu gần như hoàn toàn áp lực dọn rác (GC) của JVM.

---

## 5. Bảng So sánh Tổng quan Lý thuyết: HUI-Miner vs EFIM

| Khía cạnh | HUI-Miner (Liu & Qu, 2012) | EFIM (Zida et al., 2017) |
| :--- | :--- | :--- |
| **Mô hình duyệt** | Depth-First Search trên cây tiền tố | Depth-First Search kết hợp Database Projection |
| **Cấu trúc dữ liệu** | Utility-List (Danh sách liên kết đối tượng) | Array-based (Utility Bins kích thước $O(\|I\|)$) |
| **Kỹ thuật nén DB** | Không có (quét toàn bộ tid qua phép Join) | **Transaction Merging** (gộp giao dịch đồng dạng) |
| **Chiến lược cắt tỉa** | $TWU$ và $iutil + rutil$ | Hai chặn trên chặt: **Sub-tree Utility** & **Local Utility** |
| **Độ phức tạp bộ nhớ** | $O(2^{\|I\|} \cdot \|D\|)$ trong trường hợp xấu | $O(\|D\| + \|I\|)$ bộ nhớ phẳng ổn định |
| **Thao tác cốt lõi** | Phép giao danh sách (Utility-List Join) | Quét mảng số nguyên tuyến tính |
| **Phù hợp hệ thống Web** | Kém hơn (dễ tràn RAM khi minUtil thấp) | **Rất phù hợp (nhẹ, nhanh, ổn định)** |
