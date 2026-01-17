#classic tower of hanoi, only hint use middle rod as a helper node
# assuming all disks are at A  and we have to move to C, B is the helper node

#drive code

"""
Docstring for towerOfHanoi

to move n disks from source to destination s->d
we have to movie n-1 disk to auxillary s-> a
so that we can move largest disk from s ->d
so that we can move n-1 disk from auxillary to destination s-> d (using S)
"""


# def tower_of_hanoi(N, source, auxillary, destination):
#     #best case
#     if N == 0:
#         print(f"Moved 1 disks from {source} to {destination}.")
#         return
#     tower_of_hanoi(N-1, source, destination, auxillary)
#     print(f"Moved {N} disks from {source} to {destination}.")
#     tower_of_hanoi(N-1, auxillary, source, destination)


# tower_of_hanoi(3, "S", "A", "D")


def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Driver code
tower_of_hanoi(3, "S", "A", "D")
