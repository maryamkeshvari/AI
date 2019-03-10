import numpy as np
class GoToWalkANN:
    def __init__(self,theWeather=1.0,theMood=1.0,theFriends=1.0):
        self.weather=theWeather
        self.mood=theMood
        self.friends=theFriends

    def activationFunctin(self,X):
        if X>=0.5:
            return 1
        else:
            return 0

    def solve(self):
        input=np.array([self.weather,self.mood,self.friends])
        weight1=[0.25,0.4,0.4]
        weight2=[0.5,-0.4,-0.9]
        weight=np.array([weight1,weight2])
        weightsHiddentooutput =np.array([1,1])
        #weightsHiddentooutput =np.array([-1,1])
        hiddeninput=np.dot(weight,input)
        print("hidden input :"+str(hiddeninput))
        hiddenoutput=np.array([self.activationFunctin(x) for x in hiddeninput ])
        print("hidden output:" + str(hiddenoutput))
        output=np.dot(weightsHiddentooutput,hiddenoutput)
        print("output "+str(output))
        return self.activationFunctin(output)
someNeuralNetwork=GoToWalkANN()
print("result " +str(someNeuralNetwork.solve()))