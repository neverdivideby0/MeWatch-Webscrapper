# MeWatch-Webscrapper
Created a MeWatch (Singaporean digital video on demand service brand owned by Mediacorp) Webscrapper and Video Converter (m3u8 -> mp4)

## Overview
This repository contains scripts for web scraping, optimized for macOS using the Safari browser.

## Getting Started

### Requirements
- macOS
- Safari browser

### Installation

1. **Install Python and Jupyter Notebook**
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Install Jupyter Notebook using Python's package manager: `pip install notebook`.
   - Add Python to your PATH to make it accessible from the command line. This is necessary for the system to recognize Python commands globally.

2. **Setting up PATH using Zsh and Nano**
   - macOS uses Zsh (Z shell) as its default shell. It reads configurations from `.zshrc` file.
   - Use Nano, a text editor, to edit `.zshrc` by running `nano ~/.zshrc` in the terminal.
   - Add `export PATH="/path/to/python:$PATH"` to the file.
   - Save changes in Nano by pressing `Ctrl + O`, `Enter`, and exit using `Ctrl + X`.

3. **Install Homebrew**
   - Homebrew is a package manager for macOS, used for installing applications and tools.
   - Install it by running `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` in the terminal.

4. **Install FFmpeg**
   - FFmpeg is a multimedia framework for handling audio, video, and other multimedia files and streams.
   - Install it via Homebrew: `brew install ffmpeg`.
  
5. **Enable Remote Automation in Safari**
   - To allow the script to control Safari, turn on Remote Automation. Go to Safari's `Develop` menu, then select `Allow Remote Automation`. This permits automated control of Safari, which is essential for web scraping activities.

6. **Install Selenium**
   - Selenium is a tool for automating web browsers. Install it using Python's package manager: `pip install selenium`.
   - It's used in the script to interact with web pages programmatically.

7. **Dependencies Installation**
   - Ensure to install the necessary Python packages such as `requests`, `beautifulsoup4`, and `selenium` using `pip`.
  
8. **Handling Ads in the Script**
   - The current script uses a 35-second delay to account for potential advertisements, but it does not specifically target ad activity.
   - Future updates may include more precise ad handling.
   - Meanwhile, it's recommended to install Adblock Pro for Safari from Safari Extensions to minimize ad interruptions during scraping.

9. **Error Handling and Logging**
   - The scripts include basic error handling. For more detailed error tracking and logging, consider enhancing the scripts accordingly.

10. **Safety and Legal Disclaimer**
   - Always scrape responsibly and be aware of the legal implications of scraping and downloading content from websites. Ensure that you have the necessary permissions and rights for the content being scraped.

## Usage
Follow the scripts in this repository to perform web scraping tasks using Python and Jupyter Notebook on macOS.


# How it works
### Web Scraping Script
- **Functionality**: The web scraping script uses Selenium to automate a Safari browser session. It navigates to specified MeWatch pages, loads all available video content, and extracts video URLs.
- **Ad Handling**: Includes a 35-second delay to account for potential ads, but this is not an ad-specific solution.
- **File Saving**: Downloads and saves video files to a designated directory on your system.

### Video Conversion Script (Bash)
- **Purpose**: Converts downloaded videos from `.m3u8` to `.mp4` format.
- **Usage**: Iterates through a directory of `.m3u8` files, converting each to `.mp4` using FFmpeg.

Remember, these scripts are designed for educational purposes and should be used responsibly, adhering to MeWatch's terms of service and copyright laws.

## Usage Instructions
- **Web Scraping**: Run the Python script in a Jupyter Notebook or Python environment. Ensure Safari's remote automation is enabled.
- **Video Conversion**: Execute the Bash script in a terminal. It will automatically process files in the specified directory.


## Customization Guide

### Setting the Season Path
- **Locate the Season URL**: Visit the MeWatch website, navigate to the season you want to scrape, and copy the URL.
- **Update the `season_path` Variable**: In the script, set `season_path` to the path portion of the URL you copied.
  ```python
  base_url = 'https://www.mewatch.sg'
  season_path = '/season/Your-Season-Path-Here'
- **Regular Expression Pattern**: Customize the Pattern: Modify the regular expression pattern to match the title and episode format of the season you're scraping.
  ```python
  pattern = re.compile(r"Your-Regex-Pattern-Here")

### Setting the File Save Path
- **Specify Your Save Location**: Change the file_path to a directory where you want the videos saved on your system.
 ```python
  file_path = os.path.join('/Your/Custom/Path/Here', file_name)


## Running the Scripts

### Running the Python Script
First, execute the Python script via Jupyter Notebook to download videos from MeWatch.


### Running the Bash Script
After downloading the videos using the Python script, you can convert them from `.m3u8` to `.mp4` using the provided Bash script.

1. **Open Terminal**: Navigate to your terminal application.
2. **Navigate to Script Location**: Use the `cd` command to go to the directory where your Bash script is located.
   ```bash
   cd /path/to/your/bash/script

Run the Script: Execute the script by typing:
bash your_script_name.sh
Replace your_script_name.sh with the name of your Bash script.
What It Does
The script iterates through the downloaded .m3u8 files.
It uses FFmpeg to convert each file into an .mp4 format.
The script checks if each file exists before attempting conversion to avoid errors
