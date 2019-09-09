#!/usr/bin/env python
import time

class pid:
    def __init__(self,Kp,Ki,Kd,ILimit = 500,PIDOverallLimit = 255):
        self.P = 0
        self.I = 0
        self.D = 0
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_time = 0
        self.time = 0
        self.last_Error = 0
        self.Error = 0
        self.I_limit = ILimit
        self.pid_overal_limit = PIDOverallLimit

    def update_pid(self,point,data):


        '''
        calculate error 
        '''
        self.Error = point - data        
        self.time = time.time()

        elapsed_time = int((self.time - self.last_time)*1000)


        '''
        calculate the P I D parameters
        '''
        self.P = self.Error * self.Kp
        self.D = ((self.Error - self.last_Error)/(elapsed_time) )* self.Kd
        self.I += ((self.Error ) * self.Ki )

        
        '''
        limit I parameters
        '''
        if self.I > self.I_limit: self.I = self.I_limit
        if self.I < -self.I_limit: self.I = -self.I_limit

        
        '''
        save tha last parameters
        '''
        self.last_time = self.time
        self.last_Error = self.Error



        '''
        calculate the pid
        '''
        pid = (self.P + self.I + self.D )


        '''
        limit last pid 
        '''
        if pid > self.pid_overal_limit: pid = self.pid_overal_limit
        if pid < -self.pid_overal_limit: pid = -self.pid_overal_limit
        
        return pid

    def get_i_term(self):
        return self.I

    def get_p_term(self):
        return self.P

    def get_d_term(self):
        return self.D
        
    def reset_I_term(self):
        self.I = 0