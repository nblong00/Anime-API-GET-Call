import requests
import pandas
import time

url = 'https://api.jikan.moe/v4/top/anime'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

def apiCallAndJsonCleanup():

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

    return cleanedUpJSON

def errorCheckingOnUserInput(normalizedJSON):
    try:
        print()
        mal_id_variable = input("Enter anime ID you want to query: ")
        print()

        if not mal_id_variable:
            raise ValueError("No input provided.")
        elif int(mal_id_variable) <= 0:
            raise ValueError("Anime ID must be a positive integer.")
        elif int(mal_id_variable) not in normalizedJSON['mal_id'].values:
            raise ValueError(f"Anime ID '{mal_id_variable}' not found in the top anime list.")
        else:
            mal_id_variable = int(mal_id_variable)
            return mal_id_variable
    except ValueError as e:
        print(f"Error: {e}")
        input("Operation failed. Press ENTER to close...")
        exit()


def apiReturnColumns(columns, normalizedJSON):
    desiredColumns = columns 
    selectedColumns = normalizedJSON[desiredColumns]
    return selectedColumns

def exitLogic():
    for i in range(3):
        anotherLoop = input("Do you want to run another GET call? (Enter Yes/No) ").title()

        if anotherLoop == "Yes":
            break

        elif i == 2 or anotherLoop == "No":
            return "exit"
        
        else:
            print("Invalid entry.")


def main():
    while True:
        normalizedJSON = apiCallAndJsonCleanup()

        print(apiReturnColumns(['mal_id', 'title_english'], normalizedJSON))

        mal_id_input_verified = errorCheckingOnUserInput(normalizedJSON)

        normalizedJSON = normalizedJSON[normalizedJSON['mal_id'] == mal_id_input_verified]

        print(apiReturnColumns(['mal_id', 'url', 'title_english'], normalizedJSON))

        time.sleep(.5)
        print()

        if exitLogic() == "exit":
            break

    print()
    input("Program exiting. Please ENTER to close...")

    # Leaving in to let me get copy of the fields returned
    # normalizedJSON.to_csv('E:\\AWS_DEV\\PythonScripts\\API-GET-CALL\\temp.csv')

main()