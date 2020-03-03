# her ætla eg ad glosa ur stat fyrir ingeniora fra NTNU 2020
import math

# mengden S er utfallsrommet, holder alle mulige utfall motsatt ved Ø som er tom
# mengden A er dermed Ø < = A < = S


# set with of die faces 1 to 6
die = set((1, 2, 3, 4, 5, 6))
otherdie = set((1, 2, 3, 4, 5, 6))
partal = set((2, 4, 6))

# difference()	Returns a set containing the difference between two or more sets
# vissara ad hafa stærra mengid a undan til ad athuga hvort thau eru eins
diff = partal.difference(otherdie)
# print(diff)

# gjensidig utelukkende, gjensidig eksluderende eller disjunkte mutullu exclusive
# er når snittmengden er tom A snitt B = Ø
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)

A = set((1, 2, 3))
B = set((3, 4))
# print(A.intersection(B))

# union
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
A = set((1, 7, 8))
B = set((7, 9))
# print(A.union(B))


# mengdedifference A\B << A minus B >> Det som er i A men ikke i B
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
A = set((7, 9))
B = set((1, 7, 8))
# print(A.difference(B))

# komplementmengde (not A) S\A x is in S: x is not in A
# A\B = A\(A snitt B) = A snitt notB
# A\S = Ø   A\Ø = A
# S = set((1, 3, 6))
# A = set((1, 3))

# oppgave 1.3
S = set((1, 2, 3, 4, 5, 6))
A = set((1, 3, 5))
B = set((2, 3, 5))

notA = S.difference(A)
notB = S.difference(B)

notA_snitt_notB = notA.intersection(notB)
notA_union_notB = notA.union(notB)

not_A_snitt_B = S.difference(A.intersection(B))
not_A_union_B = S.difference(A.union(B))

statement = not_A_snitt_B.difference(notA_snitt_notB)
statement2 = not_A_snitt_B.difference(notA_union_notB)
statement3 = not_A_union_B.difference(notA_union_notB)

# isdisjoint()	Returns whether two sets have a intersection or not
# isdisjoint = mutually exclusive

# issubset()	Returns whether another set contains this set or not

# issuperset()	Returns whether this set contains another set or not

# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another

S = {1, 2, 3, 4, 5, 6}
A = {1, 3, 4}
B = {2, 3, 5}
C = {2, 5, 6}
D = {1, 3, 4}


# print(A.symmetric_difference(B))

# print(A.union(B))

# FAKULTET
# for eksample 5! = 5*4*3*2*1 = 120

# print(math.factorial(5))

# BINOMIALKOEFFISIENTER (n over k)

def myBinom(n, k):
    diff = n - k
    return math.factorial(n) / (math.factorial(k) * math.factorial(diff))
#print(13 * 12 * myBinom(13, 2) * math.factorial(11))

# Addisjonregelen   P(A1 union A2 union A3 ..... = P(A1) + P(A2)...
# Subtraksjonregelen P(A\B) = P(A) - P(A snitt B)
# A = (A\B) + P(A snitt B)  gjensidig utelukkende => P(A) = P(A\B) + P(A snitt B)



