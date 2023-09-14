def func_args(*args: list) -> int: #multiplos argumentos, em listas e tuplas
    print(args)
    result = 0
    for x in args:
        result += x
    return result

def func_kwargs(user: str ,password: str,**kwargs: dict) -> None: #Args e Kwards,,, Args são para tuplas e Kwargs para dict(objetos com chave).. username e pass
    print(kwargs)                        #kwargs usa objetos de dicionarios (Json)
    print(user)
    print(password)
                                    #mto usado em endpoints, para filtrar dados enviados