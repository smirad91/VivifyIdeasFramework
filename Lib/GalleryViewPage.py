#Representing page: https://gallery-app.vivifyideas.com/galleries/

class GalleryViewPage:

    def __init__(self, driver):
        self.driver = driver

    def _get_base_object(self):
        return self.driver.find_element_by_css_selector("div[class='container']")

    def get_title(self):
        base = self._get_base_object()
        title = base.find_element_by_tag_name("h1").text.strip()
        return title

    def check_title(self, title):
        return title.lower() == self.get_title().lower()
