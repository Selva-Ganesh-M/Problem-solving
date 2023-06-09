class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;

class DLL:
    def __init__(self):
        self.head = None;
    
    @staticmethod
    def mergeSortedDlls(first, second):
        if first.data < second.data:
            my = first;
            other = second;
        else:
            my = second;
            other = first;
        head = my;
        myEnd = None;
        while (other):
            if (my):
                if my.data > other.data:
                    detached = other;
                    if other.next:
                        other = other.next;
                        other.prev = None;
                    else:
                        other = other.next;
                    detached.next = None;
                    if not my.prev:
                        my.prev = detached;
                        detached.next = my;
                    else:
                        my.prev.next = detached;
                        detached.prev = my.prev;
                        detached.next = my;
                        my.prev = detached;
                else:
                    if not my.next: myEnd = my;
                    my = my.next;
            else:
                myEnd.next = other;
                other.prev = myEnd;
                other = None;
        return head;
        
    @staticmethod
    def s_print(head):
        while(head):
            print(head.data);
            head = head.next;
        
    def fill(self, arr):
        if not arr: return;
        if not self.head: self.head = Node(arr[0])
        arr = arr[1:]
        prev = self.head;
        for data in arr:
            new = Node(data)
            new.prev = prev;
            prev.next = new;
            prev = new;
            
    def print(self):
        if not self.head: return;
        current = self.head;
        while(current):
            print(current.data);
            current = current.next;
    

l1 = DLL()
l2 = DLL()
l1.fill([2,3,5,7,9])
l1.print()
l2.fill([1,8,10])
l2.print()
newRoot = DLL.mergeSortedDlls(l1.head, l2.head)
print("ans")
DLL.s_print(newRoot)
