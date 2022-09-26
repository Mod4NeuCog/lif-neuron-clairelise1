# Algorithm of 1 Neuron

# Without IO 
init=-75
final= -50
print("The neuron at rest is", init)
print("The neuron when spiking is", final)
# Now with IO and with Output Spike
def Neuron():
    
    V_membrane= -75
    V_threshold= -50
    i= input("provide an input")
    print("The input is",i)
    V_membrane= int(i) + V_membrane
    print("Now the mebrane is",V_membrane)
    if V_membrane > V_threshold:
        print("Spike")
        return 1
    else:
        return 0

ret=Neuron()
print(ret)