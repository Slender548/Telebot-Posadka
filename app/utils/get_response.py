def get_response(text: str) -> str:
    text=text.replace(",", ".").split("\n")
    #D max = D + ES
    #D min = D + EI
    #d max = D + es
    #d min = D + ei
    #TD = Dmax-Dmin
    #Td = dmax-dmin
    #Smax = Dmax-dmin
    #Smin = Dmin-dmax
    #Nmax = dmax-Dmin
    #Nmin = dmin-Dmax
    #text[0] = D
    #text[1] = ES
    #text[2] = EI
    #text[3] = es
    #text[4] = ei
    Dmax = float(text[0])+float(text[1])
    Dmin = float(text[0])+float(text[2])
    dmax = float(text[0])+float(text[3])
    dmin = float(text[0])+float(text[4])
    TD = format(float(Dmax)-float(Dmin), ".3f")
    Td = format(float(dmax)-float(dmin), ".3f")
    Smax = format(float(Dmax)-float(dmin), ".3f")
    Smin = format(float(Dmin)-float(dmax), ".3f")
    Smid = format((float(Smax)+float(Smin))/2, ".3f")
    Nmax = format(float(dmax)-float(Dmin), ".3f")
    Nmin = format(float(dmin)-float(Dmax), ".3f")
    Nmid = format((float(Nmax)+float(Nmin))/2, ".3f")
    if (Dmin>dmax):
        case = 2
        answer = "Это зазор"
    elif (Dmax<dmin):
        case = 3
        answer = "Это натяг"
    else:
        case = 1
        answer = "Это общее положение"
    response = f"""
Ответ на ваш вариант:
Dmax = D + ES = {text[0]} + {text[1]} = {Dmax}
Dmin = D + EI = {text[0]}+ {text[2]} = {Dmin}
TD = Dmax - Dmin = {Dmax} - {Dmin} = {TD}
TD = ES - EI = {text[1]} - {text[2]} = {TD}
dmax = D + es = {text[0]} + {text[3]} = {dmax}
dmin = D + ei = {text[0]} + {text[4]} = {dmin}
Td = dmax - dmin = {dmax} - {dmin} = {Td}
Td = es - ei = {text[3]} - {text[4]} = {Td}"""
    match case:
        case 1:
            response += "\n"+answer + f"""
Smax = Dmax - dmin = {Dmax} - {dmin} = {Smax}
Nmax = dmax - Dmin = {dmax} - {Dmin} = {Nmax}"""
        case 2:
            response += "\n"+answer + f"""
Smax = Dmax - dmin = {Dmax} - {dmin} = {Smax}
Smin = Dmin - dmax = {Dmin} - {dmax} = {Smin}
Smid = (Smax + Smin)/2 = ({Smax} + {Smin}) / 2 = {Smid}"""
        case 3:
            response += "\n"+answer + f"""
Nmax = dmax - Dmin = {dmax} - {Dmin} = {Nmax}
Nmin = dmin - Dmax = {dmin} - {Dmax} = {Nmin}
Nmid = (Nmax + Nmin)/2 = ({Nmax} + {Nmin}) / 2 = {Nmid}"""
    return response