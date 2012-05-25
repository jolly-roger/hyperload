import json

from . import header
from . import body
from . import message


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, message) or isinstance(obj, header) or isinstance(obj, body):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)
