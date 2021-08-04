import random

def createPopulation1(n, li, ls):

    lenChromosome = len(bin(ls))

    population = []
    i = 0
    while(i < n):
        population.append(format(random.randint(li, ls), '#0'+str(lenChromosome)+'b').split('b')[1])
        i += 1
    return population

def createPopulation(n, li, ls):

    lenChromosome = len(bin(ls))

    population = []
    i = 0
    while(i < n):
        population.append(format(random.randint(li, ls), '#0'+str(lenChromosome)+'b').split('b')[1])
        i += 1
    return population

def vectorApitidao(population):
    return [square(int(x,2)) for x in population]


def probSelection(aptidao):
    soma = sum(aptidao)
    vectorProb = [x / soma for x in aptidao]
    return vectorProb


def crossover(samples):
    newpopulation = []

    tamanho = len(samples)
    while(tamanho > 1 ):
        elementx = random.randint(0, len(samples)-1)
        x = samples[elementx]
        samples.remove(x)
        elementy = random.randint(0, len(samples)-1)
        y = samples[elementy]
        samples.remove(y)
        tamanho = len(samples)

        if(x != [] and y != []):
            pontierCut = random.randint(0, len(x))

            if(pontierCut != 0 and pontierCut != len(x)):
                newpopulation.append(x[:pontierCut] + y[pontierCut:])
                newpopulation.append(y[:pontierCut] + x[pontierCut:])
            else:
                newpopulation.append(x)
                newpopulation.append(y)

    return newpopulation


def mutation(population, constMutation=1):
    newpopulation = []
    it = iter(population)
    for x in it:
        pontierMutation = random.randint(0, len(x)-1)
        mutation = random.uniform(0,100)

        if(0 < mutation and constMutation >= mutation):
            if(x[pontierMutation] == '1'):
                newpopulation.append(x[:pontierMutation] + '0'+ x[pontierMutation+1:])
            else:
                newpopulation.append(x[:pontierMutation] + '1'+ x[pontierMutation+1:])
        else:
            newpopulation.append(x)

    return newpopulation


def ag(li, ls, n, maxIteration):
    #criar a população
    population = createPopulation(n, li, ls)
    newpopulation = []
    apitidao = vectorApitidao(population)

    maxValue = square(ls)
    g = 0
    while(g < maxIteration and maxValue != max(apitidao)):

        #calcula o vetor de probabilidade de seleção
        vectorProb = probSelection(apitidao)

        #roleta
        samples = random.choices(population, vectorProb, k=n)

        newpopulation = crossover(samples)

        newpopulation = mutation(newpopulation)
        g += 1
        apitidao = vectorApitidao(newpopulation)

    print("população inicial: ")
    [print(x,str(int(x,2))) for x in population]

    if(g == maxIteration):
        print("Não conseguiu convergir para o maximo")
        print("Estado Final da população: ")
        print("numero de iterações: " + str(g))
        [print(x,str(int(x,2))) for x in newpopulation]
    else:
        print("Estado Final da população: ")
        print("numero de iterações: " + str(g))
        [print(x,str(int(x,2))) for x in newpopulation]


def square(x):
    return x**2

def main():
    print("Restrições do problema: ")
    li = int(input("Limite inferior: "))
    ls = int(input("Limite superior: "))
    n = int(input("Informe o número da população: "))

    maxIteration = 100000

    ag(li, ls, n, maxIteration)


if __name__ == '__main__':
   main()
