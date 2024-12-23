import app_functions
import time

URL = "https://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    while True:
        scraped = app_functions.scrape(URL)
        extracted = app_functions.extract(scraped)
        print(extracted)
        file_list = app_functions.read(extracted)
        if extracted != "No upcoming tours":
            if extracted+"\n" not in file_list:
                app_functions.store(extracted)
                app_functions.send_email(extracted)
        time.sleep(2)
