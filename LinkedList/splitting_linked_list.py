#Split a given likned list into 2 list with alternate values

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

    def splitting_list(self, list1, list2):
        if self.head == None or self.head.next == None:
            print('List is empty')
            return

        list1 = self.head
        list2 = self.head.next 
        
        while self.head:
            temp = self.head.next
            self.head.next = temp.next if temp!=None else temp
            self.head = temp
        print('First List') 
        self.printL(list1)   
        print('Second List')
        self.printL(list2)


    def printL(self, list):
        temp = list
        while(temp):
            print(temp.data)
            temp = temp.next



    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data), 
            temp = temp.next 


if __name__ == "__main__":
    list  = LinkedList()
    list1 = LinkedList()
    list2 = LinkedList()
    list.insertAfter(1)
    list.insertAfter(2)
    list.insertAfter(3)
    list.insertAfter(5)
    list.insertAfter(6)
    list.insertAfter(4)
    list.printList()
    list.splitting_list(list1, list2)
    # list.printList()