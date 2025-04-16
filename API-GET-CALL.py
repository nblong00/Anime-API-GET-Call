import requests
import json

url = 'https://api.jikan.moe/v4/top/anime'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

response = requests.get(url, headers=header)
print(response)

responseData = response.json()

# This can be used to overwrite file that is currently open
#f = open('file.txt', 'r+')
#f.truncate(0) # need '0' when using r+

try:
    with open('temp.json', 'w') as file:
        json.dump(responseData, file, indent=4)  # Formats JSON with indentions
    print("Data written to temp.json successfully.")
    input("Operation complete. Please key to close...")
except IOError as e:
    print(f"Error writing to file: {e}")
    input("Operation failed. Please key to close...")

