"""
一键跑全部脚本 + 聚合报告
"""
import subprocess, pathlib, shutil

pathlib.Path("showcase/reports").mkdir(exist_ok=True)

jobs = [
    ("mmorpg-trading", "python -m pytest test_trading.py --html=report.html"),
    ("fps-gun-balance", "python -m pytest gun_matrix.py --html=report.html"),
    ("card-afk-profit", "python -m pytest afk_memory.py --html=report.html"),
]

for folder, cmd in jobs:
    subprocess.run(cmd, shell=True, cwd=f"showcase/{folder}")
    shutil.move(f"showcase/{folder}/report.html", f"showcase/reports/{folder}.html")

print("✅ 全部完成，报告在 showcase/reports/")