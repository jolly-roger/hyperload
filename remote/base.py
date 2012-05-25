class base(object):
    def tojson(self):
        return json.dumps(self.__dict__, cls=remoteJsonEncoder)