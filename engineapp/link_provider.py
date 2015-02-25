from flask import request
from google.appengine.ext import ndb
import base58

class ShortLink(ndb.Model):
    link = ndb.StringProperty()

    @classmethod
    def check_existing_link(self, url):
        result = list(self.query(self.link == url))
        if len(result) == 0:
            return None

        return result[0].key

    @classmethod
    def create_new_link(self, url):
        shortLink = ShortLink(link=url)
        key = shortLink.put()
        return key

    @classmethod
    def _clean_url(self, url):
        if not ( url.startswith('http') or url.startswith('//') ):
            url = '//' + url
        return url

    @classmethod
    def generate_link(self, url):
        url = self._clean_url(url)
        link = self.check_existing_link(url)
        if link is None:
            link = self.create_new_link(url)

        return request.host_url + base58.encode(link.integer_id())

    @classmethod
    def get_link(self, key):
        try:
            id = base58.decode(key)
        except:
            return ""
        instance = self.get_by_id(id)
        if instance is None:
            return ""
        return instance.link

