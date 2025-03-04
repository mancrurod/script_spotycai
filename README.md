![Header Image](banner.png)

# Spotycai Song Downloader

This project is an automated tool to download album songs from the Spotycai website. It uses Selenium to navigate the website, extract the URLs of the songs in MP3 format, and download them to a specific folder.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- Requests

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Modify the `main.py` file and replace the value of `album_url` with the URL of the Spotycai album you want to download.
    ```python
    if __name__ == "__main__":
        album_url = "https://www.torrenet.xyz/spotycai/album/738/Antonio+Álvarez+Cordero+(Bizcocho)/Los+hermanos+del+buen+fin"
        download_all_songs(album_url)
    ```

2. Run the `main.py` script:
    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: Main script that starts the download process.
- `src/driver_setup.py`: Selenium WebDriver setup.
- `src/album_scraper.py`: Functions to extract song elements from the album page.
- `src/song_downloader.py`: Functions to get the MP3 URL and download the file.
- `src/utils.py`: Utility functions, such as filename sanitization and folder creation.
- `src/__init__.py`: Initialization file for the src module.

## Project Schema

```
script_spotycai/
├── main.py
├── requirements.txt
├── environment.yml
├── LICENSE
├── README.md
├── src/
│   ├── __init__.py
│   ├── driver_setup.py
│   ├── album_scraper.py
│   ├── song_downloader.py
│   ├── utils.py
└── album_downloaded/
```

## Notes

- Make sure you have Google Chrome installed on your system, as the script uses the Chrome WebDriver.
- The script is configured to run in headless mode (without a graphical interface). If you want to see the browser while the script is running, you can comment out the line `options.add_argument("--headless")` in `src/driver_setup.py`.

## Album Download Location

The downloaded album will be saved in a folder named `album_downloaded` within the project directory. Each album will have its own subfolder named after the album title.

## Contributions

Contributions are welcome. If you find any issues or have any improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
