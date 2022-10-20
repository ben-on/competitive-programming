class RandomizedCollection:

		def __init__(self):
			self.multi = []

		def insert(self, val: int) -> bool:
			if val in self.multi:
				self.multi.append(val)
				return False

			self.multi.append(val)
			return True

		def remove(self, val: int) -> bool:
			if val in self.multi:
				self.multi.remove(val)
				return True

			return False

		def getRandom(self) -> int:
			return random.choice(self.multi)




# class RandomizedCollection:

#     def __init__(self):
#         self.multi={}

#     def insert(self, val: int) -> bool:
#         if val in self.multi:
#             self.multi[val]+=1
#             return False
#         else:
#             self.multi[val]=1
#             return True

#     def remove(self, val: int) -> bool:
#         if val in self.multi:
#             if self.multi[val] == 1:
#                 del self.multi[val]
#             else:
#                 self.multi[val] -= 1
#             return True
#         else:
#             return False

#     def getRandom(self) -> int:
#         new=list(self.multi.keys())
#         return random.choice(new)
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()