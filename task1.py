import asyncio
import os
import time
import aiohttp

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.google.com/search?q={}'
name_arr = ['Yash', 'KOSS', 'Your Name']
results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for name in name_arr:
        tasks.append(asyncio.create_task(session.get(
            url.format(name), ssl=False)))
    return tasks


async def get_names():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # you could also do
        # tasks = [session.get(URL.format(symbol, API_KEY), ssl=False) for symbol in symbols]
        responses = await asyncio.gather(*tasks)
        # for response in responses:
        #     results.append(await response.json())

asyncio.run(get_names())

end = time.time()
total_time = end - start
print("It took {} seconds".format(total_time))
print('You did it!')
