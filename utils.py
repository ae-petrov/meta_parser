import re
from string import Template


URL_pattern = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)'
        r'+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def url_is_valid(url: str) -> bool:
    """Check if URL valid or not."""
    if url == '':
        return False
    else:
        return (re.match(URL_pattern, url))


def render_page(template: str, result=None) -> str:
    with open(template, "r") as html:
        html_string = html.read()
        html_template = Template(html_string)

    return html_template.safe_substitute(message=result)
