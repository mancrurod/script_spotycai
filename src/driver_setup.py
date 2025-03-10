import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """Sets up and returns a Selenium WebDriver instance."""
    print("Setting up WebDriver...")
    
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (remove to see the browser)
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--window-size=1920,1080")  # Set the window size
    options.add_argument("--mute-audio")  # Mute the browser audio
    
    service = Service(ChromeDriverManager().install())  # Set up the ChromeDriver service
    driver = webdriver.Chrome(service=service, options=options)  # Initialize the WebDriver with the specified options
    
    print("WebDriver setup complete.")
    return driver  # Return the WebDriver instance
