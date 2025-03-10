import os
import time
import requests
import eyed3
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils import sanitize_filename

def add_cover_to_mp3(mp3_file, cover_image):
    """Adds a cover image to the MP3 file's metadata."""
    try:
        # Load the MP3 file using eyed3
        audiofile = eyed3.load(mp3_file)

        # Read the cover image file
        with open(cover_image, "rb") as img_file:
            image_data = img_file.read()

        # Set the image as the cover art (3 represents front cover)
        audiofile.tag.images.set(3, image_data, "image/jpeg")

        # Save the changes to the MP3 file
        audiofile.tag.save()

        print(f"Cover art added to {mp3_file}")
    except Exception as e:
        print(f"Error adding cover art: {e}")

def get_mp3_url(driver):
    """Extracts the .mp3 URL."""
    try:
        # Try finding the video element first
        mp3_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "video#html5-player"))
        )
        if mp3_element:
            # Get the src attribute of the video element
            mp3_url = mp3_element.get_attribute("src")
            print(f"MP3 URL found: {mp3_url}")
            return mp3_url

        # If no video found, look for an <audio> element
        audio_elements = driver.find_elements(By.TAG_NAME, "audio")
        if audio_elements:
            # Get the src attribute of the first audio element
            mp3_url = audio_elements[0].get_attribute("src")
            print(f"MP3 URL found in audio element: {mp3_url}")
            return mp3_url

        # Lastly, look for direct links to MP3 files
        for link in driver.find_elements(By.TAG_NAME, "a"):
            href = link.get_attribute("href")
            if href and href.endswith(".mp3"):
                # Return the href attribute if it ends with .mp3
                print(f"MP3 URL found in link tag: {href}")
                return href

        print("No MP3 URL found.")
        return None

    except Exception as e:
        # Print the exception if any error occurs
        print(f"Error retrieving MP3 URL: {e}")
        return None

def download_mp3(mp3_url, download_dir, retries=3):
    """Downloads the MP3 file."""
    if not mp3_url:
        # Skip download if no MP3 URL is found
        print("No MP3 URL found. Skipping download.")
        return
    
    # Create the download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    # Sanitize the filename and create the full path
    filename = os.path.join(download_dir, sanitize_filename(os.path.basename(mp3_url)))

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for attempt in range(retries):
        try:
            # Attempt to download the MP3 file
            print(f"Downloading {mp3_url} to {filename} (Attempt {attempt + 1}/{retries})...")
            response = requests.get(mp3_url, headers=headers, stream=True, timeout=10)
            if response.status_code == 200:
                # Write the content to the file in chunks
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Download complete: {filename}")
                return filename  # Return the file path after successful download
        except requests.exceptions.RequestException as e:
            # Print the exception if any error occurs
            print(f"Error downloading {mp3_url}: {e}")
        # Wait for 5 seconds before retrying
        time.sleep(5)
    
    print(f"Failed to download {mp3_url} after {retries} attempts.")
    return None

def download_cover_image(cover_url, download_dir, retries=3):
    """Downloads the album cover image (jpg)."""
    if not cover_url:
        # Skip download if no cover URL is found
        print("No cover URL found. Skipping download.")
        return None
    
    # Save the cover image as a .jpg
    filename = os.path.join(download_dir, sanitize_filename("cover.jpg"))
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for attempt in range(retries):
        try:
            # Attempt to download the cover image
            print(f"Downloading cover image from {cover_url} to {filename} (Attempt {attempt + 1}/{retries})...")
            response = requests.get(cover_url, headers=headers, stream=True, timeout=10)
            if response.status_code == 200:
                # Write the content to the file in chunks
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Cover image download complete: {filename}")
                return filename  # Return the file path after successful download
        except requests.exceptions.RequestException as e:
            # Print the exception if any error occurs
            print(f"Error downloading cover image: {e}")
        # Wait for 5 seconds before retrying
        time.sleep(5)
    
    print(f"Failed to download cover image after {retries} attempts.")
    return None
