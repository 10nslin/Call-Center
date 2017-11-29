
from datetime import datetime
  
class Call(object):
    caller_number_ID = 0
    def __init__(self,name,phone_number,reason):

        self.name = name
        self.phone_number = phone_number
        self.time = datetime.now()
        self.reason= reason

        Call.caller_number_ID +=1

    def display(self):
        print "Id: " + str(Call.caller_number_ID)
        print "Caller Name:",self.name
        print "Phone Number:",self.phone_number
        print "Time of Call:",self.time.strftime("%b, %d %Y %I:%M:%S")
        print "Reason for Call:", self.reason

caller1 = Call("Bob Barker", "610-255-3061", "Winner")
caller1.display()
caller2 = Call("Carson Wentz", "612-543-9005", "MVP")
caller2.display()

class CallCenter(Call):
    def __init__(self):
        self.calls = []
      


    def queue_size(self):
        return len(self.calls)
  
    def add(self, new_call):
        self.calls.append(new_call)
        return self
    def remove(self, rme_call):
        self.calls.remove(rme_call)
        return self
    def info(self):
        print self.name
        print self.phone_number
        print self.queue_size
        return self

d = CallCenter()
d.add("caller1").add("caller2")

print d.queue_size()