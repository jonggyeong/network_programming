str = input("input word: ")
index = str.find('a') + 1
final = len(str)-index

print(str[:index])
print(str[index:])