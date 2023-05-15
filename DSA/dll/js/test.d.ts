
export interface INode_<T> {
  prev: INode_<T> | null;
  next: INode_<T> | null;
}

export interface ILinkedList<T> {
  append: (value: T) => void;
  print: () => void;
}
