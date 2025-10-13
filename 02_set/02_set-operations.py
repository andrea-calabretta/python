myset = set()
myset2 = set([])
s1 = set(['a','b','c'])
s2 = set(['c','d','e', 'f'])
print(s1 | s2)      # UNIONE --> {'c', 'b', 'f', 'a', 'e', 'd'}
print(s1 - s2)      # SOTTRAZIONE  {'b', 'a'}
print(s1 & s2)      # INTERSEZIONE {'c'}
print(s1 ^ s2)      # xor ovvero la negazione della differenza  {'b', 'e', 'd', 'f', 'a'}
