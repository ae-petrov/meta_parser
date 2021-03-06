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
            meta_tag = dict(attrs)

            for item in SELECTED_TAGS:

                for i in range(len(attrs)):
                    if item.regex.fullmatch(attrs[i][1]):
                        item_node = self.all_nodes[self.url][item.name]
                        item_node[attrs[i][1]] = meta_tag.get('content')


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

    return message
