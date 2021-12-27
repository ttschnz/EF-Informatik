from neuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import numpy as np

# def showImage(index):
#     imgArr = np.asfarray(trainSet[index][1:]).reshape(28,28)
#     print(trainSet[index][0])
#     plt.imshow(imgArr, cmap="Greys")

def dataPreparation():
    with open("D:/Ausbildung/2.1_Gymer/G4/Informatik/Jupyter/Notebooks/mnist_train_100.csv", "r") as f:
        trainSet = [i.split(",") for i in  f.read().split("\n")]
        
    with open("D:/Ausbildung/2.1_Gymer/G4/Informatik/Jupyter/Notebooks/mnist_test_10.csv", "r") as f:
        testSet = [i.split(",") for i in f.read().split("\n")]

    trainData = []
    for i in range(len(trainSet)-1): # -1 because last one is ""
        trainData.append([None, None])
        trainData[i][0] = np.array(list(map(int, trainSet[i][1:])))
        trainData[i][1] = np.zeros(outputNodeCount)
        trainData[i][1][int(trainSet[i][0])] = 1
    
    testData = []
    for i in range(len(testSet)-1): # -1 because last one is ""
        testData.append([None, None])
        testData[i][0] = np.array(list(map(int, testSet[i][1:])))
        testData[i][1] = np.zeros(outputNodeCount)
        testData[i][1][int(testSet[i][0])] = 1

    return trainData, testData

outputNodeCount = 10
hiddenNodeCount = 200
learningRate = .3

trainData, testData = dataPreparation()

nn = NeuralNetwork(len(trainData[0][0]),hiddenNodeCount, outputNodeCount, learningRate)
# nn.load("100000.pkl")
print("score without training:",nn.testSet(testData))
print("training")
nn.trainWithSet(trainData, 10000)
nn.save("a.pkl")
print("done, testing")
print("score with training:",nn.testSet(testData))
input("press enter to display weight layers")
print(nn.weightMatrixIn_Hidden)
print(nn.weightMatrixHidden_Out)