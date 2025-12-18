import numpy as np
from src.hud import draw_hud

def test_draw_hud_returns_frame_same_shape() -> None:
    frame = np.zeros((240, 320, 3), dtype=np.uint8)
    out = draw_hud(frame, alpha=0.5, text="test", fps=30.0)
    assert out.shape == frame.shape
