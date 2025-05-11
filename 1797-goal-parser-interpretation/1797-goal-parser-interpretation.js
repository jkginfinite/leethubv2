/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    let r = '';
    let i = 0;

    while (i < command.length) {
        if (command[i] === 'G') {
            r += 'G';
            i += 1;
        } else if (command[i] === '(' && command[i + 1] === ')') {
            r += 'o';
            i += 2;
        } else if (command.slice(i, i + 4) === '(al)') {
            r += 'al';
            i += 4;
        }
    }

    return r;
};
