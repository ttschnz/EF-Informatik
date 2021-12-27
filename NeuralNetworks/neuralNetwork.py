import numpy as np
import pickle as pkl

from numpy.core.numeric import Infinity
LOGLEVEL = Infinity
class NeuralNetwork:
    def __init__(self, inputNodeCount, hiddenNodeCount, outputNodeCount, alpha):
        self.inputNodeCount = inputNodeCount
        self.hiddenNodeCount = hiddenNodeCount
        self.outputNodeCount = outputNodeCount
        self.alpha = alpha

        self.e_W_h = np.random.normal(0.0, 1/np.sqrt(self.hiddenNodeCount), (self.hiddenNodeCount, self.inputNodeCount))        
        self.h_W_a = np.random.normal(0.0, 1/np.sqrt(self.outputNodeCount), (self.outputNodeCount, self.hiddenNodeCount))
    
    def sigmoid(self, node):
        return 1 / (1 + np.exp(-node))
    
    def trainWithSet(self, dataset, cycleCount):
        for i in range(cycleCount):
            randomSet = dataset[np.random.choice(range(len(dataset)))]
            self.train(randomSet[0], randomSet[1])
            if(i%(cycleCount/100) == 0):
                print(i/cycleCount*100, "% trained")


    def train(self, inputsSchichtE, targets):
        # process from input to hiddenlayer
        inputsSchichtH = np.dot(self.e_W_h, inputsSchichtE)
        outputsSchichtH = self.sigmoid(inputsSchichtH)
        # process from hiddenLayer to outputLayer
        inputsSchichtA = np.dot(self.h_W_a, outputsSchichtH)
        outputsSchichtA = self.sigmoid(inputsSchichtA)
        
        # calculate error
        errorsSchichtA = targets - outputsSchichtA
        errorsSchichtH = np.dot(np.transpose(self.h_W_a), errorsSchichtA)
        
        # adjust e_W_h
        self.e_W_h = (
            self.e_W_h + 
            self.alpha * 
            np.dot(
                errorsSchichtH * 
                outputsSchichtH * 
                (1 - outputsSchichtH), 
                np.transpose(inputsSchichtE)
            )
        )

        # adjust h_W_a
        self.h_W_a = (
            self.h_W_a + 
            self.alpha * 
            np.dot(
                errorsSchichtA * 
                outputsSchichtA * 
                (1 - outputsSchichtA), 
                np.transpose(inputsSchichtH)
            )
        )
        
    def run(self, inputsSchichtE):
        inputsSchichtH = np.dot(self.e_W_h, inputsSchichtE)
        outputsSchichtA = self.sigmoid(inputsSchichtH)
        inputsSchichtA = np.dot(self.h_W_a, outputsSchichtA)
        outputsSchichtH = self.sigmoid(inputsSchichtA)
        return outputsSchichtH
    
    def getIndexOfMax(self, arr, count = 1):
        return np.argpartition(arr, -count)[-count]

    def test(self, inputsSchichtE, targets):
        result = self.getIndexOfMax(self.run(inputsSchichtE)) 
        desiredResult =  self.getIndexOfMax(targets)
        if(LOGLEVEL>6):
            print("testing data {0}, hoping for result {1}, recieved {2}".format(inputsSchichtE, targets, self.run(inputsSchichtE)))
        if(LOGLEVEL>5):
            print("tested data and recieved {0}, desired result is {1}".format(result, desiredResult))
        return int(result == desiredResult)

    def testSet(self, dataset):
        score = [self.test(entry[0], entry[1]) for entry in dataset]
        return score

    def save(self, fileName):
        with open(fileName, "wb") as f:
            pkl.dump(self, f)
        
    def load(self, fileName):
        with open(fileName, "rb") as f:
            self = pkl.load(f)