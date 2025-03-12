from src.driver_setup import setup_driver
from src.album_scraper import get_album_cover, get_song_elements, click_song
from src.song_downloader import get_mp3_url, download_mp3, download_cover_image, add_cover_to_mp3
from src.utils import create_album_folder

def download_all_songs(album_url):
    # Setup WebDriver
    driver = setup_driver()
    
    # Get album cover URL
    cover_url = get_album_cover(driver, album_url)
    
    # Extract album title from the URL by replacing "+" with spaces
    album_title = album_url.split('/')[-1].replace('+', ' ')

    # Use extracted album title to create folder
    album_folder = create_album_folder(album_title)

    # Download album cover image
    cover_image_path = download_cover_image(cover_url, album_folder)
    
    # Get song elements
    song_elements = get_song_elements(driver, album_url)
    
    # Iterate through each song element and download the MP3
    for index, song in enumerate(song_elements):
        click_song(driver, song, index)
        mp3_url = get_mp3_url(driver)
        
        # Download the MP3 file
        mp3_file_path = download_mp3(mp3_url, album_folder)
        
        # Add cover art to the MP3 file
        if mp3_file_path and cover_image_path:
            add_cover_to_mp3(mp3_file_path, cover_image_path)
    
    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    album_url = "https://www.torrenet.xyz/spotycai/album/744/Jes%C3%BAs+Bienvenido+(Comparsas)/Las+Ratas"
    download_all_songs(album_url)
