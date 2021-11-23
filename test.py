import sys



def my_func(name, **kwargs):
    # print(args)
    print('------')
    print(kwargs)

    #kean add 1
    
# my_func(1, 2, 3, 4, 5, 6, name = 'jack', age = 18)

person01 = {"name": 'Leon', 'age': 20}
person02 = {"name1": 'Leo', 'age1': 30}

sequence = (2, 4, 6, 8, 20, 12, 14)
# my_func(5, 6, sequence, **person01, **person02)

# a = my_func
# a(5, 6, sequence, **person01, **person02)

def call_func(func, *args, **kwargs):
    func(*args, **kwargs)

call_func(my_func, 1)#, **person02)

# print('--------------another test----------')

# class Kean:
#     def __init__(self, my):
#         self.headerskkk = []



# a = Kean("kean")
# #print(a.headers)
# print(dir(Kean))
# print(dir(a))

# def getheaders(self):
#     return 'getter called'

# def setheaders(self, value):
#     print('----setter called')

# def delheaders(self):
#     print('deletter called')

# Kean.headers = property(getheaders, setheaders, delheaders, "I'm the 'headers' property.")

# print(a.headers)
# a.headers = 'haha'
# a.headersgggggg = 'haha'
# del(a.headers)

