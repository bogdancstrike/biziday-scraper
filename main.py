import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime as dt
from utils import convert_time_string_to_date, todayDate
import argparse
from classificator import categorize


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

    print("Will extract about {articles_number} articles\n".format(articles_number=20 * (args.scrolls + 1)))

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

    finish_percentage = 100 / args.scrolls
    for scroll in range(0, +args.scrolls):
        print("{finish}% articles extracted".format(finish=finish_percentage))
        finish_percentage = finish_percentage + 100 / args.scrolls
        loadMoreArticles(driver)

    # Save articles to list of dicts and export to JSON file
    print("\nexport articles to JSON file")

    articles = []
    articlesText = driver.find_elements(By.CLASS_NAME, 'post-title')
    articlesTimeAgo = driver.find_elements(By.CLASS_NAME, 'timeago')

    for item in range(0, len(articlesText)):
        articleJson = {
            "text": articlesText[item].text,
            "time": "{date}".format(date=convert_time_string_to_date(articlesTimeAgo[item].text).date()),
            "category": "{category}".format(category=categorize(articlesText[item].text))
        }
        articles.append(articleJson)
    export_to_file(articles)

    print("\nA total of {numar_articole} articles were extracted".format(numar_articole=len(articles)))

    print("\nArticles today: {articole}".format(articole=numberOfArticlesToday(articles)))

    print("Articles on {customDate}: {articole}".format(
        customDate=args.date,
        articole=numberOfArticlesOn(args.date, articles)))

    driver.quit()


def numberOfArticlesToday(articles):
    number = 0
    for article in articles:
        articleDate = dt.datetime.strptime(article.get("time"), '%Y-%m-%d').date()
        if articleDate == todayDate():
            number = number + 1
    return number


def numberOfArticlesOn(date, articles):
    number = 0
    for article in articles:
        articleDate = dt.datetime.strptime(article.get("time"), '%Y-%m-%d').date()
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
