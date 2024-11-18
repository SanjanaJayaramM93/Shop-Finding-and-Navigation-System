import numpy as np

class DSAHeapEntry:
    def __init__(self, priority, value = 10):
        self.priority = priority
        self.value = value

    def get_priority(self):
        return self.priority
        
    def get_value(self):
        return self.value

class DSAHeap:
    def __init__(self, max_size):
        self.heap = np.empty(max_size, dtype=object)
        self.count = 0

    def addShop_to_heap(self, priority, value):
        try:
            if self.count < len(self.heap):
                entry = DSAHeapEntry(priority, value)
                self.heap[self.count] = entry
                self.trickle_up(self.count)
                self.count += 1
            else:
                print("Heap is full. Cannot add more elements.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_shops_in_heap(self):
        try:
            # Sort in descending order
            self.heap_sort()
            for i in range(self.count - 1, -1, -1):
                print("Shop Rating : ", self.heap[i].get_priority(), 
                      "\tShop Number : ",self.heap[i].get_value().value.shop_number,
                      '\tShop Name : ', self.heap[i].get_value().value.shop_name,
                      '\tCategory : ', self.heap[i].get_value().value.category,
                      '\tLocation : ', self.heap[i].get_value().value.location)
            self.clear_heap()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def clear_heap(self):
        self.heap = np.empty(len(self.heap), dtype=object)
        self.count = 0

    def trickle_up(self, curIdx):
        try:
            parentIdx = (curIdx - 1) // 2

            while curIdx > 0 and self.heap[curIdx].get_priority() > self.heap[parentIdx].get_priority():
                self.heap[curIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[curIdx]
                curIdx = parentIdx
                parentIdx = (curIdx - 1) // 2
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
    def heapify(self):
        try:
            for i in range((self.count // 2)-1, -1, -1):
                self.trickle_down(i, self.count)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def heap_sort(self):
        try:
            self.heapify()
            for i in range(self.count - 1, 0, -1):
                self.swap(0, i)
                self.trickle_down(0, i)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Update the trickle_down method to take an additional parameter
    def trickle_down(self, curIdx, end):
        try:
            lChildIdx = curIdx * 2 + 1
            rChildIdx = lChildIdx + 1
            keepGoing = True

            while keepGoing and rChildIdx < end:
                keepGoing = False
                largeIdx = lChildIdx

                if rChildIdx < end and self.heap[lChildIdx].get_priority() < self.heap[rChildIdx].get_priority():
                    largeIdx = rChildIdx

                if self.heap[largeIdx].get_priority() > self.heap[curIdx].get_priority():
                    self.heap[largeIdx], self.heap[curIdx] = self.heap[curIdx], self.heap[largeIdx]
                    keepGoing = True
                    # curIdx = largeIdx
                    lChildIdx = curIdx * 2 + 1
                    rChildIdx = lChildIdx + 1
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def swap(self, index1, index2):
        try:
            self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        except Exception as e:
            print(f"An error occurred: {str(e)}")

