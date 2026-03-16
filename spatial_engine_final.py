"""
Project: SGAE (Spatial Geometry Analysis Engine)
Author: Ken
Description: A geometric constraint solver for architectural and industrial layout.
"""

import numpy as np
import matplotlib.pyplot as plt

class SpatialGeometryEngine:
    """處理幾何座標轉換與邊界約束的核心引擎"""
    def __init__(self, degree):
        self.degree = degree % 360
        self.grid_limit = 3.0

    def calculate_entry_coords(self):
        """極座標轉直角座標：計算入口邊界位置"""
        rad = np.radians(self.degree - 90)
        vx, vy = np.cos(rad), np.sin(rad)
        scale = 1.5 / max(abs(vx), abs(vy))
        return 1.5 + vx * scale, 1.5 + vy * scale

    def check_constraints(self, x, y, w, l):
        """Design Rule Check (DRC): 確保物件不超出邊界"""
        safe_w = min(w, self.grid_limit)
        safe_l = min(l, self.grid_limit)
        safe_x = max(0, min(x, self.grid_limit - safe_w))
        safe_y = max(0, min(y, self.grid_limit - safe_l))
        return safe_x, safe_y, safe_w, safe_l

# 註：此為核心邏輯模組，UI 渲染層已進行解耦分離。