from author import Author

class Article:
    def __init__(self, name: str, text: str, author: Author):
        self._name = name
        self._text = text
        self._author = author
        self._site = None

    def get_name(self):
        return self._name

    def get_author_name(self):
        if self._author:
            author_name = self._author.get_name()
        else:
            author_name = ""
        return author_name

    def get_site(self):
        return self._site

    def upload_to_site(self, site):
        self._site = site
