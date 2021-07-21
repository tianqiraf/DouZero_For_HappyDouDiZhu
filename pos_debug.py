# -*- coding: utf-8 -*-

# Created by: Raf

# 这个文件用来辅助调整截图区域坐标。运行游戏，全屏截图，放上路径，就可以查看截图区域。

import cv2

# Modify the region parameters and the image path
capture_pos = [(414, 804, 1041, 59),    # 玩家区域
               (530, 470, 380, 160),    # 玩家上家区域
               (1010, 470, 380, 160),   # 玩家下家区域
               (1320, 300, 110, 140),   # 地主标志区域(玩家上家)
               (320, 720, 110, 140),    # 地主标志区域(玩家)
               (500, 300, 110, 140),    # 地主标志区域(玩家下家)
               (817, 36, 287, 136)      # 地主底牌区域
               ]
img_path = 'C:/Users/Raf/Desktop/screenshot/1.png'


img = cv2.imread(img_path)
for pos in capture_pos:
    img = cv2.rectangle(img, pos[0:2], (pos[0] + pos[2], pos[1] + pos[3]), (0, 0, 255), 3)
cv2.namedWindow("test", 0)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
