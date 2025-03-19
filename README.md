![Header Image](banner.png)

# 🎵 Spotycai Song Downloader

An automated tool to download album songs from the Spotycai website. This project uses Selenium to navigate the website, extract song URLs in MP3 format, and download them to a specific folder. Additionally, it embeds album covers into the downloaded MP3 files using `eyed3`.

---

## 🚀 Features

- Automates album song downloads from Spotycai.
- Embeds album covers into MP3 files.
- Organizes downloaded albums into structured folders.

---

## 🛠️ Requirements

Ensure you have the following installed:

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- Requests
- eyed3

---

## 📦 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/script_spotycai.git
    cd script_spotycai
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## 📖 Usage

1. Update the `album_url` in `main.py` with the URL of the Spotycai album you want to download:
    ```python
    if __name__ == "__main__":
        album_url = "https://www.torrenet.xyz/spotycai/album/738/Antonio+Álvarez+Cordero+(Bizcocho)/Los+hermanos+del+buen+fin"
        download_all_songs(album_url)
    ```

2. Run the script:
    ```bash
    python main.py
    ```

---

## 📂 Project Structure

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
│   ├── mp3_tagging.py
└── album_downloaded/
```

### Key Files

- **`main.py`**: Entry point for the script.
- **`src/driver_setup.py`**: Configures Selenium WebDriver.
- **`src/album_scraper.py`**: Extracts song details from the album page.
- **`src/song_downloader.py`**: Handles MP3 URL extraction and downloading.
- **`src/utils.py`**: Utility functions for file handling and folder creation.
- **`src/mp3_tagging.py`**: Embeds album covers into MP3 files.

---

## 📌 Notes

- **Browser Requirement**: Ensure Google Chrome is installed, as the script uses Chrome WebDriver.
- **Headless Mode**: The script runs in headless mode by default. To view the browser during execution, comment out the line:
    ```python
    options.add_argument("--headless")
    ```
    in `src/driver_setup.py`.

---

## 📁 Album Download Location

Downloaded albums are saved in the `album_downloaded` folder within the project directory. Each album is stored in its own subfolder named after the album title.

---

## 📝 To-Do

- Add release date to folder names when downloading MP3 files.

---

## 🤝 Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

🎉 **Happy Downloading!**
