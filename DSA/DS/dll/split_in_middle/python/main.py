class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;
        
class DLL:
    def __init__(self):
        self.head = None;
        
    @staticmethod
    # traverses the given dll
    def traverse(l):
        if l: print(l.data)
        else: return;
        DLL.traverse(l.next)
        
    @staticmethod
    # merges two sorted dlls
    def mergeSortedDlls(l1, l2):
        if not l1: return l2;
        if not l2: return l1;
        if (l1.data < l2.data):
            detached = l1;
            l1 = l1.next;
            detached.next = None;
            if l1: l1.prev = None;
        else:
            detached = l2;
            l2 = l2.next;
            detached.next = None;
            if l2: l2.prev = None;
        nextItem = DLL.mergeSortedDlls(l1, l2)
        detached.next = nextItem;
        nextItem.prev = detached;
        return detached;
    
    @staticmethod
    # splits the given dll into two parts
    def splitInMiddle(l):
        if not l or not l.next: return l;
        slow = l;
        fast = l;
        while fast and fast.next:
            fast = fast.next.next;
            slow = slow.next;
        slow.prev.next = None;
        slow.prev = None;
        return l, slow;
        
        
    
    # fill the dll with the array items
    def fill(self, arr, node=None):
        if not arr: return;
        if not self.head: 
            self.head = Node(arr[0]);
            self.fill(arr[1:], self.head)
            return;
        node.next = Node(arr[0]);
        node.next.prev = node;
        self.fill(arr[1:], node.next)
        


dll = DLL()
dll.fill([5,1,7,3,9,4,2,6,8])
fh, sh = DLL.splitInMiddle(dll.head)
print("first half")
DLL.traverse(fh)
print("\nsecond half")
DLL.traverse(sh)
