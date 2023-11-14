def tower_of_hanoi(n, source, destination, auxilary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n-1, source, auxilary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxilary, destination, source)


tower_of_hanoi(3, "A", "C", "B")
