from app import random_string
class shortened_url_db:
    def __init__(self):
        pass
    def __int__(self, short, long):
        self.urls = {}
        self.urls[short] = long
    def add_url(self, long):
        unique_short = self.search_for_unique()
        self.urls[unique_short] = long
        return unique_short
    def search_for_unique(self):
        new_short = random_string.get_random_alphanumeric_string(5)
        while new_short in self.urls:
            new_short = random_string.get_random_alphanumeric_string(5)
        return new_short

