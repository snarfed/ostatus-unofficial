#!/usr/bin/env python
"""Serves the discovery files.

The discovery files inside /.well-known/ include host-meta (XRD), and
host-meta.xrds (XRDS-Simple), and host-meta.jrd (JRD ie JSON).
"""

__author__ = 'Ryan Barrett <ostatus@ryanb.org>'

from webutil import handlers
from webutil import webapp2

from google.appengine.ext.webapp.util import run_wsgi_app


application = webapp2.WSGIApplication(
  handlers.HOST_META_ROUTES,
  debug=appengine_config.DEBUG)

def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
