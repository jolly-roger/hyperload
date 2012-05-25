import json

from . import header
from . import body
from . import base


class message(base):
    header = header.header()
    body = body.body()
    
