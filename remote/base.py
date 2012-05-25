import json

from . import remoteJsonEncoder


class base(object):
    def tojson(self):
        import pdb; pdb.set_trace()
        return json.dumps(self.__dict__, cls=remoteJsonEncoder.remoteJsonEncoder)