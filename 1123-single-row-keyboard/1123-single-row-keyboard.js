/**
 * @param {string} keyboard
 * @param {string} word
 * @return {number}
 */
var calculateTime = function(keyboard, word) {
    let last = 0;
    let keyboardList = keyboard.split("");
    let wordList = word.split("");
    let moves = 0;

    for (let i=0; i<wordList.length;i++){
        let letter = wordList[i]
        let curr = keyboardList.indexOf(letter)
        moves+= Math.abs(curr-last)
        last = curr
    }
    return moves;


};