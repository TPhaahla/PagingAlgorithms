# Author: Tshiamo Phaahla 
# Student Number: PHHTSH006
# Title: CSC3002F OS Assignment 1 - Paging Algorithms

import sys

def FIFO(size, pages):
    frames = size
    faults = 0
    last = 0
    allocation = []

    print("\n====================================================================================")
    print("Starting FIF0 paging algorithm...")
    print(f"Number of Frames: {frames}\tReference String: {pages}")
    # print("====================================================================================\n")
    print()
    print("Step Number\tAllocation\tCumulative Faults")
    for i in range(len(pages)):
        print(i, end="\t\t")
        if(pages[i] not in allocation):
            if(len(allocation)<frames):
                allocation.append(pages[i])
                faults+=1
                if(i<2):
                    print(allocation, end="\t\t")
                else:
                    print(allocation, end="\t")
                print(faults, end="\t")
                # print()
                
            else:
                allocation[last%frames]=pages[i]
                print(allocation, end="\t")
                faults+=1
                print(faults, end="\t")
                last+=1
        print()
    print("====================================================================================\n")
        # print(allocation)
    return faults

def LRU(size, pages):

    frames = size
    faults = 0
    allocation = []
    print("\n====================================================================================")
    print("Starting FIF0 paging algorithm...")
    print(f"Number of Frames: {frames}\tReference String: {pages}")
    # print(f"Length")
    for i in range(len(pages)):
        if(len(allocation)<frames):
            reset = False
            # print(len(allocation))
            for k in range(len(allocation)):
                # print(len(allocation))
                if(pages[i] == allocation[k][0]):
                    allocation[k][1] = 0
                    reset = True
                    # print(allocation)
                else:
                    allocation[k][1] -=1
                    # print(allocation)
                if reset and k==len(allocation)-1: break
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
                        leastUsed = allocation[k][1]
                        # print(f"Least Used: {leastUsed}")
                        # print(f"Least Position: {leastPos}")
                   
                allocation[leastPos][0] = pages[i]
                allocation[leastPos][1] = 0 
                faults+=1

            # for x in allocation:
            #     print(x[0], end=" ")
            # print()
            # print(allocation)
    return faults

done = False

def OPT(size, pages):

    frames = size
    faults = 0
    allocation = []
    global done
    for i in range(len(pages)):

        # if len(allocation)==frames and not done:
        #     # print("!!!!!!!!!! All Frames in Page Table Are Now Filled. Time To Use The Optimal Page Replacement Algorithm !!!!!!!!!!\n")
        #     # print("=====================================================\n")
        #     done = True

        # print(f"Iteration: {i}\tReference: {pages[i]}\tAllocation: {allocation}")
        if i==0:
            faults+=1
            try:
                allocation.append([pages[i], pages[i+1::].index(pages[i])+i+1])
            except ValueError:
                allocation.append([pages[i], -1])
            # print(f"Adding page {pages[i]} to Frame and Recording Fault Number {faults}")
            # print(f"Current Allocation: {allocation}\n=====================================================\n")
            # faults+=1
            # print(allocation)
            continue

        

        if(len(allocation)<frames):
            reset = False
            for k in range(len(allocation)):
                if(pages[i]==allocation[k][0]):
                    # print(f"Page {pages[i]} already exists in memory.")
                    reset = True
                # try:
                #     allocation[k][1] = pages[i+1::].index(allocation[k][0]) + i + 1
                #     print(f"Updating Allocated Page Next Occurance Distances: {allocation}")
                # except ValueError:
                #     allocation[k][1] = -1
                #     print(f"Updating Allocated Page Next Occurance Distances: {allocation}")
                # print(allocation)
                if reset and k==len(allocation)-1: break
            else:
                try:
                    allocation.append([pages[i],pages[i+1::].index(pages[i])+i+1])
                    faults +=1
                    # print(f"Adding page {pages[i]} to Frame with it's Next Occurence Index and Recording Fault Number {faults}")
                    # print(f"Current Allocation: {allocation}\n=====================================================\n")
                except ValueError:
                    allocation.append([pages[i],-1])
                    faults+=1
                    # print(f"Adding page {pages[i]} to Frame and Recording Fault Number {faults}")
                    # print(f"Current Allocation: {allocation}\n=====================================================\n")

        # print(allocation)
        else:

            currentFurthest = allocation[0][1]
            nextFurthestPosition = 0
            found = False

            for k in range(len(allocation)):

                if(pages[i] == allocation[k][0]):
                    found = True
                    # print(f"Page {pages[i]} is already in our allocation. No faults recorded.")
                    # print(f"Fault Count: {faults}")
                    # print(f"Updating Next Occurence Index for {pages[i]}")
                    try:
                        # print(f"Updating Next Occurance Index for {allocation[k][0]} from {allocation[k][1]} to", end=" ")
                        allocation[k][1] = pages[i+1::].index(allocation[k][0]) + i + 1
                        # print(f"{allocation[k][1]}")
                        # print(f"Current Allocation: {allocation} \n=====================================================\n")
                        # print(f"Updating Allocated Page Next Occurance Distance For {allocation[k][0]}")
                    except ValueError:
                        # print(f"Page {allocation[k][0]} no longer appears in the reference string so we set index to -1")
                        allocation[k][1] = -1
                        # print(f"Current Allocation: {allocation} \n=====================================================\n")

                # # print(allocation)
                # print(f"Updating Allocated Page Next Occurance Distances: {allocation}")

               
                
            if not found:
                # print(f"Page {pages[i]} is not in our allocation. We Will Record a Fault and Update The Allocation Accordingly.")
                for k in range(len(allocation)):
                    # print(f"k={k}")
                    if allocation[k][1] == -1:
                        # print(f"Page {allocation[k][0]} does not appear again in the reference so we can replace it.")
                        nextFurthestPosition = k
                        currentFurthest = allocation[k][1]
                        break

                    elif allocation[k][1] >= currentFurthest:
                        # print(f"Update: Page {allocation[k][0]} is the furthest to be used next in our allocation so we can replace it.")
                        nextFurthestPosition = k
                        currentFurthest = allocation[k][1]

                faults +=1
                # print(f"Replacing Page {allocation[nextFurthestPosition][0]} with Page {pages[i]} and Recording Fault Number {faults}.")
                
                allocation[nextFurthestPosition][0] = pages[i]
                
                try:

                    # print(f"Updating Next Occurance Index for {allocation[k][0]} from {allocation[k][1]} to", end=" ")
                    allocation[nextFurthestPosition][1] = pages[i+1::].index(pages[i]) + i + 1
                    # print(f"{allocation[k][1]}")
                    # faults+=1
                except ValueError:
                    # print(f"Page {allocation[k][0]} no longer appears in the reference string so we set index to -1")
                    allocation[nextFurthestPosition][1] = -1
                    # faults+=1


                # print(f"Current Allocation: {allocation}\n=====================================================\n")
                

    return faults

def main():

    # pages = None
    # pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    
    # pages = [7,0,1,2,0,3,0,4,2,3,0,3,1,2,0]
    pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
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