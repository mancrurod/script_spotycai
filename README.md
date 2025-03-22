# 🎵 Spotycai Song Downloader

## 🚀 Overview

Download your favorite albums from Spotycai with ease! This automated tool navigates the website, extracts MP3 links, downloads songs, and even embeds album artwork - all with minimal user intervention.

---

## 📂 Project Structure

```
spotycai-downloader/
├── main.py                # Entry point script  
├── src/                   # Source code
│   ├── driver_setup.py    # Selenium WebDriver configuration
│   ├── album_scraper.py   # Extract song details from albums
│   ├── song_downloader.py # Handle MP3 downloads
│   ├── mp3_tagging.py     # Embed album artwork
│   ├── utils.py           # Utility functions
│   └── __init__.py        # Package initialization
├── album_downloaded/      # Storage for downloaded albums
├── requirements.txt       # Python dependencies
├── environment.yml        # Conda environment file
├── LICENSE                # MIT License
├── README.md              # Project documentation
└── banner.png             # Project banner image
```

---

## ✨ Features

✔ **Automated Scraping**: Navigate Spotycai's website structure with Selenium.  
✔ **Bulk Downloads**: Get entire albums with a single command.  
✔ **Album Artwork**: Automatically embed cover art into MP3 files.  
✔ **Organized Library**: Creates folder structures based on artist and album names.  
✔ **Headless Operation**: Runs without browser UI for efficiency.

---

## ⚙️ Prerequisites

Ensure you have the following installed:

- **Python**: Version 3.x
- **Google Chrome**: Required for WebDriver
- **Libraries**: Selenium, WebDriver Manager, Requests, eyed3

---

## 📥 Installation

1. **Clone the repository**:
    
```bash
git clone https://github.com/your-username/script_spotycai.git
cd script_spotycai
```

2. **Install dependencies**:
    
```bash
pip install -r requirements.txt
```

---

## 📖 Usage

1. **Set your target album**:
   Edit the `album_url` in `main.py`:
    
```python
if __name__ == "__main__":
    album_url = "https://www.torrenet.xyz/spotycai/album/738/Antonio+Álvarez+Cordero+(Bizcocho)/Los+hermanos+del+buen+fin"
    download_all_songs(album_url)
```

2. **Run the downloader**:
    
```bash
python main.py
```

3. **Find your music**:
   Downloaded albums are saved in `album_downloaded/[album_title]/`

---

## 🔄 Workflow

1. **Initialize WebDriver** → Set up headless Chrome browser.
2. **Navigate to Album** → Access the specified Spotycai album page.
3. **Extract Song Data** → Collect URLs and metadata for each track.
4. **Download MP3s** → Save files to organized folders.
5. **Add Album Art** → Embed cover images into MP3 metadata.

---

## 🛠️ Customization

🔹 **Browser Visibility** → To see the browser during execution, edit `src/driver_setup.py`:
```python
# Comment this line to disable headless mode
# options.add_argument("--headless")
```

🔹 **File Organization** → Album folders are named after the album title by default.

---

## 📌 Future Enhancements

- **Release Dates** → Add album release years to folder names.
- **Playlist Support** → Extend functionality to download playlists.
- **ID3 Tags** → Improve metadata tagging with additional info.
- **Download Queue** → Process multiple albums sequentially.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch:
    
```bash
git checkout -b feature/new-feature
```

3. Commit your changes:
    
```bash
git commit -m "Add new feature"
```

4. Push to the branch:
    
```bash
git push origin feature/new-feature
```

5. Open a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See LICENSE for details.

---

🎉 **Enjoy your music collection!**