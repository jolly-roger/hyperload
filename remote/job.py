import cherrypy
import socket

import dal.job
import auth.user

from auth import isAuthorized as authorization


START_JOB_SIG = "start_job"
STOP_JOB_SIG = "stop_job"
JOB_STATUS_SIG = "job_status"
JOB_STATS_SIG = "job_stats"

HOST_NAME = "hyperload.net"
HOST_PORT = 11011
READ_BUFFER_SIZE = 1024


class job(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def start(self, jobId=None):
        s = socket.socket()
        s.connect((HOST_NAME, HOST_PORT))
        self.sendmsg(s, START_JOB_SIG, jobId)
        m = self.recvmsg(s)
        s.close()
        
        return m
            
    @cherrypy.expose
    @authorization.isAuthorized
    def stop(self, jobId=None):
        s = socket.socket()
        s.connect((HOST_NAME, HOST_PORT))
        self.sendmsg(s, STOP_JOB_SIG, jobId)
        m = self.recvmsg(s)
        s.close()
        
        return m
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstatus(self, jobId):
        s = socket.socket()
        s.connect((HOST_NAME, HOST_PORT))
        self.sendmsg(s, JOB_STATUS_SIG, jobId)
        m = self.recvmsg(s)
        s.close()
        
        return m
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstats(self, jobId):
        s = socket.socket()
        s.connect((HOST_NAME, HOST_PORT))
        self.sendmsg(s, JOB_STATS_SIG, jobId)
        m = self.recvmsg(s)
        s.close()
        
        return m
    
    def recvmsg(self, s):
        m = ""
        
        while True:
            data = s.recv(READ_BUFFER_SIZE)
            if data:
                m += str(data, encoding="utf-8")
            else:
                break
        
        return m
    
    def sendmsg(self, s, method, jobId):
        msg = "{"\
                    "\"header\":{"\
                        "\"method\": \"" + method + "\","\
                        "\"job\": \"" + jobId + "\""\
                    "}," \
                    "\"body\":{}"\
               "}"
        
        s.sendall(msg.encode("utf-8"))