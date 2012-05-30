import json

from . import remoteJsonEncoder


class base(object):
    def tojson(self):
        return self.__dict__