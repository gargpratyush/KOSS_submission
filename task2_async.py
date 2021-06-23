import aiohttp
import asyncio
import requests
import os
import urllib.parse
import time


start = time.time()


async def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


async def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


async def mainfunc():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 201):
            itos = str(i)
            main_api = 'https://xkcd.com/' + itos + '/info.0.json'

            json_data = await session.get(main_api).json()
            json_data1 = await getList(json_data)
            json_data2 = await listToString(json_data1)

            with open('new.json', 'w') as f:
                f.write(await json_data2)


asyncio.run(mainfunc())


end = time.time()
total_time = end - start
print("It took {} seconds in Asynchronous manner".format(total_time))
