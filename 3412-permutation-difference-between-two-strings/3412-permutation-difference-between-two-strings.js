/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var findPermutationDifference = function(s, t) {
    let S = s.split('')
    let T = t.split('')
    let summ = 0

    for (let i=0; i<s.length; i++) {
        let s_char = S[i]
        summ += Math.abs(i-T.indexOf(s_char))
    }
    return summ
    
};