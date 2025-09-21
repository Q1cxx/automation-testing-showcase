#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MMORPG 交易所高并发购买脚本
--------------------------------
1. 模拟 100 个玩家同时在线
2. 并发 500 次购买请求
3. 断言成功率 ≥ 99%
4. 生成 HTML 报告供面试展示
"""
import asyncio          # 异步 IO，实现高并发
import aiohttp        # 异步 HTTP 客户端
import pytest         # 测试框架
import random         # 随机挑选玩家/道具/价格

# === 测试配置 ===
# 使用 httpbin.org 公网测试站，面试时替换为你们测试服
HOST = "https://httpbin.org"
ITEMS = range(1000, 1500)                 # 商品池 500 件
PLAYERS = [f"player_{i:03}" for i in range(100)]  # 100 个账号

# === 异步购买函数 ===
async def buy(session: aiohttp.ClientSession, player: str, item: int) -> bool:
    """单次购买请求，返回 True=成功 False=失败"""
    payload = {
        "player": player,
        "item": item,
        "price": random.randint(10, 100)   # 随机出价
    }
    try:
        async with session.post(f"{HOST}/post", json=payload) as resp:
            return resp.status == 200      # 简单判断 HTTP 200
    except Exception as e:
        print(f"[WARN] {player} 购买失败: {e}")
        return False

# === 测试用例 ===
@pytest.mark.asyncio
async def test_concurrent_trading():
    """并发 500 次购买，成功率 ≥ 99%"""
    async with aiohttp.ClientSession() as session:
        # 生成 500 个协程任务
        tasks = [
            buy(session, random.choice(PLAYERS), random.choice(ITEMS))
            for _ in range(500)
        ]
        # 并发执行并等待全部完成
        results = await asyncio.gather(*tasks)

    success = sum(results)          # 成功次数
    print(f"成功 {success}/500")
    assert success >= 495, f"成功率仅 {success}/500，低于 99%"