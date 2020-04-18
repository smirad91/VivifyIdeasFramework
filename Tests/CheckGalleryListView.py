from selenium import webdriver

from Lib.GalleryListViewPage import GalleryListViewPage


driver = webdriver.Chrome()
driver.get("https://gallery-app.vivifyideas.com/")


glv = GalleryListViewPage(driver)
gallery_list = glv.get_currentList()
if len(gallery_list) == 0:
    exit("Gallery list not shown")
