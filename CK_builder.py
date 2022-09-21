import pygame
import pickle
from random import randrange
import numpy as np

pygame.init()

screen = pygame.display.set_mode([448,448])

screen.fill([0,0,0])

boolean = True
draw = False
first = True

counter = 1

tra_d = []
tes_d = []
localList = []

def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


while boolean:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_q:
                boolean = False
            elif event.key == pygame.K_c:
                screen.fill([0,0,0])
                pygame.display.flip()         
            elif event.key == pygame.K_g:
                randNum = randrange(10)
                print(counter)
                print(randNum)
                counter+=1
                     
            elif event.key == pygame.K_s:
                pxarray = pygame.PixelArray(screen)
                convArr = [[0]*448 for k in range(448)]
                for i in range(len(pxarray)):
                    for j in range(len(pxarray[i])):
                        convArr[i][j] = (((screen.unmap_rgb(pxarray[i][j]))[0])/255)
                #Averaging program - very inefficient
                tempSum = 0
                convArrFinal = [[0]*28 for m in range(28)]
                for a in range (0,28,1):
                    for b in range(0,28,1):
                        for c in range(0,16,1):
                            for d in range(0,16,1):
                                tempSum += convArr[c+(a*16)][d+(b*16)]
                        convArrFinal[a][b] = (tempSum / 256)
                        tempSum = 0

                tempDraw = np.array(convArrFinal).reshape(784,1)
                try:
                    if(first):
                        tempTuple = tuple([tempDraw,vectorized_result(randNum)])
                    else:
                        tempTuple = tuple([tempDraw, randNum])

                    localList.append(tempTuple)
                    screen.fill([0,0,0])
                    pygame.display.flip()
                except:
                    pass

            elif event.key == pygame.K_r:

                tra_d.extend(localList)
                localList = []
                first = False

            elif event.key == pygame.K_e:
                tes_d.extend(localList)
                localList = []
            
            elif event.key == pygame.K_f:
                finalTuple = tuple([tra_d, tes_d])
                dataFile = open('data.pickle','wb')
                pickle.dump(finalTuple, dataFile)
                dataFile.close()
                boolean = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if draw:
            pygame.draw.circle(screen, [254,254,254], pygame.mouse.get_pos(), 20)  
            pygame.display.flip()

pygame.quit()