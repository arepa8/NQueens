"""
	NQueens Challenge Accepted
	@author: Andres Hernandez
"""

from models import Solution, create_session, create_db

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
		result = list()
		i = 0
		for position in solution:
			tupple = (i,position.column)
			result.append(tupple)
			i+=1
		print("Solution: {}".format(result))
		self.save(result)


	def save(self, solution):
		session = create_session()
		new = Solution(nqueen=self.size,solution=str(solution))
		session.add(new)
		try:
			session.commit()
		except Exception as e:
			print("Commiting the solution: {}".format(e))
			session.rollback()
		session.close()


if __name__ == '__main__':
	create_db()
	print("----   NQueen Solver   -----")
	while True:
		print("If you want to play, insert a positive number")
		print("If you want to quit, insert '0'.")
		n = input("Insert a number: ")
		if int(n)<=0:
			print("Bye.")
			break
		else:
			NQueens(int(n))
