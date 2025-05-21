/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let Summ = 0;
    let l = 'abcdefghijklmnopqrstuvwxyz'.split('');

    for (let index = 0; index < s.length; index++) {
        let i = s[index];
        let j = l.indexOf(i);

        Summ+=(26-j)*(index+1)
    }
    return Summ
}