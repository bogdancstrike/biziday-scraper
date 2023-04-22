import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime as dt
from utils import convert_time_string_to_date, todayDate
import argparse


def main():
    # Read args
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scrolls",
                        help="How many scrolls to load",
                        type=int,
                        default=5,
                        required=False)
    parser.add_argument("-d", "--date",
                        help="In which date to show how many articles were extracted",
                        type=date_type,
                        default=dt.datetime.today().date(),
                        required=False)
    args = parser.parse_args()

    print("scrolls: ", args.scrolls)
    print("date: ", args.date)

    # Add additional options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(r"--user-data-dir=C:\\Users\\bogda\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument(r'--profile-directory=Default')
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    # Go to Biziday
    driver.get('https://www.biziday.ro/')
    sleep(2)

    for _ in range(0, +args.scrolls):
        loadMoreArticles(driver)
    articlesText = driver.find_elements(By.CLASS_NAME, 'post-title')
    articlesTimeAgo = driver.find_elements(By.CLASS_NAME, 'timeago')

    articles = []
    for item in range(0, len(articlesText)):
        articleJson = {
            "text": articlesText[item].text,
            "time": articlesTimeAgo[item].text
        }
        articles.append(articleJson)

    # Export articles to JSON file
    export_to_file(articles)

    print("\nAu fost extrase in total {numar_articole} articole".format(numar_articole=len(articles)))

    print("\nArticole astazi: {articole}".format(articole=numberOfArticlesToday(articles)))

    print("Articole in data de {customDate}: {articole}".format(
        customDate=args.date,
        articole=numberOfArticlesOn(args.date, articles)))

    driver.quit()


def numberOfArticlesToday(articles):
    number = 0
    for article in articles:
        articleDate = convert_time_string_to_date(article.get("time")).date()
        if articleDate == todayDate():
            number = number + 1
    return number

def numberOfArticlesOn(date, articles):
    number = 0
    for article in articles:
        articleDate = convert_time_string_to_date(article.get("time")).date()
        if articleDate == date:
            number = number + 1
    return number

def loadMoreArticles(driver):
    loadMoreButton = driver.find_element(By.ID, 'more')
    loadMoreButton.click()
    sleep(3)

def date_type(string):
    try:
        return dt.datetime.strptime(string, '%Y-%m-%d').date()
    except ValueError:
        msg = "Invalid date format: '{0}'. Expected format is 'YYYY-mm-dd'.".format(string)
        raise argparse.ArgumentTypeError(msg)

def export_to_file(articles):
    with open("articles.json", "w") as f:
        json.dump(articles, f)

if __name__ == "__main__":
    main()
