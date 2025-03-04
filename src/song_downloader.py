import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils import sanitize_filename

def get_mp3_url(driver):
    """Extracts the .mp3 URL."""
    try:
        # Try finding the video element first
        mp3_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "video#html5-player"))
        )
        if mp3_element:
            mp3_url = mp3_element.get_attribute("src")
            print(f"MP3 URL found: {mp3_url}")
            return mp3_url

        # If no video found, look for an <audio> element
        audio_elements = driver.find_elements(By.TAG_NAME, "audio")
        if audio_elements:
            mp3_url = audio_elements[0].get_attribute("src")
            print(f"MP3 URL found in audio element: {mp3_url}")
            return mp3_url

        # Lastly, look for direct links to MP3 files
        for link in driver.find_elements(By.TAG_NAME, "a"):
            href = link.get_attribute("href")
            if href and href.endswith(".mp3"):
                print(f"MP3 URL found in link tag: {href}")
                return href

        print("No MP3 URL found.")
        return None

    except Exception as e:
        print(f"Error retrieving MP3 URL: {e}")
        return None

def download_mp3(mp3_url, download_dir, retries=3):
    """Downloads the MP3 file."""
    if not mp3_url:
        print("No MP3 URL found. Skipping download.")
        return
    
    os.makedirs(download_dir, exist_ok=True)
    filename = os.path.join(download_dir, sanitize_filename(os.path.basename(mp3_url)))

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for attempt in range(retries):
        try:
            print(f"Downloading {mp3_url} to {filename} (Attempt {attempt + 1}/{retries})...")
            response = requests.get(mp3_url, headers=headers, stream=True, timeout=10)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Download complete: {filename}")
                return
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {mp3_url}: {e}")
        time.sleep(5)
    
    print(f"Failed to download {mp3_url} after {retries} attempts.")
