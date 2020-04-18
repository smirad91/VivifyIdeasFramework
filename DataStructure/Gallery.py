class Gallery:

    def __init__(self, title, author, img_src, date=None, description=None, comments=None):
        self.title = title
        self.author = author
        self.img_src = img_src
        self.date = date
        self.description = description
        self.comments = comments

    def get_description(self):
        return self.description

    def get_comments(self):
        return self.comments

    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_imgSrc(self):
        return self.img_src


