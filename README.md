_This project is unmaintained. Feel free to use the source anyway though!_

This is a unofficial OStatus implementation for major social networking sites
that don't implement it themselves, including Facebook, Twitter, and Google+.
It's deployed at http://ostatus-unofficial.appspot.com/

It's part of a wider collection of OStatus and federated social web tools for
Facebook, Twitter, and Google+:

* https://github.com/snarfed/ostatus-unofficial
* https://github.com/snarfed/portablecontacts-unofficial
* https://github.com/snarfed/salmon-unofficial
* https://github.com/snarfed/webfinger-unofficial

License: This project is placed in the public domain.

Background on OStatus:
http://ostatus.org/about

The tests require the App Engine SDK and python-mox.


#### TODO

- merge all projects together into one codebase and app id? yes. but maybe later
  after below. OR more likely, just double down on serving each protocol from
  its own app id? e.g. serve atom feeds from salmon-unofficial, not
  ostatus-unofficial? probably need to merge separate twitter/fb app ids though.1

- publish activitystreams atom feed for user with profile data, salmon endpoint,
  and push hub (section 11)

- send status updates to federated friends via salmon w/ostatus:attention
  - subscribe/unsubscribe with schema:follow and ostatus:unfollow
  - etc in spec section 10

- implement push server and send pings for events


#### Misc

other libraries and tools that might be useful for reuse or interop testing:

https://github.com/Cerberus98/yagi
https://github.com/cdent/py-ostatus
