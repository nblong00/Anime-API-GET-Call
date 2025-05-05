import requests
import pandas
import time

url = 'https://api.jikan.moe/v4/top/anime'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

# API call occurs & response code is printed
response = requests.get(url, headers=header)
print()
print('Top Anime GET v1.0')
print()
time.sleep(1)

# Check if API call was successful
if response.status_code != 200:
    print(f"Error: API request failed with status code {response.status_code}")
    input("Press ENTER to close...")
    exit()

# Call results are stored in variable & json is normalized and cut down to data block
responseData = response.json()
cleanedUpJSON = pandas.json_normalize(responseData, 'data')

# Target columns to extract from JSON
desiredColumns = ['mal_id', 'title_english']  
selectedColumns = cleanedUpJSON[desiredColumns]
print(selectedColumns)

# Error checking for user input
try:
# Ask user what top anime they'd like to read more about (ID)
    print()
    mal_id_variable = input("Enter anime ID you want to query: ")
    print()

    # Check if input is empty
    if not mal_id_variable:
        raise ValueError("No input provided.")
    
    # Confirm if input is positive, else the program should exit
    elif int(mal_id_variable) <= 0:
        raise ValueError("Anime ID must be a positive integer.")

    # Check if mal_id exists in the JSON data
    elif int(mal_id_variable) not in cleanedUpJSON['mal_id'].values:
        raise ValueError(f"Anime ID '{mal_id_variable}' not found in the top anime list.")

    # Switch user input to integer after error checking
    else:
        mal_id_variable = int(mal_id_variable)

except ValueError as e:
    print(f"Error: {e}")
    input("Operation failed. Press ENTER to close...")
    exit()

# Pull the specific mal_id entry using user input
filteredMainID = cleanedUpJSON[cleanedUpJSON['mal_id'] == mal_id_variable]

# Target columns to extract from mal_id entered by user (reuse desired_columns & selected columns)
desiredColumns = ['mal_id', 'url', 'title_english']  
selectedColumns = filteredMainID[desiredColumns]
print(selectedColumns)

# Wait for user input to close window 
print()
input("Operation complete. Please ENTER to close...")

# Leaving in to let me get copy of the fields returned
# cleanedUpJSON.to_csv('E:\\AWS_DEV\\PythonScripts\\API-GET-CALL\\temp.csv')