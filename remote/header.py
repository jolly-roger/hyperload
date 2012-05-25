from . import base


class header(base.base):
    def __init__(self):
        self.method = None
        self.job = None
        
        base.base.__init__(self)
    