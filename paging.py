# Author: Tshiamo Phaahla 
# Student Number: PHHTSH006
# Title: CSC3002F OS Assignment 1 - Paging Algorithms

import sys

def FIFO(size, pages):
    frames = size
    faults = 0
    last = 0
    allocation = []

    for i in range(len(pages)):
        if(pages[i] not in allocation):
            if(len(allocation)<frames):
                allocation.append(pages[i])
                faults+=1
            else:
                allocation[last%frames]=pages[i]
                faults+=1
                last+=1
    return faults

def LRU(size, pages):

    frames = size
    faults = 0
    allocation = []
    for i in range(len(pages)):
        if(len(allocation)<frames):
            reset = False
            for k in range(len(allocation)):
                if(pages[i] == allocation[k][0]):
                    allocation[k][1] = 0
                    reset = True
                else:
                    allocation[k][1] -=1
                if reset and k==len(allocation)-1: break
            else:
                allocation.append([pages[i],0])
                faults+=1
                

                
        else: 
            leastUsed = allocation[0][1]    
            leastPos = 0
            found = False  

            for k in range(len(allocation)):
                if(pages[i] == allocation[k][0]):
                    allocation[k][1] = 0
                    found = True
                else:
                    allocation[k][1] -=1
            
            if not found:
                for k in range(len(allocation)):
                    if allocation[k][1]<leastUsed:
                        leastPos = k
                        leastUsed = allocation[k][1]
                   
                allocation[leastPos][0] = pages[i]
                allocation[leastPos][1] = 0 
                faults+=1

    return faults

done = False

def OPT(size, pages):

    frames = size
    faults = 0
    allocation = []
    global done
    for i in range(len(pages)):

       
        if i==0:
            try:
                allocation.append([pages[i], pages[i+1::].index(pages[i])+i+1])
            except ValueError:
                allocation.append([pages[i], -1])
            faults+=1
            continue

        if(len(allocation)<frames):
            reset = False
            for k in range(len(allocation)):
                if(pages[i]==allocation[k][0]):
                    reset = True
                if reset and k==len(allocation)-1: break
            else:
                try:
                    allocation.append([pages[i],pages[i+1::].index(pages[i])+i+1])
                    faults +=1
                except ValueError:
                    allocation.append([pages[i],-1])
                    faults+=1
        else:
            currentFurthest = allocation[0][1]
            nextFurthestPosition = 0
            found = False

            for k in range(len(allocation)):
                if(pages[i] == allocation[k][0]):
                    found = True
                    try:
                        allocation[k][1] = pages[i+1::].index(allocation[k][0]) + i + 1
                    except ValueError:
                        allocation[k][1] = -1
    
            if not found:
                for k in range(len(allocation)):
                    if allocation[k][1] == -1:
                        nextFurthestPosition = k
                        currentFurthest = allocation[k][1]
                        break
                    elif allocation[k][1] >= currentFurthest:
                        nextFurthestPosition = k
                        currentFurthest = allocation[k][1]

                faults +=1
                allocation[nextFurthestPosition][0] = pages[i]
                try:
                    allocation[nextFurthestPosition][1] = pages[i+1::].index(pages[i]) + i + 1
                except ValueError:
                    allocation[nextFurthestPosition][1] = -1
    return faults

def main():
    # pages = None
    pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    # pages = [7,0,1,2,0,3,0,4,2,3,0,3,1,2,0]
    # pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
    # pages = [1,2,3,4,1,2,5,1,2,3,4,5]

    size = int(sys.argv[1])
    print(f'FIFO, {FIFO(size, pages)}, page faults.')
    print(f'LRU, {LRU(size, pages)}, page faults.')
    print(f'OPT, {OPT(size, pages)}, page faults.')

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print('Usage: python paging.py [number of pages]')
    else:
        main()