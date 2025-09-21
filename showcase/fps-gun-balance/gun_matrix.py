"""
 pairwise 生成 124 枪 × 200 配件 最小组合
 pip install pytest allpairspy
"""
from allpairspy import AllPairs

guns = [f"g{i}" for i in range(1, 125)]          # 124 枪
parts = [f"p{i}" for i in range(1, 201)]         # 200 配件

def test_gun_balance():
    for pairs in AllPairs([guns, parts]):
        gun, part = pairs
        # 模拟 DPS 计算
        dps = hash(gun + part) % 80 + 20
        assert 30 <= dps <= 70, f"{gun}+{part} DPS={dps} 超出平衡区间"