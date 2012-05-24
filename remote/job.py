import cherrypy
import json
import urllib.request
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


class job(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def start(self, jobId=None):
        s = socket.socket()
        s.connect((HOST_NAME, HOST_PORT))

        msg = "{"\
                    "\"header\":{"\
                        "\"method\": \"" + START_JOB_SIG + "\","\
                        "\"job\": \"" + jobId + "\""\
                    "}," \
                    "\"body\":{}"\
               "}"
        
        s.sendall(msg.encode('utf-8'))

        m = ""
        
        while True:
            data = s.recv(2)
            if data:
                m += data
            else:
                break

        s.close()
        
        return m    
            
    @cherrypy.expose
    @authorization.isAuthorized
    def stop(self, jobId=None):
        return "test"
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstatus(self, jobId):
        pass
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getstats(self, jobId):
        pass