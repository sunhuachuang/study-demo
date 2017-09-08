import asyncio
import asyncpg


async def run():
    conn = await asyncpg.connect(user='sun', password='',
                                 database='btc', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM cnbtc''')
    print(values)
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
