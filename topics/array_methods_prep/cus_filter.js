Array.prototype.myFilter = function (cb) {
    let arr = [];
    for (let i = 0; i < this.length; i++) {
        if (cb(this[i], i, this)){ 
            arr.push(this[i])
        }
    }    
    return arr;
}

let arr = [1, 2, 3, 4]
let ans = arr.myFilter((item, i, arr)=>{
    return item % 2==0
})

console.log(ans)