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



    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data), 
            temp = temp.next 


if __name__ == "__main__":

    list = LinkedList()
    list.insertAfter(1)
    list.insertAfter(2)
    list.insertAfter(3)
    list.printList()
    list.deleteNode(2)
    # list.insertNode(3)
    # list.head = Node(1)
    # second = Node(2)
    # third = Node(3)    
    

    # list.head.next = second
    # second.next = third
    # # list.insertNode(5)
    # list.insertAfter(8)
    list.printList()
