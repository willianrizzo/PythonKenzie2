import copy

def int_mutability(params_number: int) -> None:
    params_number = 10
    print(f"Dentro de int_mutablity {params_number}" )

def list_mutability(params_list: list) -> None:
    # list_copy = params_list.copy()
    # list_copy = params_list[:]
    # list_copy = [*params_list]
    list_copy = copy.deepcopy(params_list)

    list_copy[4][0] = 20

    print(f"Dentro de list Mutabilty {list_copy}")