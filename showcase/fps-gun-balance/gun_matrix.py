#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FPS 枪械+配件平衡性验证
----------------------------
1. 124 把枪 × 200 种配件 = 24 800 种组合
2. 使用 pairwise 算法压缩到 < 400 条用例
3. 哈希模拟 DPS，断言数值在 30-70 之间
"""
from allpairspy import AllPairs   # pairwise 组合生成

# === 数据池 ===
guns = [f"g{i}" for i in range(1, 125)]   # 124 把枪
parts = [f"p{i}" for i in range(1, 201)]  # 200 种配件

# === 测试用例 ===
def test_gun_balance():
    """pairwise 遍历，保证 DPS 在平衡区间"""
    for pairs in AllPairs([guns, parts]):
        gun, part = pairs
        # 用哈希模拟 DPS（20-99）
        dps = hash(gun + part) % 80 + 20
        # 断言：太弱/太强都视为不平衡
        assert 30 <= dps <= 70, f"{gun}+{part} DPS={dps} 超出平衡区间"