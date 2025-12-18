import json
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    alpha: float = 0.75
    scale: float = 1.0
    show_fps: bool = True

def load_settings(path: Path) -> Settings:
    data = json.loads(path.read_text(encoding="utf-8"))
    return Settings(
        alpha=float(data.get("alpha", 0.75)),
        scale=float(data.get("scale", 1.0)),
        show_fps=bool(data.get("show_fps", True)),
    )

def save_settings(path: Path, s: Settings) -> None:
    path.write_text(json.dumps({"alpha": s.alpha, "scale": s.scale, "show_fps": s.show_fps}, indent=2), encoding="utf-8")
