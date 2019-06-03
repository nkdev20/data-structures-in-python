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

    def merging_pt(self, list1, list2):
        list1_length = 0
        list2_length = 0
        temp = list1.head
        while temp:
            temp = temp.next
            list1_length += 1

        temp = list2.head
        while temp:
            temp = temp.next
            list2_length += 1

        diff = abs(list2_length - list1_length)

        if list1_length > list2_length:
            traversed_list1 = self.traverse_list(list1, diff)
            temp = list2.head   
            while temp:
                if temp == traversed_list1:
                    print('Merging  Point is {}'.format(temp.data))
                    break
                temp = temp.next
                traversed_list1 = traversed_list1.next
        else:
            traversed_list2 = self.traverse_list(list2, diff)
            temp = list1.head   
            while temp:
                if temp == traversed_list2:
                    print('Merging  Point is {}'.format(temp.data))
                    break
                temp = temp.next
                traversed_list2 = traversed_list2.next


        
    def traverse_list(self, list, diff):
        temp = list.head
        count  = 0
        
        while count < diff :
            count += 1
            temp = temp.next

        return temp

    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data), 
            temp = temp.next 


if __name__ == "__main__":

    list1 = LinkedList()
    list2 = LinkedList()
    list1.insertAfter(1)
    list1.insertAfter(2)
    list1.insertAfter(3)
    list1.insertAfter(5)
    list1.insertAfter(6)
    list2.insertAfter(4)
    list2.head.next = list1.head.next.next.next
    list1.printList()

    print('-----')
    list2.printList()
    # list1.merging_pt(list1, list2)
    # list1.detect_loop()
