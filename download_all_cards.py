import json
import os
import re
import requests
from pathlib import Path

# Define the target folder
target_folder = "cards"
print(f"Downloading images and putting them in {target_folder}...")

# Make sure the target folder exists
Path(target_folder).mkdir(parents=True, exist_ok=True)

# Start on page 1
next_page_number = 1

# Fetch pages until we tell it to break
while True:
    # Make a URL to download data
    next_page_url = f"https://api.pokemontcg.io/v1/cards?page={next_page_number}"
    # Download the blob of JSON
    print(f"Loading {next_page_url}")
    response = requests.get(next_page_url)
    next_page_data = response.text
    # Parse it into a Python dictionary
    next_page_dict = json.loads(next_page_data)
    # Get the cards from the dictionary
    cards = next_page_dict.get("cards", [])
    if not cards:
        # There weren't any cards on this page, so terminate the script
        print("No more cards, terminating")
        break
    else:
        # For each card, download the image and write it to a file
        for card in cards:
            # Create a target filepath based on the card ID & name
            raw_filepath = f"{target_folder}/{card['id']}-{card['name']}.png"
            # Filter out problem characters from the filename, only allow:
            # - lowercase & uppercase letters
            # - numbers
            # - special characters: \/-_.
            # Replace any other characters with `-`
            filepath = re.sub(r'[^a-zA-Z0-9\-_\/.]', '-', raw_filepath)
            if Path(filepath).exists():
                print(f" -> skip {filepath}")
                continue

            print(f" -> {filepath}")
            try:
                # Get the URL from this card's JSON.
                # If you want the low-res url,
                # remove "imageUrlHiRes" only on the line below and put "imageUrl" instead.
                image_url = card["imageUrlHiRes"]
                # Read the file from the URL
                image_data = requests.get(image_url).content
                # Write the image data to a local file
                with open(filepath, 'wb') as f:
                    f.write(image_data)
            except Exception as err:
                print(f"Encountered an error: {err}, continuing...")
                print(f"Image url: {image_url}")
                print(f"Card data: {card}")
        
        # Increment the page number so that we get the next page
        next_page_number += 1
