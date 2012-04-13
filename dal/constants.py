GET_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s, %(excludestatus)s, %(isshared)s, %(excludeisshared)s);"

ADD_TODO = "select addtodo(%(todoname)s, %(userid)s);"
SHARE_TODO = "select sharetodo(%(todoid)s, %(friendid)s);"
SET_STATUS = "select setstatus(%(todoid)s, %(statusid)s);"
SET_PRIORITY = "select setpriority(%(todoid)s, %(todopriority)s);"

GET_ALL_STATUSES = "select * from status;"


ADD_FB_USER = "select addfbuser(%(fbuserid)s);"


ADD_RESOURCE = "select addresource(%(resourcealias)s, %(resourcedomain)s, %(outeruserid)s);"
GET_RESOURCES = "select * from getresources(%(outeruserid)s);"