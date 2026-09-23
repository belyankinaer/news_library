from author import Author

class Article:
    def __init__(self, name: str, text: str, author: Author):
        self._name = name
        self._text = text
        self._author = author
        self._site = None

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_site(self):
        return self._site

    def upload_to_site(self, site):
        self._site = site
