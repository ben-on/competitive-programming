class LFUCache:

    def __init__(self, capacity: int):
        self.frequencies = defaultdict(lambda: OrderedDict())
        self.values = defaultdict(int)
        self.capacity = capacity
        self.minfreq = float('inf')
        
    def get(self, key: int) -> int:
        f = self.values[key]

        if not f: 
            del self.values[key]
            return -1
        
        self.frequencies[f+1][key] = self.frequencies[f][key]
        self.values[key] = f+1
        
        del self.frequencies[f][key]
        
        if self.minfreq == f and not len(self.frequencies[f]):
            self.minfreq = f+1
            
        return self.frequencies[f+1][key]

    def put(self, key: int, value: int) -> None:
        if not self.capacity: return      
        
        if len(self.values) == self.capacity: 
            if not self.values[key]:
                k = self.frequencies[self.minfreq].popitem(last=False)
                del self.values[k[0]] 
                
        f = self.values[key]
        self.values[key] += 1
        
        if f != 0:
            self.frequencies[f+1][key] = value
            del self.frequencies[f][key]
            
            if self.minfreq == f and not len(self.frequencies[f]):
                self.minfreq = f+1
        else: 
            self.frequencies[f+1][key] = value    
        
        self.minfreq = min(self.values[key], self.minfreq)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)