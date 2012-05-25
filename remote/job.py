import cherrypy
import socket
import json

import dal.job
import auth.user

from auth import isAuthorized as authorization
from . import message
from . import remoteJsonEncoder


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
        m = message.message()
        
        if jobId is not None:
            s = socket.socket()
            s.connect((HOST_NAME, HOST_PORT))
            
            m.header.method = START_JOB_SIG
            m.header.job = jobId
            
            s.sendall(json.dumps(m, cls=remoteJsonEncoder.remoteJsonEncoder).encode("utf-8"))
            
            m = self.recvmsg(s)
            s.close()
        
        return m
            
    @cherrypy.expose
    @authorization.isAuthorized
    def stop(self, jobId=None):
        m = message.message()
        
        if jobId is not None:
            s = socket.socket()
            s.connect((HOST_NAME, HOST_PORT))
            
            m.header.method = STOP_JOB_SIG
            m.header.job = jobId
            
            s.sendall(json.dumps(m, cls=remoteJsonEncoder.remoteJsonEncoder).encode("utf-8"))

            m = self.recvmsg(s)
            s.close()
        
        return m
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstatus(self, jobId):
        m = "{}"
        
        if jobId is not None:
            s = socket.socket()
            s.connect((HOST_NAME, HOST_PORT))
            
            m.header.method = JOB_STATUS_SIG
            m.header.job = jobId
            
            s.sendall(json.dumps(m, cls=remoteJsonEncoder.remoteJsonEncoder).encode("utf-8"))
            
            m = self.recvmsg(s)
            s.close()
        
        return m
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstats(self, jobId):
        m = "{}"
        
        if jobId is not None:
            s = socket.socket()
            s.connect((HOST_NAME, HOST_PORT))
            
            m.header.method = JOB_STATS_SIG
            m.header.job = jobId
            
            s.sendall(json.dumps(m, cls=remoteJsonEncoder.remoteJsonEncoder).encode("utf-8"))
            
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