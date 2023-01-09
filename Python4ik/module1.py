def arithmetic(a1:float,sym:str,a2:float):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korrutamine, /jagamine
    a1 1st numb
    a2 2nd numb
    str sym tehe
    rtype 
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vastus="Div/0"
        else:
            vastus=eval(str(a1)+sym+str(a2))
    else:
        vastus="Tundmatu tehe!"
    return vastus