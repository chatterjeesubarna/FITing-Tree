
# Online Python - IDE, Editor, Compiler, Interpreter
import array as arr
import random
import numpy as np
import sys
import math

def sum(a, b):
    return (a + b)
    
def __shrinking_cone_segmentation(keys, locations, error):
        # data is the keys and pointers , it must be sorted
        # print("The ", len(keys), "-room array is: ", keys) #printing the array
        segments = []
        high_slope = float('inf')
        low_slope = 0
        origin_key = keys[0]
        origin_loc = locations[0]
        end_key = keys[0]
        # error = 32
        buffer_error = 0
        error = error - buffer_error
        no_segment = 0
        for i in range(1, len(keys)):
            key = keys[i]
            loc = locations[i]
            tmp_point_slope = (loc - origin_loc) / (key - origin_key)
            if low_slope <= tmp_point_slope <= high_slope:
                # Point is inside the cone
                tmp_high_slope = ((loc + error) - origin_loc) / (key - origin_key)
                tmp_low_slope = ((loc - error) - origin_loc) / (key - origin_key)
                high_slope = min(high_slope, tmp_high_slope)
                low_slope = max(low_slope, tmp_low_slope)
                end_key = key
            else:
                slope = (high_slope + low_slope) / 2
                if end_key == origin_key:
                    slope = 1
                # new_segment = Node.Segment(slope, origin_key, end_key)
                high_slope = float('inf')
                low_slope = 0
                origin_key = key
                origin_loc = loc
                end_key = key
                # segments.append(new_segment)
                no_segment = no_segment + 1
                
        slope = (high_slope + low_slope) / 2
        if end_key == origin_key:
            slope = 1
       
        return no_segment




def readFile(fileName):
        keys = []
        f = open(fileName)
        for line in f.readlines():
            keys.append(int(line))
        # print(keys)
        f.close()
        return keys

        # text_file = open(fileName, "r")
        # # keys = text_file.readlines().split('\n')
        # keys = text_file.read().splitlines()
        # # keys = text_file.read().split(',')
        # print(keys)
        # text_file.close()
        # return keys


        # fileObj = open(fileName, "r") #opens the file in read mode
        # keys = fileObj.read().splitlines() #puts the file into an array
        # fileObj.close()
        # return keys




data_entries = 10000000
distribution = 0
low = 4
high = 200
mu, sigma = 10000, 200 # mean and standard deviation
fanout = 32 #default

if len(sys.argv) > 1:
    distribution = int(sys.argv[1])
else:
    distribution = 0
    
if distribution == 0:
    data_entries = int(sys.argv[2])
    low = int(sys.argv[3])
    high = int(sys.argv[4])
    error = int(sys.argv[5])
    fanout = error
    # keys = np.random.uniform(low, high, data_entries)
    keys = readFile("../data.txt")
    # keys = keys.astype(int)
    keys = np.sort(keys)
    locations = range(len(keys))
    segments = __shrinking_cone_segmentation(keys, locations, error)
    length_of_each_segment = math.ceil(data_entries/segments)
    height = math.ceil(math.log(segments, fanout)) 
    print("\ndistribution: uniform, data entries:", data_entries, " low:", low, " high:", high)
    print("\n\n************************************************************ ACTUAL STRUCTURE (FIT-ing TREE) ************************************************************\n");
    print("#segments: ", segments)
    print("segments length: ", length_of_each_segment)
    print("height: ", height)
    internal_nodes = 0
    last = segments
    for i in range(height-1, 0, -1):
        if i == 1:
            last = 1
            internal_nodes = internal_nodes + 1
        else:
            last = last / fanout
            internal_nodes = internal_nodes + last
    print("FIT Internal nodes: ", internal_nodes)
elif distribution == 1:
    data_entries = int(sys.argv[2])
    mu = float(sys.argv[3])
    sigma = float(sys.argv[4])
    error = int(sys.argv[5])
    fanout = error
    # keys = np.random.normal(mu, sigma, data_entries)
    keys = readFile("../data.txt")
    # keys = keys.astype(int)
    keys = np.sort(keys)
    locations = range(len(keys))
    segments = __shrinking_cone_segmentation(keys, locations, error)
    length_of_each_segment = math.ceil(data_entries/segments)
    height = math.ceil(math.log(segments, fanout)) 
    print("\ndistribution: uniform, data entries:", data_entries, " mean:", mu, " sigma:", sigma)
    print("\n\n************************************************************ ACTUAL STRUCTURE (FIT-ing TREE) ************************************************************\n");
    print("#segments: ", segments)
    print("segments length: ", length_of_each_segment)
    print("height: ", height)
    internal_nodes = 0
    last = segments
    for i in range(height-1, 0, -1):
        if i == 1:
            last = 1
            internal_nodes = internal_nodes + 1
        else:
            last = last / fanout
            internal_nodes = internal_nodes + last
    print("FIT Internal nodes: ", internal_nodes)

