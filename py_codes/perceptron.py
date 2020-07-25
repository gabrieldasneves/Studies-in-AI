from random import *

#função normalizadora
def normalizeValue(val):
    if val<0 :
        return -1
    else:
        return 1

#função que implementa a reta do problema
def lineY(x):
    return 2*x - 3

#função para gerar o conjunto de treinamento
def generateTrainingSet(trainingSize):
    trainingSet = []
    for i in range(trainingSize):
        x = random()
        y = random()
        if y > lineY(x):
            output = 1 # Point above the line
        else:
            output = -1 # Point below the line
        trainingSet.append([x, y, output])
        return trainingSet 

#criando nosso perceptron
class perceptron:

    def __init__(self,inputSize):
        self.inputLayerSize = inputSize
        self.weights =[]
        self.bias = random()

        for i in range(inputSize):
            self.weights.append(self.bias)

    def processInput(self, nnInput):      
        # nnInput é um vetor contendo todos os valores de entrada
        assert len(nnInput) == len(self.weights)
        unprocessedOutputVal = self.bias # inicializando a soma ponderada com o bias
        for i in range(len(nnInput)): # adiciona o resto
            unprocessedOutputVal += nnInput[i]*self.weights[i]

        return normalizeValue(unprocessedOutputVal) # Return the formatted value






    
