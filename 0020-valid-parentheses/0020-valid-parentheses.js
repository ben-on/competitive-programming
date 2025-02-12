/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const open_map = new Map([
        [')', '('],
        ['}', '{'],
        [']', '['],

    ]);

    const stack = [];

    for(let char of s){
        if (!open_map.has(char)){
            stack.push(char)
        }
        else{
            if (stack.length == 0 || stack[stack.length - 1] != open_map.get(char)){return false;}
            stack.pop()
        }
    }


    return stack.length == 0;
    
};