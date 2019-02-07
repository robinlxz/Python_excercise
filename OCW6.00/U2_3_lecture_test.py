import random

class Location(object):
    def __init__(self,x,y):
        '''OCW:Assume x and y are floats'''
        self.x = x
        self.y = y
    def distanceFrom(self, LocationY):
        dis = ((self.x - LocationY.x)**2 + (self.y - LocationY.y)**2)**0.5
        return dis
    def move(self, deltaX, deltaY):
        return Location(self.x+deltaX, self.y+deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return '<'+str(self.x)+', '+str(self.y)+'>'

class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
    def getLoc(self,drunk):
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
        return random.choice(stepChoices)


    #print 'position at turn %s is' %i, f1.getLoc(d1)

# d1 = Drunk('lxz')
# f1 = Field()
# l0 = Location(0,0)
# f1.addDrunk(d1,l0)
#
# for i in range(0):
#     f1.moveDrunk(d1)
#     #print 'position at turn %s is' %i, f1.getLoc(d1)
#
# print 'location for drunk d1 is', f1.getLoc(d1)
# print 'distance for drunk d1 is', f1.drunks[d1].distanceFrom(l0)

def lxz_drunk_test():
    for steps in [10,100,1000,10000]:
        d1 = Drunk('tester')
        f1 = Field()
        l0 = Location(0,0)
        f1.addDrunk(d1, l0)
        for i in range(steps):
            f1.moveDrunk(d1)
        print '\n-----------'
        print 'After %s steps' %steps, '\nlocation for drunk d1 is', f1.getLoc(d1)
        print 'distance for drunk d1 is', f1.drunks[d1].distanceFrom(l0)

lxz_drunk_test()