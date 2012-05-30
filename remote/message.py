from . import body
from . import header
from . import base


class message(base.base):
    def __init__(self):
        self.header = header.header()
        self.body = body.body()
        
        base.base.__init__(self)
        
    def tojson(self):
        return dict(header = self.header, body = self.body)
    
