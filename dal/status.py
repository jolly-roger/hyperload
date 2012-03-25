from . import base
from . import constants

import dal.entities.status


class status(base.base):
    def __init__(self):
        base.base.__init__(self)    
    
    def getall(self):
        self.cur.execute(constants.GET_ALL_STATUSES)
        rawstatuses = self.cur.fetchall()
        
        return self._getStatusList(rawstatuses)
    
    def _getStatusList(self, rawstatuses):
        statuses = []
        
        for rawstatus in rawstatuses:
            statuses[len(statuses):] = [dal.entities.status.status(rawstatus[0], rawstatus[1], rawstatus[2])]
            
        return statuses