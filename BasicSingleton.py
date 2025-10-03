class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.name = name
            self.initialized = True
            print(f"Singleton instance created: {self.name}")

# Usage
s1 = Singleton("First")
s2 = Singleton("Second")  # This won't reinitialize

print(f"s1 is s2: {s1 is s2}")
print(f"s1.name: {s1.name}, s2.name: {s2.name}")
