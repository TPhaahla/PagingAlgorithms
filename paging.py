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
        # print(allocation)
    return faults

def LRU(size, pages):

    frames = size
    faults = 0
    allocation = []
    
    for i in range(len(pages)):
        if(len(allocation)<frames):
            for k in range(len(allocation)):
                if(pages[i] == allocation[k][0]):
                    allocation[k][1] = 0
                    # print(allocation)
                else:
                    allocation[k][1] -=1
                    # print(allocation)
            else:
                allocation.append([pages[i],0])
                faults+=1
                # print(allocation)
                # for x in allocation:
                #     print(x[0], end=" ")
                # print()

                
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
                   
                allocation[leastPos][0] = pages[i]
                allocation[leastPos][1] = 0 
                faults+=1

            # for x in allocation:
            #     print(x[0], end=" ")
            # print()
            # print(allocation)
    return faults


def OPT():
    return 

def main():

    # pages = None
    pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    # pages = [7,0,1,2,0,3,0,4,2,3,0,3,1,2,0]


    size = int(sys.argv[1])
    print(f'FIFO, {FIFO(size, pages)}, page faults.')
    print(f'LRU, {LRU(size, pages)}, page faults.')
    # print(f'OPT, {OPT(size, pages)}, page faults.')

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print('Usage: python paging.py [number of pages]')
    else:
        main()