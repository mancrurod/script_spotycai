# 🎵 Spotycai Song Downloader

**Spotycai Song Downloader** is a Python-based automation tool that allows you to download full albums from Spotycai, extract metadata, and embed album artwork into MP3 files — all in one script.

This project uses **Selenium WebDriver** to navigate the Spotycai website, automate downloads, and tag MP3 files using `eyeD3`. It’s designed for users who want to organize their music collection efficiently with minimal manual effort.

---

## 🚀 Features

- 🔎 Automated scraping of Spotycai album pages
- 💽 Bulk MP3 downloads by album
- 🖼️ Embedded cover art and metadata (ID3 tagging)
- 📁 Clean folder structure: albums stored by artist and album title
- 🧑‍💻 Headless mode support for silent execution

---

## 🧰 Technologies Used

- `Python 3.10+`
- `Selenium` for browser automation
- `eyeD3` for MP3 tagging
- `requests`, `os`, `time`, `re`, and standard libraries

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/mancrurod/script_spotycai.git
cd script_spotycai
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install [ChromeDriver](https://sites.google.com/chromium.org/driver/) and make sure it matches your version of Chrome.

---

## ⚙️ How to Use

1. Run the script:

```bash
python script.py
```

2. Enter the album URL from Spotycai when prompted.

3. Wait for the download and tagging process to complete.

> Note: Make sure the website is accessible in your region and you have Chrome properly configured.

---

## 📁 Output Structure

```
downloads/
└── Artist Name/
    └── Album Name/
        ├── 01 - Track Name.mp3
        ├── 02 - Track Name.mp3
        └── cover.jpg
```

---

## 📌 Notes

- This tool is intended for educational and personal archiving purposes.
- Spotycai is a third-party website. Use responsibly and respect copyright laws.

---

## 👨‍💻 Author

Developed by **Manuel Cruz Rodríguez**  
[LinkedIn](https://www.linkedin.com/in/mancrurod/) · [GitHub](https://github.com/mancrurod)

---

## 📘 License

This project is licensed under the MIT License.