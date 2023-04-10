LCS : Alleviating Total Cold Start Latency in Serverless Applications with LRU Warm Container Approach 

The codebase contains a simulation to compare the 2 main container selection approaches while executing any Serverless Application based on the amount of cold starts that occur due to different use cases. The two approaches are: 
    1. Most Recently Used Container Selection Approach (MRU)
    2. Least Recently Used Container Selection Approach (LRU/LCS)

To run the code:
1. Clone the repository
2. run the following commands on the terminal:
    - pip install table-logger
    - python init.py

    
The codebase contains the following files:
    - init.py: The execution of the simulation starts from here. A method to simulate the whole experiment is defined here and the summarized and compiled results are logged here.
    - input.json: This file contains all the use cases we want to run our simulation on. each use case contains three attributes:
        > requests: An array consisting of the no of requests coming in at each timestamp.
        > cycle: The total time units for which simulation needs to run
        > existing_warm_container_timestamps: An array telling us the timestamps at which a warm container is to be initiated. 
    - lru.py: Contains a class called LRUCache containing all the metadata related to the LCS algorithm and a method to execute the LRU algorithm for a given input and returning the cold starts.
    - mru.py: Contains a class called MRUCache containing all the metadata related to the MRU algorithm and a method to execute the MRU algorithm for a given input and returning the cold starts.
    - results.log: A log file created to log all the details for reference on how the flow works for both algorithms.
    - utils.py: A utility file that provides us with a Logger class that logs the info into the log file and also prints the results in a tabular form. 

Done by:- 
    Aritra Sinha(191EC108) 
    Riya Dharmesh Shah(191CS244) 
    Aaidan Ram Meghwal(191CS101)
    Malcolm Fernandes(191CS134) 
