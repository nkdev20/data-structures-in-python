class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def insertNode(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head= temp

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None) :
            if temp.data == key :
                self.head = temp.next
                temp = None
    
        while (temp is not None) : 
            if temp.data == key :
                break
            prev = temp
            temp = temp.next

        if temp == None : 
            return

        prev.next = temp.next
        temp = None

            




    def insertAfter(self, data):
        new_node = Node(data)

        #if new node empty make it head
        if self.head == None:
            self.head = new_node

        temp = self.head
        while(temp.next != None):
            temp = temp.next

        temp.next = new_node
        new_node.next = None 


    def detect_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head != None:
            while fast_ptr != None and fast_ptr.next != None:
                fast_ptr = fast_ptr.next.next
                slow_ptr  = slow_ptr.next
                if fast_ptr == slow_ptr:
                    print("Loop detected")
                    return

        print('No Loop detecet')




    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data), 
            temp = temp.next 


if __name__ == "__main__":

    list = LinkedList()
    list.insertNode(1)
    list.insertNode(2)
    list.insertNode(3)
    list.insertNode(4)
    list.insertNode(5)
    list.insertNode(6)
    list.printList()
    list.head.next.next.next.next = list.head 
    list.detect_loop()
