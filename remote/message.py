from . import body
from . import header
from . import base


class message(base.base):
    header = header.header()
    body = body.body()
    
