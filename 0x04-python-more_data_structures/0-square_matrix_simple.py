#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	return  list(map(lambda x: list(map(lambda e: e**2, x)), matrix))
