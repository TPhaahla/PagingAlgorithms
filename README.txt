The following code was written by Tshiamo Phaahla as part of the Operting Systems Module of Computer Science course with course code CSC3002F at The University of Cape Town.

Author: Tshiamo Phaahla
Student Number: PHHTSH006

====== Instructions on how to run the following code ======

In the root directory there is a python file named `paging.py`.

This can be run using the following commands:

    ========================
    ## COMMAND 1 - Using a randomly generated page reference string with specified number of page frames in memory.

        - python paging.py -p [page size]
            - [page size] refers to the number of page frames allocated in order to simulate the page replacement algorithms and count the number of page faults.

            - output format for [page size] = 3:
                - Note that the output will include the randomly generated page reference string used for the output. 
                    Each run will use a different page reference string of different lengths. 

                >   ---
                    Number of Frames: 3
                    Page Reference Length: 16
                    Page Reference String: [7, 3, 6, 2, 5, 3, 9, 5, 6, 4, 5, 5, 9, 6, 3, 3]
                    ---
                    FIFO, 13, page faults.
                    LRU, 12, page faults.
                    OPT, 9, page faults.

    ========================
    ## COMMAND 2 - recording number of page faults for specified page reference string and number of frames.
        
        - python paging.py -s [page string] -f [page size]
            - [page string] referse to page reference string to test. e.g. 674893779380
            - [page size] refers to the number of page frames allocated in order to simulate the page replacement algorithms and count the number of page faults.

            - output format for [page string] = 85625354235326256856234213754315 and [page size] = 3

                >   ---
                    Number of Frames: 3
                    Page Reference Length: 32
                    Page Reference String: 85625354235326256856234213754315
                    ---
                    FIFO, 25, page faults.
                    LRU, 23, page faults.
                    OPT, 16, page faults.

    ========================
    ## COMMAND 3 - Recording Number of faults for randomly generated page reference string for frame size 1 - 7.

        - python paging.py -t

            - output format for `-test`:
                - Note that the output will include the randomly generated page reference string used for the output. 
                    Each run will use a different page reference string of different lengths. 
                
                >   ---------------------------------------------------------
                    Page String:
                    05011536738901536167552341491507380036371779871901173354036095988835998392378115927679450404173026638462828832619436165382628399
                    ---------------------------------------------------------
                    |  Number of Pages   |  8   |  16  |  32  |  64  | 128  |
                    ---------------------------------------------------------
                    |                  Number of Frames: 1                  |
                    ---------------------------------------------------------
                    |        FIFO        |  7   |  15  |  30  |  58  | 115  |
                    ---------------------------------------------------------
                    |        LRU         |  5   |  12  |  24  |  45  |  90  |
                    ---------------------------------------------------------
                    |        OPT         |  7   |  15  |  30  |  58  | 115  |
                    ---------------------------------------------------------
                    ---------------------------------------------------------
                    |  Number of Pages   |  8   |  16  |  32  |  64  | 128  |
                    ---------------------------------------------------------
                    |                  Number of Frames: 2                  |
                    ---------------------------------------------------------
                    |        FIFO        |  5   |  13  |  25  |  50  | 100  |
                    ---------------------------------------------------------
                    |        LRU         |  5   |  12  |  24  |  45  |  90  |
                    ---------------------------------------------------------
                    |        OPT         |  5   |  11  |  22  |  42  |  81  |
                    ---------------------------------------------------------
                    ---------------------------------------------------------
                    |  Number of Pages   |  8   |  16  |  32  |  64  | 128  |
                    ---------------------------------------------------------
                    |                  Number of Frames: 3                  |
                    ---------------------------------------------------------
                    |        FIFO        |  5   |  12  |  24  |  47  |  89  |
                    ---------------------------------------------------------
                    |        LRU         |  5   |  12  |  24  |  45  |  90  |
                    ---------------------------------------------------------
                    |        OPT         |  5   |  10  |  18  |  33  |  60  |
                    ---------------------------------------------------------

                    ... rest of the output has been ommited.

========== END ==========