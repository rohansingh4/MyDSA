"""
Input: 2
Output: Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C

Input: 3
Output: Disk 1 moved from A to C
Disk 2 moved from A to B
Disk 1 moved from C to B
Disk 3 moved from A to C
Disk 1 moved from B to A
Disk 2 moved from B to C
Disk 1 moved from A to C

"""


def toh(N, source, auxillary, destination):
    if N == 0:
        return
    toh(N - 1, source, destination, auxillary)
    print(f"Moving Disk {N} from {source} to {destination}")
    toh(N - 1, auxillary, source, destination)


# driver
if __name__ == "__main__":
    N = 3
    toh(N, "A", "B", "C")
