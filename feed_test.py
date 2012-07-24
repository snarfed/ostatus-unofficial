#!/usr/bin/python
"""Unit tests for feed.py.
"""

__author__ = ['Ryan Barrett <ostatus@ryanb.org>']

import json

import feed

from activitystreams import facebook_test
from activitystreams import twitter_test
from webutil import testutil


class FeedTest(testutil.HandlerTest):

  def test_facebook_feed(self):
    self.expect_urlfetch('https://graph.facebook.com/ryan/posts?offset=0&limit=100',
                         json.dumps({'data': [facebook_test.POST]}))
    self.expect_urlfetch('https://graph.facebook.com/ryan',
                         json.dumps(facebook_test.USER))
    self.mox.ReplayAll()

    path = '/feed/acct:ryan@facebook.com/@self?format=atom'
    resp = feed.application.get_response(path)
    self.assertEquals(200, resp.status_int, resp.body)
    self.assert_multiline_equals(
      facebook_test.ATOM % {'request_url': 'http://localhost/ryan/%40self?format=atom'},
      resp.body)
