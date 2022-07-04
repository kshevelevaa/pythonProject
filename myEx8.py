# def main(s):
#     s = s.replace(' ', '')
#     s = s.replace('\n', '')
#     dict = {}
#     while s.find("<sect>") != -1:
#         left = s.find('#(') + 2
#         right = s.find(')')
#         value = s[left:right]
#         values = value.split('.')
#         newLeft = s.find('=:') + 3
#         newRight = s.find('.</')
#         name = s[newLeft:newRight]
#         dict[name] = values
#         s = s[3:]
#         s = s[s.find("<sect"):]
#     return dict
def main(s):
    dict={}
    s = s.replace(" ", "")
    s = s.replace("\n", '')
    s = s.replace("<:", '')
    s = s.replace(":>", '')
    while s.find("=")!= -1:
        valueLeft = s.find("(")
        valueRigth = s.find(")")
        value = s[valueLeft+1:valueRigth]
        s=s[valueRigth+1:]
        keyLeft = s.find(">")
        keyRight = s.find(";")
        key = s[keyLeft+1:keyRight]
        dict[key] = value
        s=s[keyRight+1:]
    return dict


def main2(s):
    dict={}
    s=s.replace(" ", '')
    s=s.replace("\n", '')
    while s.find(".<")!= -1:
        leftKey=s.find(":")
        rightKey=s.find(".<")
        key=s[leftKey+2:rightKey]
        leftValues=s.find('(')
        rightValues=s.find(')')
        values=s[leftValues+1: rightValues+1]
        print(values)
        massiv = []
        while values.find(")")!=-1:
            rightValue=values.find(".")
            skobka=values.find(")")
            if rightValue==-1:
                value=values[0:skobka]
                values=""
            elif( rightValue!=-1):
                value = values[0:rightValue]
            values = values[rightValue+1:]
            massiv.append(value)
        dict[key] = massiv
        s=s[rightKey+2:]
    return dict

#print(main("{<: option q(esesbi_83)==> querte;:> <: option q(onaen_588)==>lein_938; :> <: option q(raraer)==> inre; :>}"))
print(main2("do<sect> #( gear_255 . cedi_385 . ererer . teanis )=:`teate_923.</sect>;<sect> #( aenedra_829 . biti . anorte . aeder_977 )=: `enso.</sect>; done"))