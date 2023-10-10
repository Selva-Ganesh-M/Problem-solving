
Array.prototype.myMap = function(cb){
    let arr = [];
    for (let i = 0; i < this.length; i++) {
        arr.push(cb(this[i], i, this))   
    }
    return arr;
};

const res = [1, 2, 3].myMap((item, i, arr)=>{
    return item*10
})

console.log(res)