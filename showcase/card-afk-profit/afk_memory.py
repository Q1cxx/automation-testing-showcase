"""
 8h 长驻挂机内存采样
 pip install psutil matplotlib pytest
"""
import psutil, time, matplotlib.pyplot as plt, pytest

PROC_NAME = "GoddessPlanet.exe"      # 进程名
SAMPLE_INTERVAL = 30                 # 30s 采一次
MAX_MEM_GB = 1.6


def test_afk_memory():
    pid = next(p.pid for p in psutil.process_iter(['pid', 'name'])
               if p.info['name'] == PROC_NAME)
    mem = []
    for _ in range(int(8*3600/SAMPLE_INTERVAL)):
        mem.append(psutil.Process(pid).memory_info().rss / 1024**3)
        time.sleep(SAMPLE_INTERVAL)
    plt.plot(mem); plt.savefig("mem.png")
    assert max(mem) < MAX_MEM_GB, f"峰值内存{max(mem):.2f}GB 超限"