from collections import deque


def search(graph,name):
    visited = list()
    search_queue = list()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.pop(0)
        if person not in visited:
            # print(person, end="->")
            if is_mongo_seller(person):
                print(f"Person name is {person}", visited)
                return True
            else:
                search_queue += graph[person]
                visited.append(person)
    return False


def is_mongo_seller(name):
    return name[-1] == "m"
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search(graph, "you")