class DLLNode{
    #_data;
    #_next = null;
    #_prev = null;

    constructor(data){
        this.#_data = data;
    }

    //#region : 'getters and setters'
    
    get data(){
        return this.#_data;
    }

    set data(val){
        this.#_data = val;
    }

    get next(){
        return this.#_next;
    }

    set next(node){
        this.#_next = node;
    }

    get prev(){
        return this.#_prev
    }

    set prev(node){
        return this.#_prev
    }

    //#endregion : 'getters and setters'

}

class DLL {
    #head = null;
    #tail = null;

    constructor(){
        this.#head = null;
        this.#tail = null;
    }

    //#region : 'getters and setters'
    get head () {
        return this.#head;
    }

    set head(node){
        this.#head = node;
    }

    get tail(){
        return this.#tail;
    }

    set tail(node){
        this.#tail = node;
    }
    //#endregion : 'getters and setters'

    //#region : 'static methods'
    
    static print(){
        console.log(`I am static print.`)
    }
    //#endregion : 'static methods'
    
    #createHead (item){
        let node = (item instanceof DLLNode) ? item : new DLLNode(item);
        this.#head = node;
        this.#tail = node;
    }

    print(){
        if (!this.#head){
            console.log(`dll is empty.`)
            return;
        }else{
            let curr = this.#head;
            do{
                // console.log(`${curr.data}`);
                process.stdout.write(curr.data+" ")
                curr = curr.next;
            }
            while (curr);
            process.stdout.write("\n")
        }
    }
    
    get length(){
        if (!this.#head){
            return 0;
        }else{
            let curr = this.#head;
            let count = 0;
            while (curr.next){
                curr = curr.next;
                count++;
            }
            return count;
        }
    }

    push(value) {
        if (!value){
            console.log(`can't push null to dll.`);
            return;
        }
    
        let node = new DLLNode(value);

        //if head is null
        if (!this.#head){
            return this.#createHead(node);
        }
        // if head is present
        else{
            this.#tail.next = node;
            node.prev = this.#tail;
            this.#tail = node;
        }
    }

    unshift(value){

        let node = new DLLNode(value)
        
        // if no head
        if (!this.#head){
            return this.#createHead(node);
        }
        // if head is present
        else{
            node.next = this.#head;
            this.#head.prev = node;
            this.#head = node;
        }
    }

    unshiftRotate(p){
        for (let i=0; i<p; i++){
            let temp = this.#head;
            this.#head = this.#head.next;
            this.#head.prev = null;
            temp.next = null;
            temp.prev = this.#tail;
            this.#tail.next = temp;
            this.#tail = temp;
        }
    }

}

// 1 <= p <= n
let n = 6, p = 6;
let data = [1, 2, 3, 4, 5, 6]
let dll = new DLL();
data.forEach((item)=>dll.push(item));
dll.unshiftRotate(p);
dll.print();

