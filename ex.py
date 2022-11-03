# Coral Belo 
import requests

""" 
A function that do a binary search on the values of the timstampes of the blocks, Time Complexity: O(log n) 
input: l- first index of the block, r- last index of the block, ts- input TS
output: return the index of the block which is the closest to TS
"""
def binarySearch(l, r, ts):
    # Middle index of the block
    mid = l + (r - l) // 2
    # The timestamp of the middle index of the block
    currentTs=int(getTimeStamp(mid))
    # check if current timestamp is bigger from the given TS
    if currentTs > ts:
        # The timestamp of the middle-1 index of the block
        prevTs=int(getTimeStamp(mid-1))
        # check if the prev timestamp is the last timestamp that small from TS
        if(currentTs > ts and prevTs < ts):
            return mid-1
        # else, continue to search the last index of that most closet to TS
        return binarySearch(l, mid-1, ts)

    # Else the index of the block which is the closest to TS can only be present in the right range
    else:
        return binarySearch(mid + 1, r, ts)
    
""" 
A function that calculate the timestamp of the given Height of block
input: blockHeight - height of the block 
output: return the timestamp of the given Height of block
"""
def getTimeStamp(blockHeight):
    # making a get request
    URL = f"https://blockchain.info/block-height/{blockHeight}?format=json"
    # extracting data in json format
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    datablocks=data["blocks"][0]
    return datablocks["time"]

""" 
A function that return the latest block height
input: None
output: return the latest block height
"""
def getLastBlock():
    # making a get request
    URL = "https://blockchain.info/latestblock"
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    return data["height"]

#main
lastIndexBlock = str(getLastBlock())
# timestamp of the last block
tsLastBlock = int(getTimeStamp(lastIndexBlock))
# timestamp of the first block
tsfirstBlock= int(getTimeStamp('0'))
inputTs= int(input('What it is the timestamp?'))
# check if the input is negative
if inputTs < 0:
    print("the timestamp should be positive") 
# if the timestamp of the first block is bigger or equal to the input timestamp, no such index exists
elif tsfirstBlock >= inputTs:
    print("No such index exists")
# if the input of timestamp bigger from the timestamp of the last block, the lastindexblock is the last index
elif inputTs >= tsLastBlock:
    print(lastIndexBlock)
else:
    index = binarySearch(0,int(lastIndexBlock),inputTs)
    print(index)
