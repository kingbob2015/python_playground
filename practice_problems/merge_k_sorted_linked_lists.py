# Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.

# Input:
# First line of input contains number of testcases T. For each testcase, first line of input contains number of linked lists N and next line contains data of nodes of all K linked lists, with first element as M, the length of linked list and next M elements for the same linked list.

# Output:
# For each testcase, in a new line, print the merged linked list.

# Your Task:
# The task is to complete the function mergeKList() which merges the K given lists into a sorted one. The printing is done automatically by the driver code.

# Constraints
# 1 <= T <= 50
# 1 <= N <= 103

# Example:
# Input:
# 2
# 4
# 3 1 2 3 2 4 5 2 5 6 2 7 8
# 3
# 2 1 3 3 4 5 6 1 8
# Output:
# 1 2 3 4 5 5 6 7 8
# 1 3 4 5 6 8

# Explanation :
# Testcase 1: The test case has 4 sorted linked list of size 3, 2, 2, 2
# 1st    list     1 -> 2-> 3
# 2nd   list      4->5
# 3rd    list      5->6
# 4th    list      7->8
# The merged list will be 1->2->3->4->5->5->6->7->8.
# Testcase 2: The test case has 3 sorted linked list of size 2, 3, 1.
# 1st list 1 -> 3
# 2nd list 4 -> 5 -> 6
# 3rd list 8
# The merged list will be 1->3->4->5->6->8.

'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    heads is a list containing the n linkedlists
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
    
    linked list class:

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.nxt=Node(x)
            self.tail=self.tail.nxt
'''
from heapq import heappush, heappop

def merge(heads,n):
    #code here
    returnList = LinkedList()
    h = []
    #Need the extra increment in heap in case of tie value
    i = 0
    for l in heads:
     heappush(h, (l.head.data,i, l.head))
     i+=1
    while len(h) > 0:
        toAdd = heappop(h)
        returnList.add(toAdd[0])
        if toAdd[2].nxt:
            try:
                heappush(h, (toAdd[2].nxt.data,i,toAdd[2].nxt))
                i+=1
            except Exception as e:
                print(e)
    return returnList


#{ 
#  Driver Code Starts


#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.nxt=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.nxt=Node(x)
            self.tail=self.tail.nxt
    
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data, end=' ')
            temp=temp.nxt
        print()

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        heads=[]
        index=0
        for i in range(n):
            heads.append(LinkedList())
            size=line[index]
            for j in range(index+1,index+1+size):
                heads[i].add(line[j])
            index+=size+1
        
        merged_list = merge(heads,n)
        merged_list.printList()

# } Driver Code Ends