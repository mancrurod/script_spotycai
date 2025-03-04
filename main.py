from src.driver_setup import setup_driver
from src.album_scraper import get_song_elements, click_song
from src.song_downloader import get_mp3_url, download_mp3
from src.utils import create_album_folder

def download_all_songs(album_url):
    """Main function to automate song downloads."""
    print("Starting download process...")
    driver = setup_driver()

    # Extract album title from the URL by replacing "+" with spaces
    album_title = album_url.split('/')[-1].replace('+', ' ')
    
    songs = get_song_elements(driver, album_url)

    if not songs:
        print("No songs found. Exiting.")
        driver.quit()
        return
    
    # Use extracted album title to create folder
    album_folder = create_album_folder(album_title)

    for index, song in enumerate(songs):
        click_song(driver, song, index)
        mp3_url = get_mp3_url(driver)
        download_mp3(mp3_url, album_folder)

    print("All downloads complete. Closing driver.")
    driver.quit()

if __name__ == "__main__":
    album_url = "https://www.torrenet.xyz/spotycai/album/738/Antonio+Álvarez+Cordero+(Bizcocho)/Los+hermanos+del+buen+fin"
    download_all_songs(album_url)
