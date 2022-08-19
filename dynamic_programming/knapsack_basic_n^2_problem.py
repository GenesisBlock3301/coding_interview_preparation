
def greedy(data):
    arr = list()
    for i in data:
        for k in data:
            if i != k:
                val = data.get(i)[-1] + data.get(k)[-1]
                if val <= 35:
                    arr.append(i)
    return arr

data = {
    "stereo": [3000, 30],
    "guitar": [1500, 15],
    "laptop": [2000, 20]
}
print(greedy(data))