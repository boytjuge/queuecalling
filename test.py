
def sol(s1:str , s2:str) -> bool:
    return bool(set(s1) & set(s2))



print(sol("bank","kanb"))
