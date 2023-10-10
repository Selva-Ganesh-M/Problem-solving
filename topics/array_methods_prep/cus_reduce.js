// let arr = [1, 2, 3]
// let sum = arr.reduce((acc, item, i, arr)=>{
    //     return acc + item
    // }, 0)
    
Array.prototype.myReduce = function (cb, initialState) {
    let acc = initialState || this[0];
    let x = initialState ? 0 : 1;
    for (let i = x; i < this.length; i++) {
        acc = cb(acc, this[i], i, this)
    }
    return acc;
}
    
let arr = [1, 2, 3]
let ans = arr.myReduce((acc, item, i, arr)=>{
    return acc + item
}, 0)
console.log(ans)