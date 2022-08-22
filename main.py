from functools import reduce

def add_num(x,y):
    return x+y

# reference ...https://docs.python.org/3/library/__main__.html?highlight=main#module-__main__
if __name__ == "__main__":
    a = [10,200,30,10]
    print(reduce(add_num,a))
    print("Hello Git")