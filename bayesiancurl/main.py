from bayesian import *
from node import *

A = Node("A")
B = Node("B")
B.add_parent(A)

# Darle la probabilidad de que sea verdadero
A.create_probs(0.5)

# Dado Aa -> valores de B -> cuando es true dado a true y a dado false
B.create_probs_son(0.3, 0.7)
