## Báo Cáo: Tìm Hiểu Về Crawler Data
## 1.Giới Thiệu
## 1.1 Khái Niệm Crawler Data
Crawler data, còn được gọi là web scraping, là quá trình tự
động thu thập dữ liệu từ các trang web. Thay vì thu thập dữ liệu bằng cách thủ công, chương trình crawler sẽ duyệt qua các trang web, lấy dữ liệu và lưu lại vào các định dạng như CSV, Excel, JSON, hoặc cơ sở dữ liệu như MySQL, PostgreSQL.
## 1.2 Ứng Dụng của Crawler Data
Crawler data có nhiều ứng dụng trong thực tế:
**• Phân tích dữ liệu**: Thu thập dữ liệu để phân tích xu hướng hoặc đưa ra dự đoán.
**•	Tìm kiếm thông tin**: Tự động thu thập thông tin từ nhiều trang web để so sánh và tổng hợp.
**•	Tạo cơ sở dữ liệu**: Xây dựng cơ sở dữ liệu từ nội dung trên các trang web, ví dụ như danh sách sản phẩm, giá cả, tin tức,...
## 2. Nguyên Lý Hoạt Động Crawler Data
## 2.1 Cơ Chế Hoạt Động
Chương trình crawler hoạt động theo các bước sau:
1.	**Gửi yêu cầu HTTP**: Gửi yêu cầu HTTP đến URL của trang web cần thu thập dữ liệu.
2.	**Phân tích HTML**: Sau khi nhận phản hồi từ máy chủ, chương trình sẽ phân tích cấu trúc HTML để tìm kiếm các phần tử chứa thông tin cần thiết.
3.	**Trích xuất dữ liệu**: Lấy thông tin từ các phần tử HTML như tiêu đề, liên kết, nội dung văn bản.
4.	**Lưu trữ dữ liệu**: Dữ liệu sau khi trích xuất được lưu vào file hoặc cơ sở dữ liệu.
## 2.2 Thư Viện Sử Dụng
Trong Python, hai thư viện phổ biến để xây dựng một chương trình crawler là:
•	**Requests**: Thư viện để gửi yêu cầu HTTP.
•	**BeautifulSoup**: Thư viện giúp phân tích cú pháp và trích xuất dữ liệu từ HTML.
