import json

from . import message
from . import header
from . import body


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, message.message) or isinstance(obj, header.header) or isinstance(obj, body.body):
            return obj.tojson()
        return json.JSONEncoder.default(self, obj)
