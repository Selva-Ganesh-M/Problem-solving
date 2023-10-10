function operation(operator){
    return function(a){
        return function(b){
            switch(operator){
                case "add":
                    return a+b;
                case "mul":
                    return a*b
                default:
                    return 0;
            }
        }
    }
}


multiplier = operation("mul")
console.log(multiplier(5) (5))
console.log(multiplier(4)(4))
