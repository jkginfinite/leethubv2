/**
 * @param {string} s
 * @return {string}
 */
var makeSmallestPalindrome = function(s) {
    let left = 0;
    let right = s.length-1;
    let S = s.split('');

    if (s.length%2===0){
        while (left<right) {
            let L = S[left];
            let R = S[right];

            if (L!==R) {
                let minChar = L<R ? L:R;
                if (L===minChar){
                    S[right]=minChar;
                } else {
                    S[left]=minChar;
                }
            }
            left++;
            right--;
        }
    } else {
        while (left <= Math.floor(s.length/2) && right>=Math.floor(s.length/2)+1) {
            let L = S[left];
            let R = S[right];
            if (L!==R){
                let minChar = L<R ? L:R;
                if (L===minChar) {
                    S[right]=minChar;
                } else {
                    S[left]=minChar;
                }
            }
            left++;
            right--;
        }
    }
    return S.join('');
};