class wektor:
    def __init__(self, cordinates = None):
        self.n = 3 
        if(cordinates == None): cordinates = [0 for i in range(3)]
        self.cord = cordinates
    
    # Subscription (wek[0])
    def __getitem__(self, key: int) -> any:
        return self.cord[key]

    def __setitem__(self, key: int, value: any):
        self.cord[key] = value

    def __mul__(self, other: any) -> 'wektor':
        if isinstance(other, (int, float)):
            return wektor([x * other for x in self.cord])
        elif isinstance(other, wektor):
            return mul(self, other)
        else:
            raise TypeError(f"Unsupported type for multiplication: {type(other)}")    
    def __rmul__(self, other: any) -> 'wektor':
        return self.__mul__(other)
    
    def __add__(self, other: any) -> 'wektor':
        if isinstance(other, (int, float)):
            return wektor([x + other for x in self.cord])
        elif isinstance(other, wektor):
            return wektor([self.cord[i] + other.cord[i] for i in range(self.n)])
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")

    def __str__(self):
        return f"wektor({self.cord})"

    class iterator(int):
        def __new__(cls, value):
            value = int(value)
            value = value % 3
            return super().__new__(cls, value)
        def __add__(self, other):
            return wektor.iterator(super().__add__(other))
        def __sub__(self, other):
            return wektor.iterator(super().__sub__(other))
        
def mul(a:wektor, b:wektor):
    res = wektor()
    for i in range(0, a.n):
        res[i] = a[i] * b[i]
    return res

def skalar(a:wektor, b:wektor):
    res = wektor()
    for i in range(a.n):
        it = wektor.iterator(i)
        res[i] += a[it+1] * b[it+2]
        res[i] -= a[it+2] * b[it+1]
    return res


