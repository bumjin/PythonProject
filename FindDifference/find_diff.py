import cv2
import os
import time
from time import sleep
import pyautogui
from PIL import ImageChops

# 왼쪽(원본) 이미지
# 시작 좌표 (0,25)

# 오른쪽(원본) 이미지
# 시작 좌표 (964,25)

# 이미지 크기
# width 956
# height 765

width, height = 956, 765
y_pos = 45

src = pyautogui.screenshot(region=(0, y_pos, width, height))
src.save('src.jpg')
dest = pyautogui.screenshot(region=(963, y_pos, width, height))
dest.save('dest.jpg')

diff = ImageChops.difference(src, dest)
diff.save('diff.jpg')

while not os.path.exists('diff.jpg'):
    time.sleep(1)

src_img = cv2.imread('src.jpg')
dest_img = cv2.imread('dest.jpg')
diff_img = cv2.imread('diff.jpg')

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
gray = (gray > 25) * gray

contours, _ = cv2.findContours(
    gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)  # BGR 녹색
for cnt in contours:
    if cv2.contourArea(cnt) < 100:
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    print(x, y, w, h)
    cv2.rectangle(src_img, (x, y), (x + w, y + h), COLOR, 2)
    cv2.rectangle(dest_img, (x, y), (x + w, y + h), COLOR, 2)
    cv2.rectangle(diff_img, (x, y), (x + w, y + h), COLOR, 2)

    to_x = x + (w // 2)
    to_y = y + (h // 2) + y_pos

    pyautogui.moveTo(to_x, to_y, duration=1)
    time.sleep(0.3)
    pyautogui.click()

# cv2.imshow('src', src_img)
# cv2.imshow('dest', dest_img)
# cv2.imshow('diff', diff_img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()
