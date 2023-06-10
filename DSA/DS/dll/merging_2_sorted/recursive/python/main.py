class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;
        
class DLL:
    def __init__(self):
        self.head = None;
        
    @staticmethod
    def traverse(l):
        if l: print(l.data)
        else: return;
        DLL.traverse(l.next)
        
    @staticmethod
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
    
    def fill(self, arr, node=None):
        if not arr: return;
        if not self.head: 
            self.head = Node(arr[0]);
            self.fill(arr[1:], self.head)
            return;
        node.next = Node(arr[0]);
        node.next.prev = node;
        self.fill(arr[1:], node.next)
        
        
            
dll1 = DLL()
dll2 = DLL()
dll1.fill([4,7,8])
dll2.fill([1,3,10, 11, 12])
mergedHead = DLL.mergeSortedDlls(dll1.head, dll2.head);
DLL.traverse(mergedHead)
