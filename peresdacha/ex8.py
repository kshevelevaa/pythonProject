def main(s):
    dict={}
    s = s.replace(" ", '')
    s = s.replace("\n", '')
    while s.find('.')!=-1:
        begin = s.find('#')
        s = s[begin+1:]
        keyRight = s.find("to")
        key = s[:keyRight]
        valueRight = s.find(".")
        value = s[keyRight+2:valueRight]
        dict[value] = int( key)
        s= s[valueRight+1:]
    return dict


print(main("begin <sect> store#-2940 to dile. </sect>; <sect> store #-4594 to teusri_453. </sect>;<sect> store #3186 to beed. </sect>; <sect> store#-351 to attige_301. </sect>; end"))


