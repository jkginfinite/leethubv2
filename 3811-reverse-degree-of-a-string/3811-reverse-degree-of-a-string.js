/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let Summ = 0;
    let l = 'abcdefghijklmnopqrstuvwxyz'.split('');

    for (let index = 0; index < s.length; index++) {
        Summ+=(26-l.indexOf(s[index]))*(index+1)
    }
    return Summ
}