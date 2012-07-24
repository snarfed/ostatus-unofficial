#!/usr/bin/env python
"""Serves a user's OStatus profile feed.

Background:
http://ostatus.org/sites/default/files/ostatus-1.0-draft-2-specification.html#anchor11
"""

__author__ = 'Ryan Barrett <ostatus@ryanb.org>'

import appengine_config

from activitystreams import activitystreams
from activitystreams import facebook
from activitystreams import twitter

from webutil import handlers
from webutil import util
from webutil import webapp2

DOMAINS_TO_SOURCES = {
  'facebook.com': facebook.Facebook,
  # TODO: find activitystreams feed for g+
  'gmail.com': None,
  'twitter.com': twitter.Twitter,
  }


class UserFeedHandler(activitystreams.Handler):
  """Returns a user's ActivityStreams profile feed in Atom format.

  Instance attributes:
    source: the activitystreams.Source subclass to use
  """

  def get(self, acct_uri, rest):
    """The GET handler.

    Args:
      acct_uri: string, e.g. me@twitter.com. this is the second path element.
      rest: rest of the path
    """
    user, domain = util.parse_acct_uri(acct_uri, DOMAINS_TO_SOURCES.keys())
    self.source = DOMAINS_TO_SOURCES[domain]
    # TODO: refactor a common method out of Handler.get() instead of this ugliness
    self.request.path_info = '/%s%s' % (user, rest)
    super(UserFeedHandler, self).get()

  def source_class(self):
    """Return the Source subclass to use."""
    return self.source


application = webapp2.WSGIApplication([
    ('/feed/([^/]+)(/.+)?', UserFeedHandler),
    ], debug=appengine_config.DEBUG)

def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
