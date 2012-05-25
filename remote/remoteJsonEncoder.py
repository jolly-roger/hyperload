import json

import remote.message as message
import remote.header as header
import remote.body as body


class remoteJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, message.message) or isinstance(obj, header.header) or isinstance(obj, body.body):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)
