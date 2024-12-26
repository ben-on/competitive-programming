/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxset = new Set();
    let l = 0
    let ans = 0
    for(let i = 0; i < s.length; i++){
        while(maxset.has(s[i])){
            maxset.delete(s[l]);
            l += 1;
        }
        maxset.add(s[i])
        ans = Math.max(ans, i - l + 1);
    }

    return ans
};