
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        #initialize a hashmap to store tree nodes
        #iterate through each element innums
        #calculate coordinates by dividing the current element by 10
        #calculate value by taking the remainder of the element when divided by 10
        #store the coordinates as the key and value as the value in map

        #initlaize an integer variable sum with 0
        #call the helper function dfs(rootCoordinates,preSum, sum, map) with
        #rootCoordinates set to nums[0]/10
        #preSum set to 0
        #sum passed by reference
        #return value of sum


        #helper function dfs(rootCoordinates, preSum, sum, map)
        #calculate the level and position from rootCoordinates
        #level is obtained b dividing rootCoordinates by 10
        #position is obtained by taking the remainder of rootCoordinates when divided by 10
        #determine the coordinates of the left and right children
        #left is caculated as (level+1)*10+position*2-1
        #right is calculated as (level+1)*10+position*2

        #updatecurrSum by adding the value of the curren node to preSum
        #if map does not contain both left and right coordinates
        #add currSum to sum
        #return from the function

        #if left exists in map, call dfs(levft, currSum, sum, map)
        #if right exists in map, call dfs(right, currSum, sum, map)
        coord_map = {}
        for element in nums:
            coordinates = element//10
            value = element%10
            coord_map[coordinates] = value
        
        return self.dfs(nums[0]//10,0,coord_map)

    def dfs(self,root_coordinates,pre_sum,coord_map):
        #find the level and position values from the coordinates
        level = root_coordinates//10
        position = root_coordinates%10

        #find out the left child and. right child positions of the tree
        left = (level+1)*10+position*2-1
        right = (level+1)*10+position*2
        curr_sum = pre_sum+coord_map[root_coordinates]

        #if left child and right child do not exist, return
        if not left in coord_map and not right in coord_map:
            return curr_sum

        #else
        left_sum = (self.dfs(left,curr_sum,coord_map) if left in coord_map else 0)
        right_sum = (self.dfs(right,curr_sum,coord_map) if right in coord_map else 0)

        return left_sum+right_sum        