import json

import cherrypy

from meta_parser import processing_url
from settings import DEFAULT_MESSAGE, WEBSERVICE_CONF


class SimplePage(object):
    @cherrypy.expose
    def index(self):
        return open('template/index.html')

    @cherrypy.expose
    def collect(self, url):
        return json.dumps(processing_url(url), indent=4, ensure_ascii=False)

    @cherrypy.expose
    def default(self, attr=''):
        return self.index()


@cherrypy.expose
class WebServiceAPI(object):

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self, url=None):
        url = cherrypy.request.params.get('url')
        if url:
            return processing_url(url)
        else:
            return 'No URL key in request. Use following pattern: ' \
                   'http://app_domain/?url=<URL_YOU_WANT_TO_PARSE>'

    @cherrypy.tools.json_out()
    def POST(self, url=None):
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def PUT(self, url=None):
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def DELETE(self, url=None):
        return DEFAULT_MESSAGE

    @cherrypy.tools.json_out()
    def PATCH(self, url=None):
        return DEFAULT_MESSAGE


if __name__ == '__main__':
    webservice = SimplePage()
    webservice.api = WebServiceAPI()
    cherrypy.quickstart(webservice, '/', WEBSERVICE_CONF)
