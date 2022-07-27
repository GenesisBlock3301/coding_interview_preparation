# https://pythonwife.com/greedy-algorithms-in-python/
"""
We are given N number of activities with their start and finish times.
A person can only work on a single activity at a time. According to the problem question,
we need to select the maximum number of activities that can be performed by a single person.
"""

"""
Implementation of Activity Selection Problem
The Activity Selection Problem makes use of the Greedy Algorithm in the following manner:

-> First, sort the activities based on their finish time.
-> Select the first activity from the sorted list and print it.
-> For all the remaining activities, check whether the start time of the activity is greater
 or equal to the finish time of the previously selected activity. If so, select this activity and print it.

"""
"""
Time and Space Complexity
The time complexity for the Activity Selection Problem is O(NlogN) as it takes this much time to sort the unsorted
list of activities. The space complexity is O(1) as no additional memory is required.
"""

# Function to solve the Activity Selection Problem
def print_max_activities(activities):
    activities.sort(key=lambda x: x[2])
    i = 0
    first_a = activities[i][0]
    print(first_a)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j


activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
              ]
print_max_activities(activities)
