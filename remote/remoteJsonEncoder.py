import json


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, message.message) or isinstance(obj, header.header) or isinstance(obj, body.body):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)
