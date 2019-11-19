Search: https://www.youtube.com/watch?v=LkzlUpQkV-M&feature=youtu.be<br/>
Multiagent: https://www.youtube.com/watch?v=XcbaZKIoU_k&feature=youtu.be<br/>
Q1: evaluation = getScore() + khoảng cách pacman tới enemy gần nhất chia cho khoảng cách tới thức ăn gần nhất cộng thêm 1 hằng số nếu action là Stop, eval lớn khi xa enemy & gần food, hạn chế việc đứng yên<br/>
Q2 &Q3 &Q4: tương tự mã giả trong slide<br/>
Q5: evaluation = getScore() + tổ hợp tuyến tính khoảng cách với enemy gần nhất, hàm heuristic với food (tương tự bài Search) và số food còn lại. <br/>
Classification: https://www.youtube.com/watch?v=jJYX3QQarjc&feature=youtu.be <br/>
Q4: đặc trưng là số thành phần liên thông của hình. Duyệt toàn bộ pixel, đánh dấu đã duyệt hay chưa, nếu gặp 1 pixel chưa duyệt thì loang và cộng thêm 1<br/>
Q5: tương tự Q1<br/>
Q6: các đặc trưng thêm vào là: bước di chuyển có phải STOP hay không, nghịch đảo khoảng cách đến thức ăn hoặc viên thuốc gần nhất, khoảng cách đến ma gần nhất<br/>
