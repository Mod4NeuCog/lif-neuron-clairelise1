import numpy as np


class Neuron:
    def __init__(self):
        self.V_th= -65
        self.V_rest= -75
        self.tau_m= 5
        self.g_L= 10
        self.V_init= -75
        self.E_L= -75
        self.V = np.zeros(1000)
        self.V[0]=self.V_init
        self.V.shape
        self.I=200
        self.dt=0.1
        
    def updateMembranePotential(self):
        for k in range(1,1000):
            dV=(-(self.V[k-1]-self.V_rest)+self.I/self.g_L)/self.tau_m
            if self.V[k-1]>= self.V_th:
                self.V[k]=self.V_init
                print(f"Spiked at {k}")
            else:
                self.V[k]=self.V[k-1]+(self.dt*dV)
                
n = Neuron()
network= [0,0,0]
n.updateMembranePotential()
