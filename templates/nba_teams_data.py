import pandas as pd
import requests

# Define the headers
headers = {
    'Ocp-Apim-Subscription-Key: {key}'
}

# Fetch data from an API (example URL, replace with a real API endpoint)
try:
    response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Standings/{season}', headers=headers, timeout=10)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
else:
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Convert the data to a DataFrame
        df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
        print(df)
    else:
        print(f"Failed to fetch data: {response.status_code}")

