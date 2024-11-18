class DSAListNode:                            # List node class
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None                
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_next(self):
        return self.next
    def set_next(self, newNext):
        self.next = newNext
    def get_prev(self):                 
        return self.prev
    def set_prev(self, newPrev):        
        self.prev = newPrev

class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_First(self, newValue):
        try:
            newNd = DSAListNode(newValue)
            if self.is_empty():
                self.head = newNd
                self.tail = newNd
            else:
                newNd.set_next(self.head)
                self.head.set_prev(newNd)
                self.head = newNd
            return newValue
        except Exception as e:
            print(f"An error occurred during insertion: {str(e)}")

    def insert_last(self, newValue):
        try:
            newNd = DSAListNode(newValue)
            if self.is_empty():
                self.head = newNd
                self.tail = newNd
            else:
                newNd.set_prev(self.tail)
                self.tail.set_next(newNd)
                self.tail = newNd
            return newValue
        except Exception as e:
            print(f"An error occurred during insertion: {str(e)}")

    def insert_sorted(self, newValue):
        try:
            newNd = DSAListNode(newValue)

            if self.is_empty():
                self.head = newNd
                self.tail = newNd
            else:
                current_shop = self.head

                while current_shop is not None and newValue.get_value().shop_number > current_shop.get_value().get_value().shop_number:
                    current_shop = current_shop.get_next()

                if current_shop is None:
                    self.tail.set_next(newNd)
                    newNd.set_prev(self.tail)
                    self.tail = newNd
                else:
                    newNd.set_next(current_shop)
                    newNd.set_prev(current_shop.get_prev())

                    if current_shop.get_prev() is None:
                        self.head = newNd
                    else:
                        current_shop.get_prev().set_next(newNd)

                    current_shop.set_prev(newNd)
            return newValue
        except Exception as e:
            print(f"An error occurred during insertion: {str(e)}")

    def peek_first(self):
        try:
            if self.is_empty():
                print('Empty')
            else:
                nodeValue = self.head.get_value()
                return nodeValue
        except Exception as e:
            print(f"An error occurred during peek_first: {str(e)}")

    def peek_last(self):
        try:
            if self.is_empty():
                print('Empty')
            else:
                nodeValue = self.tail.get_value()
                return nodeValue
        except Exception as e:
            print(f"An error occurred during peek_last: {str(e)}")

    def remove_first(self):
        try:
            if self.is_empty():
                print('Empty')
            else:
                nodeValue = self.head.get_value()
                if self.head.get_next():
                    self.head.get_next().set_prev(None)
                self.head = self.head.get_next()
                return nodeValue
        except Exception as e:
            print(f"An error occurred during remove_first: {str(e)}")

    def remove_last(self):
        try:
            if self.is_empty():
                print('Empty')
            else:
                nodeValue = self.tail.get_value()
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.get_prev().set_next(None)
                    self.tail = self.tail.get_prev()
                return nodeValue
        except Exception as e:
            print(f"An error occurred during remove_last: {str(e)}")
