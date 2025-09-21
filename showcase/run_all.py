#!/usr/bin/env python3
"""
一键跑全部脚本 + 聚合报告
"""
import subprocess, pathlib, shutil, sys

root = pathlib.Path(__file__).parent
reports = root / "reports"
reports.mkdir(exist_ok=True)

jobs = [
    ("mmorpg-trading", "pytest test_trading.py --html=report.html --self-contained-html"),
    ("fps-gun-balance", "pytest gun_matrix.py --html=report.html --self-contained-html"),
    ("card-afk-profit", "pytest afk_memory.py --html=report.html --self-contained-html"),
]

for folder, cmd in jobs:
    print(f"\n>>> 正在跑 {folder} ...")
    code = subprocess.run(cmd, shell=True, cwd=root / folder)
    if code.returncode == 0:
        shutil.move(root / folder / "report.html", reports / f"{folder}.html")
    else:
        print(f"{folder} 运行失败，请检查脚本", file=sys.stderr)

print("\n✅ 全部完成！报告在 showcase/reports/")