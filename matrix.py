"""
Chapitre 11.2
"""


import numbers
import copy
import collections
import collections.abc


class Matrix:
	"""
	Matrice numérique stockée en tableau 1D en format rangée-major.

	:param height: La hauteur (nb de rangées)
	:param width: La largeur (nb de colonnes)
	:param data: Si une liste, alors les données elles-mêmes (`data` affectée, pas copiée). Si un nombre, alors la valeur de remplissage
	"""

	def __init__(self, height, width, data = 0.0):
		if not isinstance(height, numbers.Integral) or not isinstance(width, numbers.Integral):
			raise TypeError()
		if height == 0 or width == 0:
			raise ValueError(numbers.Integral)
		self.__height = height
		self.__width = width
		if isinstance(data, list):
			if len(data) != len(self):
				raise ValueError(list)
			self.__data = data
		elif isinstance(data, numbers.Number):
			self.__data = [data for i in range(len(self))]
		else:
			raise TypeError()

	@property
	def height(self):
		return self.__height

	@property
	def width(self):
		return self.__width

	@property
	def data(self):
		return self.__data

	# TODO: Accès à un élément en lecture
	def __getitem__(self, indexes):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		# TODO: Retourner la valeur
		index = (indexes[0]) * self.width + (indexes[1])
		return self.data[index]


	# TODO: Affectation à un élément
	def __setitem__(self, indexes, value):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		# TODO: L'affectation
		index = (indexes[0]) * self.width + (indexes[1])
		self.data[index] =  value

	def __len__(self):
		"""
		Nombre total d'éléments
		"""
		return self.height * self.width

	# TODO: Représentation affichable (conversion pour print)
	def __str__(self):
		# TODO: Chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.
		n = len(self.data)
		res = ''

		for i in range(0, n):
			if i != 0 and (i) % self.width == 0:
				res += '\n'
			res += f'{self.data[i]} '

		return res

	# TODO: Représentation officielle
	def __repr__(self):
		# TODO: une string qui représente une expression pour construire l'objet.
		return f"Matrix({self.height}, {self.width}, {self.data})"

	# TODO: String formatée
	def __format__(self, value):
		# TODO: On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`
		n = len(self.data)
		res = ''

		for i in range(0, n):
			if i != 0 and (i) % self.width == 0:
				res += '\n'
			el = format(self.data[i], value)
			res += f'{el} '

		return res

	def clone(self):
		return Matrix(self.height, self.width, self.data)

	def copy(self):
		return Matrix(self.height, self.width, copy.deepcopy(self.data))

	def has_same_dimensions(self, other):
		return (self.height, self.width) == (other.height, other.width)

	def __pos__(self):
		return self.copy()

	# TODO: Négation
	def __neg__(self):
		return Matrix(self.height, self.width, [-i for i in self.data])

	# TODO: Addition
	def __add__(self, other):
		if self.has_same_dimensions(other):
			pairs = list(zip(self.data, other.data))
			return Matrix(self.height, self.width, [int(i[0] + i[1]) for i in pairs])
	
	# TODO: Soustraction
	def __sub__(self, other):
		if self.has_same_dimensions(other):
			pairs = list(zip(self.data, other.data))
			return Matrix(self.height, self.width, [int(i[0] - i[1]) for i in pairs])
	
	# TODO: Multiplication matricielle/scalaire
	def __mul__(self, other):
		if isinstance(other, Matrix):
			# TODO: Multiplication matricielle.
			# Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (hauteur_A = largeur_B)
			# C = Matrice(hauteur_A, largeur_B)
			# Pour i dans [0, hauteur_C[
				# Pour j dans [0, largeur_C[
					# Pour k dans [0, largeur_A[
						# C(i, j) = A(i, k) * B(k, j)
			C = Matrix(self.height, other.width)
			print(C)
			for i in range(0, C.height):
				for j in range(0, C.width):
					for k in range(0, other.height):
						C[i, j] += self[i, k] * other[k, j]

			return C
		elif isinstance(other, numbers.Number):
			# TODO: Multiplication scalaire.
			return Matrix(self.width, self.height, [other * i for i in self.data])
		else:
			raise TypeError()

	# TODO: Multiplication scalaire avec le scalaire à gauche

	def __abs__(self):
		return Matrix(self.height, self.width, [abs(e) for e in self.data])

	# TODO: Égalité entre deux matrices
	def __eq__(self, other) -> bool:
		return (self.data == other.data and self.has_same_dimensions(other))

	@classmethod
	def identity(cls, width):
		result = cls(width, width)
		for i in range(width):
			result[i, i] = 1.0
		return result

