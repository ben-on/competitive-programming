/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = [];
    const ans = new Array(temperatures.length).fill(0);

    for(let i = 0; i < temperatures.length; i++){
        while(stack.length > 0 && temperatures[stack[stack.length - 1]] < temperatures[i]){
            day = stack.pop();
            ans[day] = i - day;

        }
        stack.push(i);
    }

    return ans;
    
};