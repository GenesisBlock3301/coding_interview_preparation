## Sorting Algorithm note:

### Bubble Sort:
- Take a array and use two loop for traverse all value.
- Compare two values and swap.
- Time and Space complexity - **O(n^2) and O(1)**.

### Selection Sort:
- Select first index as MinimumIndex. 
- Compare with others value.
- Then compare if MinimumIndex value larger than other swap both of them.
- Time and Space complexity - **O(n^2) and O(1)**.

### Insertion Sort:
- Loop through 1 number value, and compare each other
- Compare below all items and then place this value right place
- Time and Space complexity - **O(n^2) and O(1)**.

### Merge sort:
- First of all find mid and divide left and right.
- Then this left and right values send to merge function to make merge them.
- Time and space complexity - O(n log n) and O(n).

### Quick Sort
- select pivot as a first
- Compare all values left and right side of values
- Call recursion left + pivot + right
- Time and space complexity - avg - O(n log n), worse O(n^2) and avg(log n),worse O(n).

### Redix Sort