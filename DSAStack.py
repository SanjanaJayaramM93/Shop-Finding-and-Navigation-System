from DSALinkedlist import DSALinkedList

class DSAStack(DSALinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        try:
            self.insert_First(value)
            return value
        except Exception as e:
            print(f"An error occurred while pushing: {str(e)}")

    def pop(self):
        try:
            if self.is_empty():
                return None
            else:
                headValue = self.peek_first()
                self.remove_first()
                return headValue
        except Exception as e:
            print(f"An error occurred while popping: {str(e)}")

