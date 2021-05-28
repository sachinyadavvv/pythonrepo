# dice problems
from itertools import product

K = 3

temp = [list(range(1, 7)) for _ in range(K)]

res = list(product(*temp))

print("The constructed dice Combinations : " + str(res))
