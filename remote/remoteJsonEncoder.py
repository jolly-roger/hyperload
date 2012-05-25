import json

from remote import message as message
from remote import header as header
from remote import body as body


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, message.message) or isinstance(obj, header.header) or isinstance(obj, body.body):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)