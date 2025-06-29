/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    function helper(n) {
        if (n%3!==0) return false;
        else if (n===3) return true;
        else return helper(Math.floor(n/3)); /* tail recursion for memory optimization*/
    }
    if (n===1) return true;
    if (n<=0 || n%3 !==0) return false;
    return helper(n);
};