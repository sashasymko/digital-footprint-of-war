from pathlib import Path

root = Path(__file__).parent

data = root / "data"
raw_data = data / "raw_data"
control_data = data / "control_data"
external_data = data / "external_data"
raw_kyiv = data / "raw_kyiv_time_data"
filtered_data = data / "filtered_data"
daily_data = data / "daily_data"