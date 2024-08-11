# Pokémon Card Image Downloader

This script downloads images of Pokémon cards from the Pokémon TCG API and stores them in a local directory called `cards`.

## Prerequisites

- Python 3.x is required to run the script.
- You need an active internet connection to download the images.

## Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/SoaresPT/PokemonTCG-Downloader.git
    cd PokemonTCG-Downloader
    ```

2. **Ensure Python is Installed**

    Make sure you have Python 3 installed on your system. You can verify the installation by running:

    ```bash
    python --version
    ```

    or

    ```bash
    python3 --version
    ```

    If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/).

3. **Prepare the Script**

    Navigate to the directory where the script resides.

4. **Run the Script**

    You can run the script using the following command:

    ```bash
    python download_pokemon_images.py
    ```

    or

    ```bash
    python3 download_pokemon_images.py
    ```

## What the Script Does

- The script fetches pages of Pokémon card data from the Pokémon TCG API, starting at page 1.
- For each card, it downloads the high-resolution image and saves it to a local directory named `cards`.
- If the `cards` directory does not exist, the script will create it.
- The script continues to fetch and download images until there are no more cards available on the API.

## Additional Information

- The script uses the Pokémon TCG API: [https://api.pokemontcg.io/](https://api.pokemontcg.io/)
- The images are saved in the `cards` directory with the filename format: `<card_id>-<card_name>.png`.

---

Enjoy downloading your Pokémon card images!
