# This is where chapter 15 exercises go.

# Exercise 15.3

class Point(object):
	"""Represents a point in 2-D space."""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def position(self):
		return self.x, self.y

class Rectangle(object):
	"""Represents a rectangle.

	attributes: width, height, corner
	"""

	def __init__(self, width, height, corner_x, corner_y):
		self.width = width
		self.height = height
		self.corner = Point(corner_x, corner_y)

	def find_center(self):
		p = Point(self.corner.x + self.width/2.0, self.corner.y + self.height/2.0)
		return p.position()

	def grow_rectangle(self, width, height):
		self.width += width
		self.height += height

	def move_rectangle(self, x, y):
		self.corner.x += x
		self.corner.y += y

def move_rectangle(rect, dx, dy):
	# Creates a new rectangle at the new point, instead of moving the old one.
	# The function name is strange for this operation.
	new_rect = Rectangle(rect.width, rect.height, rect.corner.x, rect.corner.y)
	new_rect.move_rectangle(dx, dy)
	return new_rect

rectyboy = Rectangle(50, 100, 2, 5)
new_location = move_rectangle(rectyboy, 25, 25)
print new_location.width, new_location.height, new_location.corner.x, new_location.corner.y
