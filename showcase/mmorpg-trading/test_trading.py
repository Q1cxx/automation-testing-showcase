"""
 concurrently trading 100 players, 500 items
 pip install pytest pytest-html aiohttp
"""
import asyncio, aiohttp, pytest, json, random

HOST = "https://demo.qa-server.io"          # 面试时换成你们测试服
ITEMS = range(1000, 1500)                  # 商品池
PLAYERS = [f"player_{i:03}" for i in range(100)]


async def buy(session, player, item):
    payload = {"player": player, "item": item, "price": random.randint(10, 100)}
    async with session.post(f"{HOST}/trading/buy", json=payload) as resp:
        return resp.status == 200


@pytest.mark.asyncio
async def test_concurrent_trading():
    async with aiohttp.ClientSession() as session:
        tasks = [buy(session, random.choice(PLAYERS), random.choice(ITEMS))
                 for _ in range(500)]
        results = await asyncio.gather(*tasks)
    success = sum(results)
    assert success >= 495, f"only {success}/500 success"