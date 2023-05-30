import copy
# list1 = [1, 2, 3, [4, 5, 6]]
# # copytext = list1.copy()
# # copytext[3].append(7)
# # print(list1)
# # print(copytext)

# # list1.append(8)
# # print(list1)
# # print(copytext)

# shallow_copy = copy.copy(list1)
# shallow_copy[3].append(8)
# print(list1)
# print(shallow_copy)

# deepcopy = copy.deepcopy(list1)
# deepcopy[3].append(9)

# print(list1)
# print(deepcopy)


class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
a = Point(1, 2)
b = copy.copy(a)
a.x = 3
print(a)
print(b)