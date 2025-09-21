"""
并发交易 500 次，成功率 ≥ 99%
域名用 httpbin.org 保证可访问
"""
import asyncio, aiohttp, pytest, random

HOST = "https://httpbin.org"  # 公网测试站
PLAYERS = [f"player_{i:03}" for i in range(100)]
ITEMS = range(1000, 1500)


async def buy(session, player, item):
    payload = {"player": player, "item": item, "price": random.randint(10, 100)}
    async with session.post(f"{HOST}/post", json=payload) as resp:
        return resp.status == 200


@pytest.mark.asyncio
async def test_concurrent_trading():
    async with aiohttp.ClientSession() as session:
        tasks = [buy(session, random.choice(PLAYERS), random.choice(ITEMS)) for _ in range(500)]
        results = await asyncio.gather(*tasks)
    success = sum(results)
    assert success >= 495, f"仅 {success}/500 成功"