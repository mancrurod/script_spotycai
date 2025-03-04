import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_song_elements(driver, album_url):
    """Fetch song elements from the album page."""
    print(f"Navigating to album URL: {album_url}")
    driver.get(album_url)
    
    try:
        # Wait until the song elements are loaded
        song_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".flex-table-row-item.track-number"))
        )
        print(f"Found {len(song_elements)} songs.")
        return song_elements
    except Exception as e:
        print(f"Error retrieving song elements: {e}")
        return []
    
def click_song(driver, song, index):
    """Clicks on a song element."""
    try:
        print(f"Clicking on song {index + 1}...")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", song)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(song)).click()
        time.sleep(3)  # Allow song to load
    except Exception as e:
        print(f"Error clicking song {index + 1}: {e}")
