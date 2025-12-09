class BrowserHistory:
    def __init__(self, homepage: str):
        self.b = []
        self.f = []
        self.curr = homepage
        
    def visit(self, url: str) -> None:
        prev = self.curr
        self.curr = url
        self.b.append(prev)
        self.f = []

    def back(self, steps: int) -> str:
        while steps>0 and self.b:
            self.f.append(self.curr)
            self.curr = self.b.pop()
            steps-=1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps>0 and self.f:
            self.b.append(self.curr)
            self.curr = self.f.pop()
            steps-=1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)