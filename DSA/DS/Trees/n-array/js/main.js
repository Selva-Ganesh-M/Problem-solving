class Node{
    #data;
    #children = [];
    constructor(data){
        this.#data = data
    }

    //#region : 'get and set'
    get data(){
        return this.#data;
    }

    set data(value){
        this.#data = value;
    }

    get children(){
        return this.#children;
    }
    //#endregion : 'get and set'

    addChildren (item){
        this.#children.push((item instanceof Node) ? item : new Node(item))
    }
}

class NArrayTree{
    #root;
    constructor(){
        this.#root = null;
    }

    
}