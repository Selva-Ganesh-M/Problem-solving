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

class BST{
    #root = null;
    constructor(){}

    insert(value, curr=null){
        let node = (value instanceof Node) ? value : new Node(value);
        if (!this.#root){
            this.#root = node;
        }else{
            curr = curr ? curr : this.#root;
            if (node.data < curr.data){
                if (curr.left){
                    this.insert(node, curr.left)
                }else{
                    curr.left = node;
                }
            }else{
                if (curr.right){
                    this.insert(node, curr.right)
                }else{
                    curr.right = node;
                }
            }
        }
    }

    //#region : 'level order traversal'
    bfs(){
        if (!this.#root) return;
        let queue = [this.#root];
        while(queue.length){
            let curr = queue[0];
            queue.splice(0, 1);
            console.log(curr.data)
            curr.left && queue.push(curr.left);
            curr.right && queue.push(curr.right);
        }
    }
    //#endregion : 'level order traversal'

    //#region : 'depth traversal'
    
    inorder(node = null){
        if (!this.#root) return;
        !node && (node = this.#root);
        node.left && this.inorder(node.left);
        console.log(node.data)
        node.right && this.inorder(node.right);
    }
    
    preorder(node = null){
        if (!this.#root) return;
        !node && (node = this.#root);
        console.log(node.data)
        node.left && this.preorder(node.left);
        node.right && this.preorder(node.right);
    }
    postorder(node = null){
        if (!this.#root) return;
        !node && (node = this.#root);
        node.left && this.postorder(node.left);
        node.right && this.postorder(node.right);
        console.log(node.data)
    }

    //#endregion : 'depth traversal'
}

let bst = new BST();
[12, 3, 45, 18, 19, 23, 7].forEach((item)=>bst.insert(item))
// bst.bfs()
// bst.inorder();
// bst.preorder();
// bst.postorder();
