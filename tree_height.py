# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    tree = [[] for i in range(n)]
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)
    root = np.where(parents == -1)[0][0]
    queue = [(root,0)]
    max_height = 0
    # Your code here
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height+1)
        for child in tree[node]:
            queue.append((child, height +1))
    return max_height


def main():
    # implement input form keyboard and from files
    input_type = input().strip()
    if "I" in input_type:
        n = int(input().strip())
        parentss = input().strip()
        parents = np.array(list(map(int, parentss.split())))
        height = compute_height(n, parents)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    elif "F" in input_type:
        file_name = input().strip()
        if "a" in file_name:
            print("incorrect, try again :^)")
            return
        with open("./test/" + file_name, 'r') as file:
            n = int(file.readline().strip())
            parentss = file.readline().strip()
            parents = np.array(list(map(int, parentss.split())))
            height = compute_height(n, parents)
    print(height)
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
# print(numpy.array([1,2,3]))