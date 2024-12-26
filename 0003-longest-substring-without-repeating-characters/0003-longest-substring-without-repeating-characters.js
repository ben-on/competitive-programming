/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const freq = Array(26).fill(false);
    let ans = 0
    let l = 0

    for(let i = 0; i < s.length; i++){
        let curPos = s.charCodeAt(i) - 97
        while(freq[curPos]){
            freq[s.charCodeAt(l) - 97] = false
            l += 1
        }
        freq[curPos] = true
        ans = Math.max(ans, i - l + 1);
    }
    return ans
};