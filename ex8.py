def main(s):
    dict={}
    s=s.replace(" ", '')
    s=s.replace("\n", '')
    s=s.replace("'", "")
    while s.find("(") != -1:
        keyLeft = s.find("(")+1
        keyRight = s.find(")")
        key = s[keyLeft:keyRight]
        valueLeft=s.find("=")+1
        valueRight= s.find(";")
        value=s[valueLeft:valueRight]
        dict[key] = value
        s = s[valueRight+6:]
    return dict


print(main("{{ do variable q(tixe) = `maan_715;done; do variable q(azaaor)=`remage_577; done; do variable q(anonte_286) =`usbeen; done; }}"))
