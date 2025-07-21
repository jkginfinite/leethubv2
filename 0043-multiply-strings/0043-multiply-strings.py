class Solution:
    def represent(self, num):
        d = {}
        v=1
        for i in range(len(num)-1,-1,-1):
            d[v] = num[i]
            v=v*10
        return d
    
    def convert(self,d):
        number = 0
        for key in list(d.keys())[::-1]:
            for i in range(10):
                if str(i)==d[key]:
                    number+=i*key
        return number
            
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.convert(self.represent(num1))
        n2 = self.convert(self.represent(num2))
        return str(n1*n2)
        