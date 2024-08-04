import requests
import os

# Define the flags you want to download with flagpedia URL
flags = {
    'Chinese Taipei': 'tw',
    'Hong Kong': 'hk',
    'Great Britain': 'gb',
    'North Korea': 'kp',
    'Kosovo': 'xk',
    'Czech Republic': 'cz',
    'Individual Neutral Athletes': 'np'  # Neutral Athlete flag
}

# Base URL for the SVG flags
base_url = 'https://flagpedia.net/data/flags/'

# Directory to save the flags
output_dir = 'flags'
os.makedirs(output_dir, exist_ok=True)

for country, code in flags.items():
    url = f"{base_url}{code}.svg"  # Using SVG format
    response = requests.get(url)
    
    if response.status_code == 200:
        # Convert country name to a safe filename
        safe_file_name = country.lower().replace(' ', '_') + '.svg'
        with open(os.path.join(output_dir, safe_file_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {country} flag successfully.")
    else:
        print(f"Failed to download {country} flag. Status code: {response.status_code}")

print("All downloads completed.")
