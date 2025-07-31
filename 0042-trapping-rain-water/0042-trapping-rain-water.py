class Solution:
    def trap(self, height):
        #use a stack to store the indices of the bars
        #iterate the array
        #while stakc is not empty and height[current]>height[st.top()]
            #it means that the stack element canbe popped, pop the top element as top
            #find the distance between the current element and the element at the top of the stack which is to be filled
            #distance = current - st.top()-1
            #find the bounded height
            # bounded_height = min(height[current],height[st.top()])-height[top]
            #addd the resulting trapped water to the answer ans+=distance*bounded_height
        #push current index to top of the stack
        #move current to the next position
        ans=0
        current=0
        stack = []
        while current<len(height):
            while len(stack)!=0 and height[current]>height[stack[-1]]:
                top=stack[-1]
                stack.pop()
                if len(stack)==0:
                    break
                distance = current-stack[-1]-1
                bounded_height = (min(height[current],height[stack[-1]])-height[top])
                ans+=distance*bounded_height
            stack.append(current)
            current+=1
        return ans