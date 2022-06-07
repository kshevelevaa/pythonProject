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

print(main("{<: option q(esesbi_83)==> querte;:> <: option q(onaen_588)==>lein_938; :> <: option q(raraer)==> inre; :>}"))
