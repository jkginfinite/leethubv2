class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        array = []
        while i<=n:
            if i%3==0 and i%5==0 and i>0:
                _ = "FizzBuzz"
            elif i%3==0 and i>0:
                _ = "Fizz"
            elif i%5==0 and i>0:
                _ = "Buzz"
            else:
                _ = str(i)
            array.append(_)
            i+=1
        return array
        