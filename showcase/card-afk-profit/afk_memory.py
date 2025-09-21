#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8 小时挂机内存泄漏监控
----------------------------
1. 每 30 秒采样一次内存
2. 绘制内存趋势图
3. 断言峰值 < 1.6 GB
"""
import psutil                       # 读取进程内存
import time
import matplotlib.pyplot as plt     # 绘图
import pytest

# === 配置 ===
PROC_NAME = "GoddessPlanet.exe"   # 被测游戏进程名
MAX_MEM_GB = 1.6                  # 内存上限
SAMPLE_INTERVAL = 30              # 采样间隔（秒）
MAX_SAMPLES = int(8 * 3600 / SAMPLE_INTERVAL)  # 8 小时总次数

# === 测试用例 ===
def test_afk_memory():
    """长驻挂机内存泄漏验证"""
    # 找到进程 PID
    pid = next(p.pid for p in psutil.process_iter(["pid", "name"])
               if p.info["name"] == PROC_NAME)
    proc = psutil.Process(pid)
    mem = []                        # 存放内存序列

    print("开始 8h 采样，每 30s 一次...")
    for i in range(MAX_SAMPLES):
        rss = proc.memory_info().rss / 1024 ** 3  # 转 GB
        mem.append(rss)
        print(f"\r{i+1}/{MAX_SAMPLES}  {rss:.2f} GB", end="")
        time.sleep(SAMPLE_INTERVAL)

    # 画图保存
    plt.plot(mem)
    plt.title("8h 内存趋势")
    plt.xlabel("采样点")
    plt.ylabel("内存 (GB)")
    plt.savefig("mem.png")
    print("\n已生成 mem.png")

    # 断言峰值
    assert max(mem) < MAX_MEM_GB, f"峰值内存{max(mem):.2f}GB 超过阈值"