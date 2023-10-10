function add(x){
    if (x){
        return (y)=>{
            if (y) return add(x+y)
            else return x
        }
    }else return x
}

console.log(add(1)(2)(5)())