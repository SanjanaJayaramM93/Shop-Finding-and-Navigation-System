from DSALinkedlist import DSALinkedList

class DSAQueue(DSALinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        try:
            self.insert_last(value)
            return value
        except Exception as e:
            print(f"An error occurred while enqueuing: {str(e)}")

    def dequeue(self):
        try:
            if self.is_empty():
                return None
            else:
                headValue = self.peek_first()
                self.remove_first()
                return headValue
        except Exception as e:
            print(f"An error occurred while dequeuing: {str(e)}")
