import argparse
from pathlib import Path

import cv2

from src.hud import HudState, draw_hud, update_fps
from src.settings import Settings, load_settings, save_settings

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="0", help="Camera index (0) or path to a video file")
    ap.add_argument("--settings", default="settings.json", help="Path to settings.json")
    args = ap.parse_args()

    settings_path = Path(args.settings)
    s = load_settings(settings_path) if settings_path.exists() else Settings()

    src = args.source
    cap = cv2.VideoCapture(int(src)) if src.isdigit() else cv2.VideoCapture(src)
    if not cap.isOpened():
        print("Could not open video source. Try --source 0 or a valid file path.")
        return 1

    state = HudState()
    print("Controls: [q] quit | [+/-] alpha | [s] save settings")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        update_fps(state)
        hud = draw_hud(frame, alpha=s.alpha, text="vision-hud-controller", fps=state.fps if s.show_fps else None)
        cv2.imshow("HUD", hud)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if key == ord("+"):
            s.alpha = min(0.95, s.alpha + 0.05)
        if key == ord("-"):
            s.alpha = max(0.05, s.alpha - 0.05)
        if key == ord("s"):
            save_settings(settings_path, s)
            print(f"Saved settings: {settings_path}")

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
