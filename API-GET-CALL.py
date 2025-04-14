import requests
import pandas

url = 'https://api.jikan.moe/v4/top/anime'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

response = requests.get(url, headers=header)
print(response)

responseData = response.json()

open('temp.json', 'w').close()

# This can be used to overwrite file that is currently open
#f = open('file.txt', 'r+')
#f.truncate(0) # need '0' when using r+

data = pandas.json_normalize(responseData, 'data')
data.to_json("temp.json")

input("Operation complete. Please key to close...")
