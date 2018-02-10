class Heap:

    def __init__(self):
        self.A = [0]

    def LEFT(self,i):
        if i is 0:
            return "Warning: LEFT(i), i is 0 out of lower-boundry"
        return 2 * i

    def RIGHT(self,i):
        if i is 0:
            return "Warning: RIGHT(i), i is 0 out of lower-boundry"
        return (2 * i) + 1

    def PARENT(self,i):
        if i is 0:
            return "Warning: PARENT(i), i is 0 out of lower-boundry"
        elif i is not 1:
            return (i) / 2
        else:
            return "Warning: PARENT(i), i is 1 Root has NO parent"

    def Max_Heapify(self,i,size=0):

        if size is 0:
            size = len(self.A)

        l = self.LEFT(i)
        r = self.RIGHT(i)

        if l <= size-1 and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i

        if r <= size-1 and self.A[r] > self.A[largest]:
            largest = r

        if largest is not i:
            tmp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = tmp
            self.Max_Heapify(largest,size=size)

    def Build_Max_Heap(self):
        n = len(self.A)
        mid = n / 2
        for i in range(mid, 0, -1):
            self.Max_Heapify(i,size=n)

    def Heapsort(self):
        length = len(self.A)-1
        self.Build_Max_Heap()
        for i in range(length,1,-1):
            tmp = self.A[1]
            self.A[1] = self.A[i]
            self.A[i] = tmp
            self.Max_Heapify(1,size=i)

        print "Heap Sort:\t\t\t\t\t\t     " + str(self.A)

    def Max_Heap_Insert(self,key):
        self.A.append(key)
        self.Heap_Increase_Key(len(self.A)-1,key)

    def Heap_Extract_Max(self):
        n = len(self.A)-1
        if n < 1:
            return "Error: Heap Underflow."
        max = self.A[1]
        self.A[1] = self.A[n]
        self.A.remove(self.A[n])
        self.Max_Heapify(1,size=n-1)
        return max

    def Heap_Increase_Key(self,i,key):
        if key < self.A[i]:
            return "Error: New key is smaller than current key."
        self.A[i] = key
        while(i > 1 and self.A[self.PARENT(i)] < self.A[i]):
            tmp = self.A[i]
            self.A[i] = self.A[self.PARENT(i)]
            self.A[self.PARENT(i)] = tmp
            i = self.PARENT(i)

    def Heap_Maximum(self):
        return self.A[1]

def CREATE_HEAP(list):
    h = Heap()
    h.Build_Max_Heap()
    print "\n---HEAP INFO---"
    print "Input List:\t\t\t\t\t\t\t " + str(list)
    print "Insert the input list into the Heap:",
    for i in range(len(list)):
        h.Max_Heap_Insert(list[i])
    print h.A

    print "Build Max Heap:\t\t\t\t\t\t " + str(h.A)
    print "Heap Extract Max:     - " + str(h.Heap_Extract_Max()) + " -\t\t\t " + str(h.A)

    h.Heap_Increase_Key(8, 10)
    print "Increase Key of 8th node as 10:\t\t " + str(h.A)
    h.Heapsort()

def generateRandomArray(length,rng):
	from random import randint
	List=[randint(0,length) for i in range(rng)]
	return List

def main():
    CREATE_HEAP(generateRandomArray(30,100))
    CREATE_HEAP(generateRandomArray(50, 1000))
    CREATE_HEAP(generateRandomArray(100, 500))

if __name__ == '__main__':
    main()