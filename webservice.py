import json

import cherrypy

from meta_parser import processing_url
from settings import DEFAULT_MESSAGE, WEBSERVICE_CONF
from utils import render_page


class SimplePage(object):
    @cherrypy.expose
    def index(self):
        """Rendering index page."""
        return render_page('template/index.html')

    @cherrypy.expose
    def collect(self, url):
        """Runs after collect tag button is pressed."""
        return render_page('template/collected.html',
                           result=json.dumps(processing_url(url),
                                             indent=4, ensure_ascii=False))

    @cherrypy.expose
    def default(self, attr=''):
        """Handle all other endpoints not included in methods above
           and returns index page."""
        return self.index()


@cherrypy.expose
class WebServiceAPI(object):

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self, url=None):
        """Main method for API. Returns JSON or error message."""
        url = cherrypy.request.params.get('url')
        if url:
            return processing_url(url)
        else:
            return '''No URL key in request. Use following pattern:
                      http://app_domain/api/?url=<URL_YOU_WANT_TO_PARSE>'''

    @cherrypy.tools.json_out()
    def POST(self, url=None):
        """Handling other methods."""
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def PUT(self, url=None):
        """Handling other methods."""
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def DELETE(self, url=None):
        """Handling other methods."""
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def PATCH(self, url=None):
        """Handling other methods."""
        return DEFAULT_MESSAGE


if __name__ == '__main__':
    webservice = SimplePage()
    webservice.api = WebServiceAPI()
    cherrypy.quickstart(webservice, '/', WEBSERVICE_CONF)
