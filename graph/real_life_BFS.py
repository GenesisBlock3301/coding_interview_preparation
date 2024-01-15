def is_distination(destination):
    return destination == "Dhaka"


def search_short_path(graph, name):
    visited = list()
    search_queue = list()
    search_queue += graph[name]
    while search_queue:
        district = search_queue.pop(0)
        if district not in visited:
            # print(person, end="->")
            if is_distination(district):
                print(f"Person name is {district}", visited)
                return True
            else:
                search_queue += graph[district]
                visited.append(district)
    return False


graph = dict()
graph["Jamalpur"] = ["Mymensingh", "Tangail"]
graph["Mymensingh"] = ["Gazipur"]
graph["Dhaka"] = []
graph["Tangail"] = ["Dhaka"]
graph["Gazipur"] = ["Dhaka"]

search_short_path(graph, "Jamalpur")
