import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_album_cover(driver, album_url):
    """Fetch the album cover image URL from the album page."""
    print(f"Navigating to album URL: {album_url}")
    driver.get(album_url)  # Navigate to the album URL
    
    try:
        # Wait until the album cover image is loaded
        cover_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".album-image img"))
        )
        cover_url = cover_element.get_attribute("src")  # Get the URL of the album cover image
        print(f"Album cover found: {cover_url}")
        return cover_url
    except Exception as e:
        print(f"Error retrieving album cover: {e}")
        return None  # Return None if there is an error

def get_song_elements(driver, album_url):
    """Fetch song elements from the album page."""
    print(f"Navigating to album URL: {album_url}")
    driver.get(album_url)  # Navigate to the album URL
    
    try:
        # Wait until the song elements are loaded
        song_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".flex-table-row-item.track-number"))
        )
        print(f"Found {len(song_elements)} songs.")
        return song_elements  # Return the list of song elements
    except Exception as e:
        print(f"Error retrieving song elements: {e}")
        return []  # Return an empty list if there is an error
    
def click_song(driver, song, index):
    """Clicks on a song element."""
    try:
        print(f"Clicking on song {index + 1}...")
        # Scroll the song element into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", song)
        # Wait until the song element is clickable and then click it
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(song)).click()
        time.sleep(3)  # Allow song to load
    except Exception as e:
        print(f"Error clicking song {index + 1}: {e}")
