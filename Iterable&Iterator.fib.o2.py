class fib :
    def __init__(self, end):
        self.a=0
        self.b=1
        self.end=end
    def __iter__(self):
        return self  
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b 
        if self.a> self.end:
            raise StopIteration
        return self.a
    
fib1=fib(5000) 
for item in fib1:
    print(item, end='\t')   