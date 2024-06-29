from Q1 import *
# Biến đổi hình ảnh(ví dụ chụp điện thoại ở góc nghiêng => thu được hình tứ giác, biến đổi để thu được hình chữ nhật)
# Biến global để lưu trữ các điểm được chọn
points = []

def mouse_click(event, x, y, flags, param):
    # Xác định sự kiện nhấp chuột
    if event == cv2.EVENT_LBUTTONDOWN:
        # Thêm tọa độ vào danh sách points
        points.append((x, y))
        # Vẽ điểm trên ảnh
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow('Image', image)

# Load ảnh
image = cv2.imread('captured_image.jpg')
# Sao chép ảnh để tránh thay đổi ảnh gốc
clone = image.copy()

# Tạo cửa sổ và kết nối với hàm xử lý sự kiện
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_click)

# Hiển thị ảnh và chờ sự kiện
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu toạ độ vào file txt
with open('coordinates.txt', 'w') as f:
    for point in points:
        f.write(f"{point[0]}, {point[1]}\n")
# Đọc tọa độ từ file txt
with open('coordinates.txt', 'r') as f:
    points = [tuple(map(int, line.strip().split(', '))) for line in f]

# Tính toạ độ của hình chữ nhật bao quanh 4 điểm
x_sorted = sorted(points, key=lambda x: x[0])
y_sorted = sorted(points, key=lambda x: x[1])

left = x_sorted[0][0]
right = x_sorted[-1][0]
top = y_sorted[0][1]
bottom = y_sorted[-1][1]

# Tạo ma trận biến đổi từ hình tứ giác thành hình chữ nhật
input_pts = np.float32(points)
output_pts = np.float32([[left, top], [right, top], [right, bottom], [left, bottom]])

# Tính ma trận biến đổi và biến đổi hình ảnh
transform_matrix = cv2.getPerspectiveTransform(input_pts, output_pts)
image = cv2.imread('captured_image.jpg')
warped_image = cv2.warpPerspective(image, transform_matrix, (image.shape[1], image.shape[0]))

# Hiển thị hình ảnh biến đổi
cv2.imshow('Warped Image', warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()