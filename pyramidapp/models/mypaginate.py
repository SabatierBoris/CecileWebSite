# coding : utf-8
"""
The new paginate item
"""
from paginate import Page
import re


class MyPage(Page):
    """
    Custom version of Page for have control of pager
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.url = None
        super(MyPage, self).__init__(*args, **kwargs)

    def get_pages(self, form='~2~', url=None):
        """
        Get n tuple of symbol, url and boolean if it's current page
        """
        self.url = url
        radius = int(re.search(r'~(\d+)~', form).group(1))
        if self.first_page == self.last_page:
            return

        leftmost_page = max(self.first_page, (self.page-radius))
        rightmost_page = min(self.last_page, (self.page+radius))

        if leftmost_page > self.first_page:
            yield self.get_item_pages('«', self.first_page)
        for thispage in range(leftmost_page, rightmost_page+1):
            yield self.get_item_pages(thispage, thispage)
        if rightmost_page < self.last_page:
            yield self.get_item_pages('»', self.last_page)

    def get_item_pages(self, name, number):
        """
        Get the tuple for get_pages method
        """
        return (name, self._default_url_maker(number), (number == self.page))
