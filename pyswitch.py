# pyswitch version 1.0
class Switch:
    def __init__(self,target):
        self.target = target
        self.cases = []
    
    def case(self,case):
        self.cases.append(self.target == case)
        return self.target == case
    
    def default(self):
        for x in self.cases:
            if x:
                return False
        return True

    def restart(self,newTarget):
        self.target = newTarget

"""
Example:


var = 2
s = Switch(var)

if s.case(0):
    print("zero")
if s.case(1):
    print("one")
if s.case(2):
    print("two")
if s.default():
    print("some other number")


"""   

"""
Changelog:
1.0.1 - added restart method
"""