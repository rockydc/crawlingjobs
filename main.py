import time
from selenium import webdriver
from pages.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from helper.Crawler import Crawler
from selenium.webdriver.chrome.options import Options

def TriggerCrawling():

    #driver
    options = Options()  # Initialize an instance of the Options class
    options.headless = True  # True -> Headless mode activated
    options.add_argument('window-size=1920x1080')  # Set a big window size, so all the data will be displayed
    #set user agent to avoid bot detector
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    driver.get('https://www.upwork.com/ab/account-security/login')
    #data login
    username = 'simanjuntak123@gmail.com'
    password = 'Situmeang182#'

    # login
    login = LoginPage(driver, username, password)
    crawler = Crawler()
    login.login()
    driver.get('https://www.upwork.com/nx/jobs/search/?q=automation%20selenium&sort=recency')
    # driver.maximize_window()
    btnPagination = "//button[contains(@class,'up-pagination-item up-btn' )]//span[contains(text(),'Next')]"
    #crawling
    totalPage = 5
    for i in range(totalPage):
        page_source = driver.page_source
        crawler.runCrawler(page_source)
        driver.find_element("xpath", btnPagination).click()
        time.sleep(1)
    #store to dataframe
    crawler.storeToMonggoDb()

    driver.quit()
    return "Crawling Berhasil dijalankan"

