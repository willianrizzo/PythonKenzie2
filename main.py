from package.mutability import *
from package.packing_unpaking import *

def mutability_print():
    # number = 3
    # print(f"antes de int_mutablity {number}" )
    # int_mutability(number)
    # print(f"depois de int_mutablity {number}" )

    lista = [1,2,3,4, [1,2,3]]
    print(f"antes de list Mutability {lista}" )
    list_mutability(lista)
    print(f"depois de list Mutability {lista}" )

def packing_unpacking_print():
    req = {
        "user": "Wiu",
        "password":"1234",
        "email":"wiu@wiu.com",
        "sum_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14],
    }

    # func_args(*req["sum_list"])
    func_kwargs(**req["sum_list"])
    

def main():
    # mutability_print()
    packing_unpacking_print()

if __name__ =="__main__":
    main()