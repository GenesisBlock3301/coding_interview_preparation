def greedy(_data):
    arr = list()
    for i in _data:
        for k in _data:
            if i != k:
                val = _data.get(i)[-1] + _data.get(k)[-1]
                if val <= 35:
                    arr.append(i)
    return arr


data = {
    "stereo": [3000, 30],
    "guitar": [1500, 15],
    "laptop": [2000, 20]
}
print(greedy(data))
