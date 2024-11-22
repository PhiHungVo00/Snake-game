Snake Game - README

Giới thiệu

SnakeGame là một phiên bản hiện đại của trò chơi Rắn săn mồi truyền thống, đã gắn liền với tuổi thơ của nhiều người trên khắp thế giới. Với sự phát triển của các nền tảng kỹ thuật số, các trò chơi như Snake Xenzia đã lấy lại được sự yêu thích, và dự án của chúng tôi nhằm tái hiện lại trải nghiệm cổ điển này với đồ họa và lối chơi được nâng cao.

Mục tiêu của chúng tôi là tái hiện lại lối chơi hoài niệm của trò chơi Rắn săn mồi cổ điển, đồng thời bổ sung thêm đồ họa màu sắc và trải nghiệm sống động hơn so với phiên bản đen trắng trên các điện thoại di động cũ. Nhiệm vụ của người chơi là điều khiển rắn để ăn thật nhiều trái cây đồng thời tránh va chạm. SnakeGame cũng có hai chế độ chơi khác nhau để người chơi trải nghiệm.

Đặc điểm

Điều khiển đơn giản: Sử dụng các phím mũi tên hoặc W-A-S-D để điều khiển con rắn.

Tăng Điểm Số: Mỗi lần rắn ăn mồi, điểm số của người chơi sẽ tăng.

Thử Thách Tăng Dần: Trò chơi trở nên khó khăn hơn khi rắn dài ra.

Chơi Lại Không Giới Hạn: Người chơi có thể chơi lại nhiều lần để cải thiện điểm số cá nhân.

Hướng dẫn chơi

SnakeGame là một game nhẹ, lấy cảm hứng từ trò chơi Rắn săn mồi cổ điển, có thể tải về và chơi một cách nhanh chóng. Thực hiện theo các bước sau để cài đặt và chơi:

Cài đặt

Tải mã nguồn từ kho GitHub: Snake Game GitHub.

Giải nén và chạy tệp thực thi Snake_Game.exe để bắt đầu chơi.

Giao diện game

Khi mở chương trình, cửa sổ trò chơi sẽ hiển thị các mục sau:

Play New Game: Bắt đầu trò chơi mới.

HighScore: Xem bảng xếp hạng điểm số cao nhất của 5 người chơi.

Quit: Thoát khỏi trò chơi.

Setting: Mở menu mới để cài đặt trò chơi theo ý thích, bao gồm độ khó, chế độ chơi, và màu sắc của rắn.

Người chơi có thể sử dụng các phím số tương ứng để chọn từng mục. Menu cài đặt cho phép tùy chỉnh:

Chọn Cấp Độ (Choose Level): Đặt độ khó của trò chơi thành Dễ, Bình thường hoặc Khó.

Chọn Chế Độ (Choose Mode): Chọn giữa hai chế độ – Cổ điển và Hiện đại.

Chọn Màu (Choose Color): Chọn màu sắc cho rắn là Xanh lá, Tím hoặc Vàng.

Điều khiển

Sử dụng phím mũi tên hoặc các phím W, A, S, D để điều khiển hướng của rắn:

W: Di chuyển lên

S: Di chuyển xuống

A: Di chuyển sang trái

D: Di chuyển sang phải

Rắn chỉ có thể đổi hướng giữa phương ngang và phương dọc.

Nhấn Space để tạm dừng hoặc ESC để kết thúc trò chơi ngay lập tức.

Chế độ chơi

Chế độ Cổ điển (Classic Mode): Người chơi điều khiển rắn để ăn "mồi" và dài ra sau mỗi lần ăn thành công. Nếu rắn đi ra khỏi rìa màn hình, nó sẽ xuất hiện lại từ phía đối diện. Trò chơi kết thúc khi rắn va vào chính mình.

Chế độ Hiện đại (Modern Mode): Tương tự như chế độ cổ điển, nhưng trò chơi sẽ kết thúc nếu rắn chạm vào mép màn hình thay vì xuất hiện lại ở phía đối diện.

Chi tiết kỹ thuật

Dưới đây là một số thành phần kỹ thuật được sử dụng để phát triển Snake Game:

Công cụ và nền tảng

Ngôn ngữ lập trình: Trò chơi được phát triển bằng Python.

Thư viện đồ họa và âm thanh: Chúng tôi sử dụng thư viện Pygame để tích hợp đồ họa và âm thanh.

Môi trường phát triển: Visual Studio Code và PyCharm được sử dụng làm môi trường phát triển chính.

Cấu trúc Game

Biểu diễn Rắn: Rắn được biểu diễn dưới dạng một danh sách các điểm (x, y) biểu thị tọa độ của mỗi đoạn.

Biểu diễn Thức ăn: Thức ăn được biểu diễn dưới dạng một điểm (x, y) xuất hiện ngẫu nhiên trên màn hình.

Logic Game: Các hành động trong game như di chuyển, phát hiện va chạm và ăn mồi được xử lý thông qua các hàm điều khiển quy tắc và hành vi của trò chơi.

Hiển thị đối tượng

Trò chơi có các hàm khác nhau để vẽ các đối tượng trên màn hình:

draw_snake(): Vẽ con rắn trên màn hình, sử dụng hình chữ nhật cho mỗi đoạn.

draw_food(): Vẽ thức ăn dưới dạng hình tròn hoặc hình vuông trên màn hình.

draw_menu(): Hiển thị menu trò chơi.

draw_scoreboard(): Hiển thị điểm số hiện tại.

Quá trình phát triển

Nhóm chúng tôi đã tiếp cận dự án này theo từng giai đoạn để đảm bảo sự phối hợp và chất lượng. Dưới đây là các mốc chính trong quá trình thực hiện dự án:

Khởi động Dự án (03/11/2024): Xác lập mục tiêu và chọn công cụ, nền tảng (Python và Pygame).

Thiết kế cấu trúc Game (10/11/2024): Định nghĩa cấu trúc game, xây dựng khung mã ban đầu, và bắt đầu triển khai các hàm cốt lõi.

Triển khai Logic Game Cốt lõi (13/11/2024): Phát triển các chức năng di chuyển của rắn, phát hiện va chạm, tạo thức ăn và tích hợp logic với giao diện người dùng.

Kiểm thử và Gỡ lỗi (15/11/2024): Chạy thử nghiệm, xác định lỗi và tối ưu hóa hiệu suất của trò chơi.

Hoàn thành Dự án (20/11/2024): Hoàn tất việc thử nghiệm và hoàn thiện các tính năng của trò chơi.

Thành viên nhóm

Dự án này được thực hiện bởi nhóm sinh viên từ Trường Đại học Công nghệ Thông tin tại Thành phố Hồ Chí Minh:

Võ Phi Hùng (23520582)

Nguyễn Nhựt Thành (23521451)

Nguyễn Quốc Cường (23520205)

Nguyễn Tuấn Kiệt (21522259)

Chúng tôi hy vọng rằng dự án này mang lại niềm vui và hoài niệm cho những ai chơi nó, và chúng tôi cảm ơn sự hỗ trợ và hướng dẫn từ thầy Nguyễn Văn Toàn.

Chúc bạn chơi game vui vẻ và có những giây phút hoài niệm đáng nhớ!
