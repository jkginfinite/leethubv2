/**
 * @param {number[]} digits
 * @return {number}
 */
var totalNumbers = function(digits) {
    function getPermutations(arr, length) {
        if (length==1) return arr.map(d=>[d]);
        const perms = [];
        arr.forEach((val,idx) => {
            const remaining = arr.slice(0,idx).concat(arr.slice(idx+1));
            const innerPerms = getPermutations(remaining, length - 1);
            innerPerms.forEach(p => perms.push([val, ...p]));
        });
        return perms;
    }

    const perms = getPermutations(digits,3).map(p => parseInt(p.join("")));

    const counted = new Set();

    function helper(perms, count, countedSet) {
        if (perms.length===0) return count;
        const val = perms.shift();
        if (val%2===0 && val>=100 && !countedSet.has(val)) {
            countedSet.add(val);
            count+=1;
        } else {
            countedSet.add(val);
        }
        return helper(perms, count, countedSet);
    }
    return helper(perms, 0, counted);
};