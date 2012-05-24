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


class job(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def start(self, jobId=None):
        s = socket.socket()
        s.connect(("hyperload.net", 11011))
        
        #sendmsg = "{}"
        #sendmsglen = len(sendmsg)
        #totalsent = 0
        #
        #while totalsent < sendmsglen:
        #    sent = s.send(sendmsg[totalsent:])
        #    if sent == 0:
        #        raise RuntimeError("socket connection broken")
        #    totalsent = totalsent + sent
        #
        #recvmsg = ""
        
        s.send("{"\
                    "header:{"\
                        "method: \"start_job\","\
                        "job: \"" + jobId + "\""\
                    "}," \
                    "body:{}"\
               "}".encode('ascii'))

        m = s.recv(1024)
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