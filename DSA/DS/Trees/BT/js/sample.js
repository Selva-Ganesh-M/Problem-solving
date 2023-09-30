class Node{
    #data;
    #left = null;
    #right = null;
    constructor(data){
        this.#data = data;
    }

    get data () {
        return this.#data;
    }

    set data(value){
        this.#data = value;
    }
}

class BT{
    #root = null;
    constructor(){}

    insert(value, curr=null){
        let node = new Node(value);
        if (!this.#root){
            this.#root = node;
        }else{
            curr = curr ? curr : this.#root;
            if (!curr.left){
                curr.left = node;
            }else{}
        }
    }
}