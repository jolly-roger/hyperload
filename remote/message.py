import remote.base as base
import remote.header as header
import remote.body as body


class message(base.base):
    header = header.header()
    body = body.body()
    
