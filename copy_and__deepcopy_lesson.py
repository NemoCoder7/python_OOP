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


# class Point():
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
    
# a = Point(1, 2)
# b = copy.copy(a)
# a.x = 3
# print(a)
# print(b)


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        
        return result

