import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from urllib.parse import urlparse

# Base URL of MeWatch
base_url = 'https://www.mewatch.sg'

# TODO: Update with the specific season path you're targeting
season_path = '/season/My-Star-Guide-S6-195550'

# Initialize the Safari browser
driver = webdriver.Safari()
driver.get(base_url + season_path)
counter = 1

try:
    # Wait until the page loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "d2-item__title"))
    )

    # Continuously click "Load More" to reveal all episodes
    while True:
        try:
            load_more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Load More')]"))
            )
            load_more_button.click()
            time.sleep(3)  # Allow time for content to load
        except:
            break  # Exit loop when no more episodes to load

    # Parse the loaded page
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and store all episode URLs
    anchor_tags = soup.find_all('a', class_='d2-item__title truncate')
    episode_urls = [base_url + tag['href'] for tag in anchor_tags]

    # TODO: Update with Regex pattern for extracting title and episode number
    pattern = re.compile(r"(My-Star-Guide-S6)-(E\d+)-\d+")

    # Process each episode URL
    for episode_url in episode_urls:
        match = pattern.search(episode_url)
        if match:
            title = match.group(1).replace('-', ' ')
            episode_number = match.group(2)
            episode_name = f"{title} {episode_number}"
        else:
            episode_name = "UnknownEpisode"

        # Navigate to each episode's page
        driver.get(episode_url)

        # Account for possible ads and wait for video element
        time.sleep(35)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        videos = driver.find_elements(By.TAG_NAME, "video")
        
        # Extract video URL
        video_url = videos[1].get_attribute('src') if len(videos) > 1 else videos[0].get_attribute('src')
        
        # Download the video
        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            parsed_url = urlparse(video_url)
            base_file_name = os.path.basename(parsed_url.path)
            file_name = f"{counter}_{episode_name}_{base_file_name}" if base_file_name else f"{counter}_{episode_name}_downloaded_video.mp4"
            counter += 1
            
            # TODO: Update with the specific file path and write the video file
            file_path = os.path.join('/Users/bryanlee/Desktop/Mediacorp_Archives', file_name)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Video downloaded successfully: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
