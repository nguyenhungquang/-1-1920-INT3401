Search: https://www.youtube.com/watch?v=LkzlUpQkV-M&feature=youtu.be
Multiagent: Q1: evaluation = getScore() + khoảng cách pacman tới enemy gần nhất chia cho khoảng cách tới thức ăn gàn nhất cộng thêm 1 hằng số nếu action là Stop, eval lớn khi xa enemy & gần food, hạn chế việc đứng yên
Q2 &Q3 &Q$: tương tự mã giả trong slide
Q5: evaluation = getScore() + tổ hợp tuyến tính khoảng cách với enemy gần nhất, hàm heuristic với food (tương tự bài Search) và số food còn lại. 
