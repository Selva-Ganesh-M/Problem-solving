package ds;

class Node{
    private int data;
    private Node next;
    public Node(int num){
        this.data = num;
        this.next = null;
    }

    public int getData(){
        return this.data;
    } 

    public void setData(int data){
        this.data = data;
    }

    public Node getNext(){
        return this.next;
    }

    public void setNext(Node node){
        if (node instanceof Node || node==null){
            this.next = node;
        }else{
            System.out.println("Invaid value for a node.");
        }
    }
}

public class Sll{
    private Node head;
    private Node tail;
    public Sll(){
        this.head = null;
        this.tail = null;
    }

    public void append(int data){
        Node node = new Node(data);
        if (this.tail==null){
            this.head = node;
            this.tail = this.head;
        }else{
            this.tail.setNext(node);
            this.tail = node;
        }
    }

    public void prepend(int data){
        Node node = new Node(data);
        if(this.head==null){
            this.head = node;
            this.tail = this.head;
        }else{
            node.setNext(this.head);
            this.head = node;
        }
    }

    public void print(){
        Node temp = this.head;
        while (temp!=null){
            System.out.println(temp.getData());
            temp = temp.getNext();
        }
    }

    public int getHeadValue(){
        return this.head.getData();
    }

    public int getTailValue(){
        return this.tail.getData();
    }

    public void insert(int index, int data) throws IndexOutOfBoundsException{
        Node node = new Node(data);
        if (index == 0 ){
            node.setNext(this.head);
            this.head = node;
            this.tail = node;
            return;
        }    
        Node current = this.head;
        int currIndex = 0;
        while (current!=null && currIndex < index - 1){
            current = current.getNext();
            currIndex++;
        }
        if (current==null){
            throw new IndexOutOfBoundsException("provided index is out of range.");
        }
        node.setNext(current.getNext());
        current.setNext(node);
        if (node.getNext()==null){
            this.tail = node;
        }

    } 

    public void removeByValue (int value) throws Exception {
        if(this.head==null){
            return;
        }
        Node current = this.head;
        Node prev = null;
        while(current!=null){

            // if item matched
            if (current.getData()==value){

                // if its head
                if (current == this.head){
                    this.head = current.getNext();
                    current.setNext(null);
                    return;
                }
                // if its tail
                else if (current == this.tail){
                    prev.setNext(null);
                    this.tail = prev;
                    return;
                }
                // if any node in-between
                else{
                    prev.setNext(current.getNext());
                    current.setNext(null);
                    return;
                }
            }
            prev = current;
            current = current.getNext();
        }
        if (current==null){
            throw new Exception("Item not found.");
        }
    }

    public void removeByPosition (int pos) throws IndexOutOfBoundsException {
        if (this.head==null) return;
        int currPos = 0;
        Node currentNode = this.head;

        // if head is the target
        if (pos == currPos){
            this.head = this.head.getNext();
            currentNode.setNext(null);
            return;
        }

        // traverse to start before the target if it exists.
        while (currentNode!=null && currPos<pos-1){
            currPos++;
            currentNode = currentNode.getNext();
        }


        // if target not exists
        if (currentNode==null){
            throw new IndexOutOfBoundsException("index out of range to delete.");
        }

        // if target is tail node
        if (currentNode.getNext()==this.tail){
            currentNode.setNext(null);
            this.tail = currentNode;
        }
        // if target is in-between nodes
        else{
            Node target = currentNode.getNext();
            currentNode.setNext(target.getNext());
            target.setNext(null);
        }

    }

}