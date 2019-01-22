class Location(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def moveLocation(Loc,Movement):
		#Movement is a 2-D tuple
		x = Movement[0]
		y = Movement[1]
		Loc.x += x
		Loc.y += y
		return Loc


class Drunk(object):
	