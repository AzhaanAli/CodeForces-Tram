"""
DIRECTIONS:
Linear Kingdom has exactly one tram line. It has n stops, numbered from 1 to n in the order of tram's movement.
At the i-th stop 'a' passengers exit the tram, while 'b' passengers enter it.
The tram is empty before it arrives at the first stop. Also, when the tram
arrives at the last stop, all passengers exit so that it becomes empty.

Your task is to calculate the tram's minimum capacity such that the number of people inside the tram at anytime never
exceeds this capacity. Note that at each stop all exiting passengers exit before any entering passenger enters the tram.
"""

# We need to loop through all inputs while keeping track of the highest current capacity.
# The highest current capacity is the answer to the question.

stops = int(input())
maxCapacity = 0
currentCapacity = 0
for i in range(0, stops):
    data = input().split(' ')
    # Let off an on passengers.
    currentCapacity -= int(data[0])
    currentCapacity += int(data[1])
    # If currentCapacity > maxCapacity, set maxCapacity to currentCapacity.
    maxCapacity = max(maxCapacity, currentCapacity)

# maxCapacity should now hold the highest capacity throughout the tram.
print(maxCapacity)
