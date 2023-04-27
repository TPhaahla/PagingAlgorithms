# Author: Tshiamo Phaahla 
# Student Number: PHHTSH006
# Title: CSC3002F OS Assignment 1 - Paging Algorithms

import sys
import random

def FIFO(size, pages):
    """
        Simulation of the First In First Out (FIF0) page replacement algorithm.
        Output: Number of Page Faults
        Arguments:
            - size: Number of page frames in memory
            - pages: Page string reference as an array
    """

    # Initialise values for the function
    frames = size
    faults = 0
    last = 0
    allocation = []

    for i in range(len(pages)):
        if(pages[i] not in allocation):
            if(len(allocation)<frames): # Add page to memory
                allocation.append(pages[i])
                faults+=1
            else: # Replace page in memory
                allocation[last%frames]=pages[i]
                faults+=1
                last+=1
    return faults

def LRU(size, pages):
    """
        Simulation of the Least Recently Used (LRU) page replacement algorithm.
        Output: Number of Page Faults
        Arguments:
            - size: Number of page frames in memory
            - pages: Page string reference as an array
    """

    # Initialise values for the function
    frames = size
    faults = 0
    allocation = [[None,0], [None,0], [None,0]]
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
            else: # Add pages to memory
                allocation.append([pages[i],0])
                faults+=1
                       
        else: 
            leastUsed = allocation[0][1]    
            leastPos = 0
            found = False  

            for k in range(len(allocation)):
                # Update usage counter if necessary for pages used
                if(pages[i] == allocation[k][0]):
                    allocation[k][1] = 0
                    found = True
                else:
                    allocation[k][1] -=1
            
            if not found:
                # Replace pages in memory with lowest used value counter
                for k in range(len(allocation)):
                    if allocation[k][1]<leastUsed:
                        leastPos = k
                        leastUsed = allocation[k][1]
                   
                allocation[leastPos][0] = pages[i]
                allocation[leastPos][1] = 0 
                faults+=1

    return faults

def OPT(size, pages):
    """
        Simulation of the Optimal (OPT) page replacement algorithm.
        Output: Number of Page Faults
        Arguments:
            - size: Number of page frames in memory
            - pages: Page string reference as an array
    """

    # Initialise values for the function
    frames = size
    faults = 0
    allocation = []

    for i in range(len(pages)):
        if i==0: # Handle First Page Separately
            # Add page to memory as a 2D array with a counter for when it appears next in the reference string.
            try:
                allocation.append([pages[i], pages[i+1::].index(pages[i])+i+1])
            except ValueError:
                allocation.append([pages[i], -1]) # Case when page is never used again, the counter value will be -1
            faults+=1
            continue

        if(len(allocation)<frames): # Case for if all frames in memory have not been used
            reset = False # Flag to keep track of if a page is already in memory
            for k in range(len(allocation)):
                if(pages[i]==allocation[k][0]):
                    reset = True
                if reset and k==len(allocation)-1: break
            else: # Add page to memory
                try:
                    allocation.append([pages[i],pages[i+1::].index(pages[i])+i+1])
                    faults +=1
                except ValueError:
                    allocation.append([pages[i],-1])
                    faults+=1
        else: # Case for replacement of pages in memory needed instead of addition of pages in memory

            # Initialise variables for managing replacement
            currentFurthest = allocation[0][1]
            nextFurthestPosition = 0
            found = False # Flag for if page already exists in memory

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

def generate_pages():

    page_numbers = [0,1,2,3,4,5,6,7,8,9] # Possible page values
    # pages = [8,5,6,2,5,3,5,4,2,3,5,3,2,6,2,5,6,8,5,6,2,3,4,2,1,3,7,5,4,3,1,5]
    pageString=[] # Initialise empty array to store randomly generaated page string
    length_page_string = [8,16,32,64,128]#,256] # array of different page string lengths to be used for testing

    # create random page string by randomly choosing from the possible page numbers
    for i in range(length_page_string[-1]):
        page = random.choice(page_numbers)
        pageString.append(page)

    refStringLength = random.choice(length_page_string) # Length of the randomly generated reference string to use
    pages=pageString[0:refStringLength:] # truncated page refernce string using random length between 8 and 512
    
    return {
        "full_page_string": pageString,
        "truncated_pages": pages
    }

def main(pages,size):
    
    if(pages and size):
        pages = str(pages)
        generated_pages = []
        for i in range(len(pages)):
            generated_pages.append(pages[i])
        size = int(size)
    else:
        generated_pages = generate_pages()
        pages = generated_pages["truncated_pages"]
        size = int(sys.argv[2])

    # Output informing user of algorithm inputs and number of faults recorded for the relevant input
    print("---")
    print(f"Number of Frames: {size}")
    print(f"Page Reference Length: {len(pages)}")
    print(f"Page Reference String: {pages}")
    print("---")
    print(f'FIFO, {FIFO(size, pages)}, page faults.')
    print(f'LRU, {LRU(size, pages)}, page faults.')
    print(f'OPT, {OPT(size, pages)}, page faults.')


def algorithm_test_results():

    print("\n")

    generated_pages = generate_pages()
    page_string_length = [8,16,32,64,128]
 
    ref_str=''
    for i in generated_pages["full_page_string"]:
        ref_str+=str(i)
    
    print("-".rjust(57,"-"))
    print(f"Page String:\n{ref_str}".center(62," "))


    for j in range(7):
        frame_size=j+1
        # print(j)
        print("-".rjust(57,"-"))
        print("|",end="")
        print("Number of Pages".center(20," "), end="|")
        for i in page_string_length:
            print(str(i).center(6," "), end="|")
        print()

        print("-".rjust(57,"-"))
        print("|",end="")
        print(f"Number of Frames: {frame_size}".center(55," "), end="|")
        print()

        print("-".rjust(57,"-"))
        print("|",end="")
        print("FIFO".center(20," "), end="|")
        for i in page_string_length:
            print(str(FIFO(frame_size,generated_pages["full_page_string"][0:i])).center(6," "), end="|")
        print()

        print("-".rjust(57,"-"))
        print("|",end="")
        print("LRU".center(20," "), end="|")
        for i in page_string_length:
            print(str(LRU(frame_size,generated_pages["full_page_string"][0:i])).center(6," "), end="|")
        print()
        
        print("-".rjust(57,"-"))
        print("|",end="")
        print("OPT".center(20," "), end="|")
        for i in page_string_length:
            print(str(OPT(frame_size,generated_pages["full_page_string"][0:i])).center(6," "), end="|")
        print()
        print("-".rjust(57,"-"))
        
    print("\n")


    

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        error = False
        command = sys.argv[1]

        if (command=='-p'):
            if sys.argv[2].isdigit():
                main(None,None)
            else:
                error = True

        elif (command=='-t'):
            algorithm_test_results()

        elif (command=='-s'):
            if(len(sys.argv)==5):
                if(sys.argv[2].isdigit()) and (sys.argv[4].isdigit()):
                    page_string = sys.argv[2]
                    if (sys.argv[3]=='-f'):
                        frame_size = sys.argv[4]
                        main(page_string,frame_size)
                    else:
                        print('Invalid Command')
                        error = True
                else:
                    print('Error, page string and page size must be only numbers with no spaces')
                    error = True
                
            else:
                error = True        
       
else:
        print('Usage: python paging.py -p [number of pages]\n')
        print('Usage: python paging.py -t\n')
        print('Usage: python paging.py -s [page string] -f [page size]')
        
