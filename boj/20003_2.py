import math

n=int(input())

moms=[]
sons=[]

for i in range(n):
    son, mother = map(int, input().split())
    moms.append(mother)
    sons.append(son)

all_mom = math.lcm(*moms)

new_sons=[]
for son, mom in zip(sons, moms):
    new_sons.append(son * (all_mom // mom))

sons_gcd=math.gcd(*new_sons)
ans_son=sons_gcd//math.gcd(all_mom,sons_gcd)
ans_mom=all_mom//math.gcd(all_mom,sons_gcd)

print(ans_son, ans_mom)