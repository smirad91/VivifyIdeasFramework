#Representing page: https://gallery-app.vivifyideas.com/

from time import sleep

from DataStructure.Gallery import Gallery


class GalleryListViewPage:

    def __init__(self, driver):
        self.driver = driver

    def get_currentList(self):
        gallery_list = []
        sleep(5) # this should be change to not static wait, this should wait for some object to appear
        grid_object = self.driver.find_element_by_css_selector("div[class='grid']")
        g_list = grid_object.find_elements_by_tag_name("div")
        for gallery in g_list:
            gallery_view_page = self._create_gallery(gallery)
            gallery_list.append(gallery_view_page)
        return gallery_list

    def _create_gallery(self, div):
        # parameter div is WebElement object in list view that contains info about specific gallery
        # returns GalleryFromList object
        title = div.find_element_by_tag_name("h2").text.strip()
        author = div.find_element_by_tag_name("p").text.split(":")[1].strip()
        img = div.find_element_by_tag_name("img").get_attribute("src")
        date = div.find_element_by_tag_name("small").text.split(":")[1].strip()
        gfl = Gallery(title, author, img, date)
        return gfl

    def open_galleryByIndex(self, index):
        sleep(5) # should be change to not static wait
        grid_object = self.driver.find_element_by_css_selector("div[class='grid']")
        gallery = grid_object.find_elements_by_tag_name("div")[index-1]
        gallery_to_open = self._create_gallery(gallery)
        gallery.find_element_by_tag_name("h2").find_element_by_tag_name("a").click()
        sleep(5)
        return gallery_to_open

    def get_listByTitle(self, title):
        pass