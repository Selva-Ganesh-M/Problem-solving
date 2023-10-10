function curryPrep(fn){
    return curry = (...args) => {
        if (args.length >= fn.length){
            return fn(...args);
        }else{
            return (...next)=>{
                return curry(...args, ...next);
            }
        }
    }
}

add = (a, b, c) => {
    return a+b+c
}

curriedAdd = curryPrep(add);
console.log(curriedAdd(1)(2)(3))