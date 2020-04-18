from selenium import webdriver

from Lib.GalleryListViewPage import GalleryListViewPage
from Lib.GalleryViewPage import GalleryViewPage


driver = webdriver.Chrome()
driver.get("https://gallery-app.vivifyideas.com/")

glv = GalleryListViewPage(driver)
gallery_info = glv.open_galleryByIndex(1)


gv = GalleryViewPage(driver)
if not gv.check_title(gallery_info.get_title()):
    exit("Gallery that is opened from gallery list is not the same as title in opened page")
