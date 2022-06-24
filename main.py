class Array:
    def __init__(self, a = []):
        self.a = a
    def bubble_sort(self):
        length = len(self.a)
        for i in range(0, length-1):
            for j in range(0, length-1-i):
                 if self.a[j] > self.a[j+1]:
                      self.a[j], self.a[j+1] = self.a[j+1], self.a[j]
        return self.a

