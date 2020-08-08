import os.path
import re

import cherrypy


class Tag(object):
    """Class describes tags. Add new if necessary."""
    def __init__(self, name: str, regex: re.Pattern) -> None:
        if not isinstance(regex, re.Pattern):
            raise TypeError(f'"{regex}" in "{name}" '
                            f'Tag is not regular expression.')

        self.name = name
        self.regex = regex


# Initializate tags here
og = Tag('Open Graph', re.compile(r"^og:[\S]*$"))
fb = Tag('Facebook', re.compile(r"^fb:[\S]*$"))
tw = Tag('Twitter', re.compile(r"^twitter:[\S]*$"))
al = Tag('Mobile', re.compile(r"^al:[\S]*$"))
vk = Tag('Vkontakt', re.compile(r"^vk:[\S]*$"))

# Add initialized tags here to use them in process
SELECTED_TAGS = (og, fb, tw, al, vk,)

# CherryPy server configuration
WEBSERVICE_CONF = {
    '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },

    '/api': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type',
                                            'application/json')],
    },
}

# Default message for handling not GET methods
DEFAULT_MESSAGE = '''Method not allowed, use GET Method.
                     Use following pattern:
                     http://open-grap.gq/api/?url=<URL_YOU_WANT_TO_PARSE>'''
