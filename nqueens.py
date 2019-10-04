"""

"""

class Position:
	def __init__(self, column, sons=list()):
		self.column = column
		self.sons = sons

	def __str__(self):
		return "<Column : {} | Sons: {}>".format(self.column,self.sons)

class NQueens:
	"""NQueens Problem solver"""
	def __init__(self, size):
		self.size = size
		self.solutions = 0
		self.tree = Position(None,list(Position(pos) for pos in range(size)))
		self.do_it()

	def __str__(self):
		return "NQueens {}".format(self.size)

	def do_it(self):
		if self.tree.sons:
			self.set_in_place(self.tree.sons,[])
			print(self)
			print("Solutions {}".format(self.solutions))

	def get_sons(self, place, taken_places):
		possible_sons = list(range(self.size))
		
		#remove place column and diagonals
		possible_sons.remove(place.column)
		if place.column + 1 < self.size:
			possible_sons.remove(place.column + 1)
		if place.column - 1 >= 0:
			possible_sons.remove(place.column - 1)
		
		#taken places to int array
		taken_places_int = [position.column for position in taken_places]

		#remove taken columns and diagonals
		for position in taken_places_int:
			if position in possible_sons:
				possible_sons.remove(position)
			target = len(taken_places) + 1 - taken_places_int.index(position)
			if (position + target < self.size) and (position + target in possible_sons) :
				possible_sons.remove(position + target)
			if (position - target >= 0) and (position - target in possible_sons) :
				possible_sons.remove(position - target)

		if possible_sons:
			return [Position(x) for x in possible_sons]
		else:
			return []


	def set_in_place(self,possible_places,taken_places):
		if len(taken_places) == self.size:
			self.pretty_print(taken_places)
			self.solutions += 1
		else:
			if possible_places:
				for place in possible_places:
					place.sons = self.get_sons(place,taken_places)
					self.set_in_place(place.sons,taken_places+[place])

	def pretty_print(self,solution):
		solution = [position.column for position in solution]
		print("Solution: {}".format(solution))


if __name__ == '__main__':
	NQueens(8)
