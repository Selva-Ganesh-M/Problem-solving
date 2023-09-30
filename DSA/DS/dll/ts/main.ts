
import { ILinkedList, INode_ } from "./testT";

class Node_<T> implements INode_<T> {
  public value: T;
  prev: Node_<T> | null;
  next: Node_<T> | null;

  constructor(value: T) {
    this.prev = null;
    this.next = null;
    this.value = value;
  }

  // methods
}

class LinkedList<T> implements ILinkedList<T> {
  private head: Node_<T> | null;
  private tail: Node_<T> | null;

  constructor() {
    this.head = null;
    this.tail = null;
  }

  // methods

  // #region : private mtds

  private addFirst = (value: T) => {
    this.head = this.tail = new Node_<T>(value);
  }

  private isEmpty = () => {
    return this.head == null
  }

  // #endregion : private mtds

  // #region : public mtds

  // add new node to linked list
  append = (value: T) => {
    // if we are adding the very first element
    if (!this.tail) {
      this.addFirst(value)
    } else {
      const oldTail = this.tail;
      this.tail = new Node_(value);
      oldTail.next = this.tail;
      this.tail.prev = oldTail;
    }
  };

  // adding items to the first of the list
  prepend = (value: T) => {
    if (!this.head) {
      this.addFirst(value);
    } else {
      const newNode = new Node_<T>(value);
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
  }


  delete = (value: T) => {
    console.log("deleting...", value)
    if (this.head == null || this.tail == null) {
      console.log("linked list is empty.")
    } else if (value == this.head.value) {
      // case: if the head is the node we're looking for.

      if (this.head.next) {
        // case: if the head element is the one we're looking for and it has siblings
        const oldHead = this.head;
        this.head = this.head.next;
        oldHead.next = null;
        this.head.prev = null;
      } else {
        // case: if the head element is the one we're looking for and it has siblings
        this.head = null;
        this.tail = null;
      }
    } else if (value == this.tail.value) {
      // case: the tail node is the one we're looking for.
      const oldTail = this.tail;
      this.tail = this.tail.prev;
      this.tail!.next = null;
      oldTail.prev = null;
    } else {
      // case: if the node is neither the head, nor the tail
      // let isFound = false;
      let item = this.head.next;
      while (item) {
        if (item.value == value) {
          // detaching the item
          const prev = item.prev;
          const next = item.next;
          prev!.next = next;
          next!.prev = prev;
          item.prev = null;
          item.next = null;
        }
        item = item.next;
      }
    }
  }

  // printing the entire llist
  print = () => {
    let item = this.head;
    if (!item) {
      console.log("linked list is empty.");
    }
    while (item) {
      console.log(item.value);
      item = item.next;
    }
  };

  // #endregion : public mtds




}

const llist = new LinkedList();
llist.append(1)
llist.append(2)
llist.prepend(3)
llist.prepend(4)
llist.prepend(5)
llist.prepend(6)
llist.prepend(7)
llist.prepend(8)
llist.prepend(9)
llist.print();
llist.delete(6);
llist.print();
llist.delete(1);
llist.print();
llist.delete(9);
llist.print();
llist.delete(3);
llist.print();
llist.append(900)
llist.print();
llist.prepend(900)
llist.print();
