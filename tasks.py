import os
import sys
from datetime import datetime
from RPA.Browser.Selenium import Selenium
from config import TEMP_FOLDER, OUTPUT_FOLDER
from libraries.common import log_message, print_version, create_or_clean_dir

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def search_for(term):
    input_field = "css:input"
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    create_or_clean_dir(TEMP_FOLDER)
    create_or_clean_dir(OUTPUT_FOLDER)
    try:
        open_the_website("https://robocorp.com/docs/")
        search_for("python")
        store_screenshot("output/screenshot.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    digital_worker_name = "Digital Worker Template"
    log_message(f'Start "{digital_worker_name}"')
    print_version()

    main()

    log_message(f'End "{digital_worker_name}"')
