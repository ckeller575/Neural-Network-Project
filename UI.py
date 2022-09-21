import CK_loader
import network
import pygame
import numpy as np

training_data, test_data = CK_loader.load_data()

net = network.Network([784, 30, 10])
net.SGD(training_data, 100, 10, 3.0, test_data=test_data)

pygame.init()

screen = pygame.display.set_mode([448,448])

screen.fill([0,0,0])

boolean = True
draw = False

while boolean:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_q:
                boolean = False
            elif event.key == pygame.K_c:
                screen.fill([0,0,0])
                pygame.display.flip()                
            elif event.key == pygame.K_p:
                pxarray = pygame.PixelArray(screen)
                convArr = [[0]*448 for k in range(448)]
                for i in range(len(pxarray)):
                    for j in range(len(pxarray[i])):
                        convArr[i][j] = (((screen.unmap_rgb(pxarray[i][j]))[0])/255)
                
                tempSum = 0
                convArrFinal = [[0]*28 for m in range(28)]
                for a in range (0,28,1):
                    for b in range(0,28,1):
                        for c in range(0,16,1):
                            for d in range(0,16,1):
                                tempSum += convArr[c+(a*16)][d+(b*16)]
                        convArrFinal[a][b] = (tempSum / 256)
                        tempSum = 0

               
                print('PREDICTION:')
                print(np.argmax(net.feedforward((np.array(convArrFinal)).reshape(784,1))))
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if draw:
            pygame.draw.circle(screen, [254,254,254], pygame.mouse.get_pos(), 20)  
            pygame.display.flip()

pygame.quit()

