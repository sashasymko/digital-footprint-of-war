from pathlib import Path

root = Path(__file__).parent

folders = [
    root / "data" / "raw_data",
    root / "data" / "control_data",
    root / "data" / "external_data",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)
