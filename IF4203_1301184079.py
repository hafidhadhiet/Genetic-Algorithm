import random
import math
import functools
import time

# Fungsi untuk membangkitkan individu yang terdiri dari x1 dan x2
def individual(minX1, maxX1, minX2, maxX2):
    x1 = random.randint(minX1, maxX1)
    x2 = random.randint(minX2, maxX2)
    return [x1, x2]

# Fungsi untuk membangkitkan populasi yang terdiri dari 'count' individu
def population(count, minX1, maxX1, minX2, maxX2):
    return [individual(minX1, maxX1, minX2, maxX2) for x in range(count)]

# Fungsi untuk menghitung nilai fitness per individu
def individualFitness(individual):
    b = 10
    x1 = individual[0]
    x2 = individual[1]
    h = (math.cos(x1)*math.sin(x2))-(x1/((x2*x2)+1))
    return b-h;

# Fungsi untuk melakukan proses mutasi secara random
def mutation(sisaPop):
    peluangMutasi = 0.9
    n = 0
    for i in sisaPop:
        r = random.random()
        if peluangMutasi > r:
            ubahAngka = random.randint(0,len(i)-1)
            if ubahAngka == 0:
                i[ubahAngka] = random.randint(-1, 2)
            elif ubahAngka == 1:
                i[ubahAngka] = random.randint(-1, 1)
        sisaPop[n] = i
        n = n + 1
    return sisaPop

# Fungsi untuk menghitung nilai fitness per individu pada suatu populasi
def fitnessPerIndividu(pop):
    hasil = []
    i = 0
    while i<len(pop):
        hasil.append([individualFitness(pop[i]), pop[i]])
        i = i+1
    return hasil

# Fungsi untuk mengurutkan individu dalam suatu populasi secara ascending berdasarkan nilai fitnessnya
def urutkanFitnessPerIndividu(pop):
    hasil = [x[1] for x in sorted(pop)]
    return hasil

# Fungsi untuk menseleksi parent berdasarkan fitness terbaik
# Variabel retain untuk menentukan berapa persen parent terbaik yang akan dipertahankan
def tournamentSelection(pop, retain):
    pop.reverse()
    parents = pop[:retain]
    sisa = pop[retain:]
    seleksi = [parents, sisa]
    return seleksi

# Fungsi untuk melakukan crossover
def crossover(sisaPop):
    sisaPopLength = len(sisaPop)
    children = []
    while len(children) < sisaPopLength:
        maleNumber = random.randint(0, sisaPopLength-1)
        femaleNumber = random.randint(0, sisaPopLength-1)
        if maleNumber != femaleNumber:
            male = sisaPop[maleNumber]
            female = sisaPop[femaleNumber]
            half = round(len(male)/2)
            child = male[:half] + female[half:]
            children.append(child)
    return children
        
def evolve(ga):
    retain = 1
    fitnessIndividu = fitnessPerIndividu(ga)
    urutkan = urutkanFitnessPerIndividu(fitnessIndividu)
    seleksi = tournamentSelection(urutkan, retain)
    persilangan = crossover(seleksi[1])
    mutasi = mutation(persilangan)
    newPop = seleksi[0] + mutasi
    return newPop

# Coba secara keseluruhan
cekStagnan = [True, 0, 0]
generasi = 1
populasi = population(3, -1, 2, 1, 2)
minLokal = 0
cekStagnan[1] = minLokal
print(fitnessPerIndividu(populasi))
# print(populasi)

while (generasi <= 10000) and (cekStagnan[0]):
    populasi = evolve(populasi)
    minLokal = individualFitness(populasi[0])
    if minLokal == cekStagnan[1]:
        cekStagnan[2] = cekStagnan[2] + 1
        if cekStagnan[2] >= 50:
            cekStagnan[0] = False
    else:
        cekStagnan[1] = minLokal
        cekStagnan[2] = 0
    generasi = generasi + 1

# print(populasi)
print('Banyaknya generasi = ',generasi)
print('fitness terbaik = ', individualFitness(populasi[0]))
individu = populasi[0]
x1 = individu[0]
x2 = individu[1]
minimal = (math.cos(x1)*math.sin(x2))-(x1/((x2*x2)+1))
print ('nilai minimum', minimal)
print('x1 = ',x1,' x2 = ',x2)
