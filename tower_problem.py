heights_string = input("Enter numbers: ").split(",")
heights = [int(x) for x in heights_string]

#############################################################################################################

import time

def getKeyPoints(heights): # Finds indexes for special towers. More mentioned below
    ascend = True
    key_points = []
    for index in range(len(heights) - 1):
        # It should be ascending
        if ascend:
            if heights[index] > heights[index + 1]:
                key_points.append(index) # Capture key point
                ascend = False
        # Not ascending (obviously)
        else:
            if heights[index] < heights[index + 1]:
                ascend = True
    # Checking if last tower is a key tower
    if ascend and heights[-1] >= heights[-2]:
        key_points.append(len(heights)-1)
    return key_points
key_points = getKeyPoints(heights) # Indexes of towers that act as sort of "walls" for gaps


# Volume for gaps of water
def getVolume():
    if len(key_points) == 0 or len(key_points) == 1:
        return 0
    volumeTotal = 0
    for indexKey in range(len(key_points) - 1):
        heightsTwo = sorted([heights[key_points[indexKey]], heights[key_points[indexKey + 1]]])
        areaRange = heights[key_points[indexKey] + 1:key_points[indexKey + 1]]
        smallest_height = heightsTwo[0]
        volume = len(areaRange) * smallest_height
        for towerHeight in areaRange:
            if smallest_height - towerHeight < 0:
                towerHeight = smallest_height
            volume -= towerHeight
        volumeTotal += volume
    return volumeTotal
volumeFinal = 0
volumeTotal = getVolume()

#############################################################################################################

while volumeTotal != 0: # Once no more volume can be added, end loop
    volumeFinal += volumeTotal
    # Gaps will be "filled" with water, and the remain
    for indexKey in range(len(key_points) - 1):
        heightsTwo = sorted([heights[key_points[indexKey]], heights[key_points[indexKey + 1]]])
        smallest_height = heightsTwo[0]
        for indexVal in range(key_points[indexKey] + 1, key_points[indexKey + 1]):
            if heights[indexVal] < smallest_height:
                heights[indexVal] = smallest_height
    key_points = getKeyPoints(heights)
    volumeTotal = getVolume()
    
    
print(volumeFinal)
