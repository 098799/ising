from random import randrange, randint, random
from operator import xor
from math import exp
from sys import argv

#Define the size of the array n:
n = int(argv[2])

#Check the temperature t for easy usage in bash:
t = float(argv[1])

#Define how many big steps do you want in the calculations:
st=1000

#How many small steps in a big step?
small=n**2

table = [[randrange(-1,2,2) for x in range(n)] for y in range(n)]

def prob(dE,t):
    "Probability of rejecting positive energy change"
    return 1-exp(-dE/t)

def en(i,j,ip,jp):
    "Checks energy between table[i][j] and table[ip,jp]"
    return abs(table[i][j]+table[ip][jp])-1

def energy():
    "Calculates the energy of Ising model in tabela. Periodic boundary conditions are applied."
    energy = 0
    for j in range(n):
        for i in range(n):
            energy = energy + en(i,j,(i+1)%n,j) + en(j,i,j,(i+1)%n)
    return energy

def enchk(i,j):
    "Checks whether the energy of the system in <<tabela>> increases when <<i>>th place is changed"
    return en(i,j,(i+1)%n,j)+en(i,j,(i-1)%n,j)+en(i,j,i,(j+1)%n)+en(i,j,i,(j-1)%n)

for step in range(st):
    for i in range(small):
        spoti = randint(0,n-1)
        spotj = randint(0,n-1)
        temp = enchk(spoti,spotj)
        table[spoti][spotj] = table[spoti][spotj]*(-1)
        if enchk(spoti,spotj) > temp:
            if random() < prob(enchk(spoti,spotj),t):
                table[spoti][spotj] = table[spoti][spotj]*(-1)
    print(energy())
