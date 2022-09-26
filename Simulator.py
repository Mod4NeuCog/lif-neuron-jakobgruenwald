import sys
import numpy as np

# without IO: it just assigns the initial membrane potential to the
# membrane potential, but doesn't return anything
class Neuron1:
    def __init__(self):
        self.initial_membrane_potential = -55
        self.membrane_potential = np.NaN
        self.threshold = -65

    def main(self):
        self.membrane_potential = self.initial_membrane_potential
        print("Nothing to see here.")


myNeuron = Neuron1()
myNeuron.main()


# with IO: to the membrane potential is assigned the sum of the
#       initial membrane potential and the predefined input current.
#       Then the membrane potential is produced as output
class Neuron2:
    def __init__(self):
        self.initial_membrane_potential = -55
        self.membrane_potential = np.NaN
        self.threshold = -65
        self.input = -15

    def main(self):
        self.membrane_potential = self.initial_membrane_potential + self.input

        return self.membrane_potential


myNeuron = Neuron2()
result = myNeuron.main()
print(result)


# with IO and spike: as before, but gives also a Boolean output saying,
#          whether a spike was present of not
class Neuron3:
    def __init__(self):
        self.initial_membrane_potential = -55
        self.membrane_potential = np.NaN
        self.threshold = -65
        self.input = -15

    def main(self):
        self.membrane_potential = self.initial_membrane_potential + self.input

        if self.membrane_potential <= self.threshold:
            spike = True
        else:
            spike = False

        return (self.membrane_potential, spike)


myNeuron = Neuron3()
result = myNeuron.main()
print(result)

# with console input: same as before, but the input is defined by the
#       user through a console input
class Neuron4:
    def __init__(self):
        self.initial_membrane_potential = -55
        self.membrane_potential = np.NaN
        self.threshold = -65
        self.input = np.NaN

    def main(self):
        self.input = float(input('Enter your input current (in mV):'))
        self.membrane_potential = self.initial_membrane_potential + self.input

        if self.membrane_potential <= self.threshold:
            spike = True
        else:
            spike = False

        return self.membrane_potential, spike


myNeuron = Neuron4()
result = myNeuron.main()
print(result)














