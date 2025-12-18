import time
from dataclasses import dataclass

import cv2
import numpy as np

@dataclass
class HudState:
    last_t: float = time.perf_counter()
    fps: float = 0.0

def update_fps(state: HudState) -> None:
    now = time.perf_counter()
    dt = max(1e-6, now - state.last_t)
    state.fps = 1.0 / dt
    state.last_t = now

def draw_hud(frame: np.ndarray, *, alpha: float = 0.75, text: str = "HUD", fps: float | None = None) -> np.ndarray:
    h, w = frame.shape[:2]
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 48), (0, 0, 0), thickness=-1)
    blended = cv2.addWeighted(overlay, float(alpha), frame, 1.0 - float(alpha), 0)
    cv2.putText(blended, text, (12, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    if fps is not None:
        cv2.putText(blended, f"FPS: {fps:.1f}", (w - 160, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return blended
