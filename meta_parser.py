from html.parser import HTMLParser
from typing import Dict, List, Union

import requests
from requests.exceptions import RequestException

from settings import SELECTED_TAGS
from utils import url_is_valid


class MetaHTMLParser(HTMLParser):
    def __init__(self, url: str, *args, **kwargs) -> None:
        """Describes MetaHTMLParser entity."""
        self.all_nodes = {url: {}}

        for item in SELECTED_TAGS:
            self.all_nodes[url][item.name] = {}

        self.url = url
        super().__init__(*args, **kwargs)

    def handle_starttag(self, tag: str, attrs: List) -> None:
        """Handle and process tag section if it is equal to 'meta'."""
        if tag == 'meta':
            for item in SELECTED_TAGS:
                if item.regex.fullmatch(attrs[0][1]):
                    item_node = self.all_nodes[self.url][item.name]
                    item_node[attrs[0][1]] = attrs[1][1]


def processing_url(url: str) -> Union[Dict, str]:
    """Processing url, chek if it is valid and parsing it."""
    if not url_is_valid(url):
        message = 'Invalid URL'

    else:
        try:
            response = requests.get(url)
        except RequestException as e:
            message = e.__doc__

        if response.status_code != 200:
            message = f'''HTTP response code {response.status_code},
                          reason {response.reason}'''

        else:
            html_parser = MetaHTMLParser(url=response.url)
            html_parser.feed(response.text)

            message = html_parser.all_nodes
            if message.get(url) is not None:
                for tag in SELECTED_TAGS:
                    if message[url][tag.name] == {}:
                        message[url][tag.name] = 'No tags were find of ' \
                                                 'this type'
            else:
                message = 'Error. Well, something goes wrong. ' \
                          'Check please URL you have entered. ' \
                          'The best way is to use copy-paste ' \
                          'from URL filed from browser. ' \
                          'Please try again.'

    return message
