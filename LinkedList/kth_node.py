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


    def find_kth_node(self, k):
        first_ptr = self.head
        second_ptr = self.head
        count = 0
        while count < k: 
            second_ptr = second_ptr.next
            count+=1

        if self.head != None:
            while second_ptr != None :
                first_ptr = first_ptr.next
                second_ptr  = second_ptr.next
        print('The kth node is {}'.format(first_ptr.data))


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

    list.find_kth_node(5)
