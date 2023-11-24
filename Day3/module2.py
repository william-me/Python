#imports from module.py file
import module

#module is a module containing square function
result = module.square(5)

result_add = module.add(5,10)
result_subtract = module.subtract(15,10)

print(result) #prints 125
print(module.pi) #prints 3.14
print(f"Addition: {result_add}") #prints 15
print(f"Subtraction: {result_subtract}") #prints 5