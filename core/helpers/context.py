class Context:
    def __init__(self):
        self.data = {}
    
    def set(self, key, value):
        self.data[key] = value 
    
    def get(self,key):
        return self.data.get(key, None)