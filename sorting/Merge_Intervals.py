# https://leetcode.com/problems/merge-intervals/


def merge_interval(intervals):
    intervals.sort()
    n = len(intervals)
    output = [intervals[0]]
    if n == 1:
        return intervals
    i = 1
    while i < n:
        if output[-1][1] >= intervals[i][0]:
            output[-1][1] = max(output[-1][1], intervals[i][1])
        else:
            output.append(intervals[i])
        i += 1
    return output


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,3]]
# intervals = [[1, 4],[5,6]]
# intervals = [[1, 4], [0, 4]]
# intervals = [[1,4],[0,1]]
# intervals = [[1,4],[0,0]]
intervals = [[1,4],[0,2],[3,5]]
print(merge_interval(intervals))
