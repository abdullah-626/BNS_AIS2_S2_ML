# def user_info(name:str, age:int | None = None) -> str : #parametars 
#     '''
#     print hello name , ur age is age
#     '''
#     return f"hello {name}, ur age is {age}"

# print(user_info(name = "abdo", age = 10)) #arguments


# def func(item, lst = None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst
# print(func('1'))
# print(func('2'))
# print(func('3'))


# def func_1(*args):
#     print(args)
#     print(type(args))

# func_1('depi', 'ai', 'ml',1,300.1)


# def func_1(**args):
#     print(args)
#     print(type(args))

# func_1(key1 = 'depi',key2 = 'ai',key3 = 'ml')


sum = lambda x:x+10 
print(sum(1))