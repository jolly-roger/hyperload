import json

import remote.message
import remote.header
import remote.body


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, remote.message.message) or isinstance(obj, remote.header.header) or isinstance(obj, remote.body.body):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)
