#!/usr/bin/env python
"""Serves a user's OStatus profile feed.

Background:
http://ostatus.org/sites/default/files/ostatus-1.0-draft-2-specification.html#anchor10
"""

__author__ = 'Ryan Barrett <ostatus@ryanb.org>'

import appengine_config
from webutil import handlers
from webutil import webapp2


class FeedHandler(handlers.TemplateHandler):
  """Returns a user's feed."""
  def get(self, email):
    pass


application = webapp2.WSGIApplication([
    ('/feed/([^/]+)', FeedHandler),
    ], debug=appengine_config.DEBUG)

def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
