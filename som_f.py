#
import numpy as np
import math
import random
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt


def mapunits(input_len):
    heuristic_map_units = 20*input_len**0.54321
    return heuristic_map_units

#Algoritmo SOM

def som(observations,map_width,map_height,epochs):
    MAP = np.random.uniform(size=(map_height,map_width,len(observations[0])))
    prev_MAP = np.zeros((map_height,map_width,len(observations[0])))

    radius0 = max(map_width,map_height)/2
    learning_rate0 = 0.1

    coordinate_map = np.zeros([map_height,map_width,2],dtype=np.int32)

    for i in range(0,map_height):
        for j in range(0,map_width):
            coordinate_map[i][j] = [i,j]


    radius=radius0
    learning_rate = learning_rate0
    max_iterations = len(observations)+1
    too_many_iterations = 10*max_iterations

    convergence = [1]

    timestep=1
    e=0.001 #determinación de la convergencia
    flag=0 #Cuando es igual a 1 significa que la red llego a un punto estacionario

    epoch=0
    while epoch<epochs:

        shuffle = np.random.randint(len(observations), size=len(observations))
        for i in range(len(observations)):

            # Revisamos si la red ha convergido
            J = np.linalg.norm(MAP - prev_MAP)

            if  J <= e:
                flag=1
                break

            else:

                #if timestep == max_iterations and timestep != too_many_iterations:
                #    epochs += 1
                #    max_iterations = epochs*len(observations)

                observation = observations[shuffle[i]]
                observation_ary = np.tile(observation, (map_height, map_width, 1))
                Eucli_MAP = np.linalg.norm(observation_ary - MAP, axis=2)
                
                BMU = np.unravel_index(np.argmin(Eucli_MAP, axis=None), Eucli_MAP.shape)    

                prev_MAP = np.copy(MAP)

                for i in range(map_height):
                    for j in range(map_width):
                        distance = np.linalg.norm([i - BMU[0], j - BMU[1]])
                        if distance <= radius:
                            #theta = math.exp(-(distance**2)/(2*(radius**2)))
                            MAP[i][j] = MAP[i][j] + learning_rate*(observation-MAP[i][j]) #Agregar un cambio dependiente de la distancia!

                learning_rate = learning_rate0*(1-(epoch/epochs))
                #time_constant = max_iterations/math.log(radius) 
                radius = radius0*math.exp(-epoch/epochs)

                timestep+=1

        if J < min(convergence):
            print('Lower error found: %s' %str(J) + ' at epoch: %s' % str(epoch))
            print('\tLearning rate: ' + str(learning_rate))
            print('\tNeighbourhood radius: ' + str(radius))
            MAP_final = MAP
        convergence.append(J)

        
        if flag==1:
            break
        epoch+=1
    return convergence, J, timestep