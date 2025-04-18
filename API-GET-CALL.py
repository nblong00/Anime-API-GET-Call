import requests
import pandas

url = 'https://api.jikan.moe/v4/top/anime'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

# API call occurs & response code is printed
response = requests.get(url, headers=header)
print()

# Check if API call was successful
if response.status_code != 200:
    print(f"Error: API request failed with status code {response.status_code}")
    input("Press ENTER to close...")
    exit()

# Call results are stored in variable & json is normalized and cut down to data block
responseData = response.json()
cleanedUpJSON = pandas.json_normalize(responseData, 'data')

# Target columns to extract from JSON
desired_columns = ['mal_id', 'title_english']  
selected_columns = cleanedUpJSON[desired_columns]
print(selected_columns)

# Ask user what top anime they'd like to read more about (ID)
print()
userInput = input("Enter anime ID you want to query:")
print()

# Error checking for user input
try:
    
    # Convert input to integer
    mal_id_variable = int(userInput)

    # Check if input is empty
    if not userInput:
        raise ValueError("No input provided.")
    # Confirm if input is positive, else the program should exit
    if mal_id_variable <= 0:
        raise ValueError("Anime ID must be a positive integer.")

    # Check if mal_id exists in the JSON data
    if mal_id_variable not in cleanedUpJSON['mal_id'].values:
        raise ValueError(f"Anime ID '{mal_id_variable}' not found in the top anime list.")

except ValueError as e:
    print(f"Error: {e}")
    input("Operation failed. Press ENTER to close...")
    exit()


# Pull the specific mal_id entry using user input
filteredMainID = cleanedUpJSON[cleanedUpJSON['mal_id'] == mal_id_variable]

# Target columns to extract from mal_id entered by user (reuse desired_columns & selected columns)
desired_columns = ['mal_id', 'url', 'title_english']  
selected_columns = filteredMainID[desired_columns]
print(selected_columns)

# Wait for user input to close window 
print()
input("Operation complete. Please ENTER to close...")

# Leaving in to let me get copy of the fields returned
# cleanedUpJSON.to_csv('E:\\AWS_DEV\\PythonScripts\\API-GET-CALL\\temp.csv')



