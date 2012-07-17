#!/usr/bin/python
"""Unit tests for feed.py.
"""

__author__ = ['Ryan Barrett <ostatus@ryanb.org>']

import feed
from webutil import testutil


class FeedTest(testutil.HandlerTest):

  def test_feed(self):
    pass
    # facebook.Facebook(key_name='ryan').save()
    # self.assertEqual(1, facebook.Facebook.all().count())

    # resp = app.application.get_response('/delete?kind=Facebook&key_name=ryan',
    #                                     method='POST')
    # self.assertEquals(302, resp.status_int, resp.body)
    # self.assertEquals('http://localhost/', resp.headers['Location'])
    # self.assertEqual(0, facebook.Facebook.all().count())
