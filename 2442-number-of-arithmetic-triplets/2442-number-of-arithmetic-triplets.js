/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    let count=0;
    let L = nums.length
    for (let i=0; i<L; i++) {
        for (let j=i+1; j<L; j++) {
            for (let k=j+1; k<L; k++) {
                if ((nums[j]-nums[i]===diff) && (nums[k]-nums[j]===diff)) {
                    count+=1
                }
            }
        }
    }
    return count
    
};