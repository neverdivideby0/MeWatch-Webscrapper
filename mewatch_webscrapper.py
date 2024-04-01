import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import time
import os

class MeWatchDownloader:
    def __init__(self, season_path):
        self.base_url = 'https://www.mewatch.sg'
        self.season_path = season_path
        self.driver = webdriver.Safari()
        # TODO: Update with Regex pattern for extracting title and episode number
        self.pattern = re.compile(r"(My-Star-Guide-S6)-(E\d+)-\d+")

    def load_full_page(self):
        try:
            self.driver.get(self.base_url + self.season_path)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "d2-item__title")))
            while True:
                try:
                    load_more_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Load More')]")))
                    load_more_button.click()
                    time.sleep(3)
                except:
                    break
            return self.driver.page_source
        except Exception as e:
            print(f"Failed to load the full page: {e}")
            return None

    def extract_episode_urls(self, page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        anchor_tags = soup.find_all('a', class_='d2-item__title truncate')
        return [self.base_url + tag['href'] for tag in anchor_tags]

    def download_video(self, episode_url, counter):
        match = self.pattern.search(episode_url)
        if match:
            title = match.group(1).replace('-', ' ')
            episode_number = match.group(2)
            episode_name = f"{title} {episode_number}"
        else:
            episode_name = "UnknownEpisode"

        self.driver.get(episode_url)
        time.sleep(35)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        videos = self.driver.find_elements(By.TAG_NAME, "video")
        video_url = videos[1].get_attribute('src') if len(videos) > 1 else videos[0].get_attribute('src')

        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            parsed_url = urlparse(video_url)
            base_file_name = os.path.basename(parsed_url.path)
            file_name = f"{counter}_{episode_name}_{base_file_name}" if base_file_name else f"{counter}_{episode_name}_downloaded_video.mp4"
            
            # TODO: Update with the specific file path and write the video file
            file_path = os.path.join('/Users/bryanlee/Desktop/Side_Projects/Mewatch_Project/', file_name)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Video downloaded successfully: {file_path}")

    def run(self):
        page_source = self.load_full_page()
        if page_source:
            episode_urls = self.extract_episode_urls(page_source)
            counter = 1
            for episode_url in episode_urls:
                self.download_video(episode_url, counter)
                counter += 1
        self.driver.quit()

if __name__ == "__main__":
    # TODO: Update with the specific season path you're targeting
    season_path = '/season/My-Star-Guide-S6-195550'
    downloader = MeWatchDownloader(season_path)
    downloader.run()
