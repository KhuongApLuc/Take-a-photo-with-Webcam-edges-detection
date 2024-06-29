#take a photo, enter "s" to save, enter "f" for edges detection

import cv2
import os
from datetime import datetime

def save_image(img, folder, filename=None):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if filename is None:
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    
    cv2.imwrite(os.path.join(folder, filename), img)
    print("Saved image as", filename)

def edge_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame)

        key = cv2.waitKey(1)
        
        if key == ord('s') or key == ord('S'):
            folder = input("Enter folder path to save the image: ")
            filename = input("Enter filename (leave blank to use timestamp): ")
            save_image(frame, folder, filename)
        
        elif key == ord('f') or key == ord('F'):
            folder = input("Enter folder path to save the edge-detected image: ")
            filename = input("Enter filename (leave blank to use timestamp): ")
            edge_img = edge_detection(frame)
            save_image(edge_img, folder, filename)
        
        elif key == 27:  # 27 is the ASCII value for the Escape key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import numpy as np 
def capture_image():
    # Mở webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Đọc khung hình từ webcam
        ret, frame = cap.read()

        # Hiển thị khung hình
        cv2.imshow('Press S to capture', frame)

        # Chờ phím được nhấn
        key = cv2.waitKey(1)
        
        # Nếu phím 's' được nhấn, chụp ảnh và lưu lại
        if key == ord('s'):
            cv2.imwrite('captured_image.jpg', frame)
            print("Image captured!")
            break

    # Đóng webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()


