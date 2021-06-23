import requests
import os
import urllib.parse
import time


# iterate over each url after converting the integer i to string and attaching it to the url. The JSON files downloaded contains dictionaries, so to store them, we have to convert them to a string after converting the dict keys to list.

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


start = time.time()
for i in range(1, 201):
    itos = str(i)
    main_api = 'https://xkcd.com/' + itos + '/info.0.json'

    json_data = requests.get(main_api).json()
    json_data1 = getList(json_data)
    json_data2 = listToString(json_data1)

    with open('sample.json', 'w') as f:
        f.write(json_data2)


end = time.time()
total_time = end - start
print("It took {} seconds in synchronous manner".format(total_time))
