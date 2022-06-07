class main:
    x = 'A';
    def edit(self):
        match(self.x):
            case 'A':
                self.x = 'F'
                return 2
            case 'B':
                raise KeyError
            case 'C':
                self.x = 'D'
                return 4
            case 'D':
                self.x = 'B'
                return 7
            case 'E':
                raise KeyError
            case 'F':
                raise KeyError
            case 'G':
                raise KeyError
    def chalk(self):
        match(self.x):
            case 'A':
                self.x = 'B'
                return 0
            case 'B':
                raise KeyError
            case 'C':
                raise  KeyError
            case 'D':
                raise KeyError
            case 'E':
                self.x = 'F'
                return 8
            case 'F':
                raise KeyError
            case 'G':
                raise KeyError
    def rig(self):
        match(self.x):
            case 'A':
                self.x = 'E'
                return 1
            case 'B':
                self.x = 'C'
                return 3
            case 'C':
                self.x = 'E'
                return 5
            case 'D':
                self.x = 'E'
                return 6
            case 'E':
                raise KeyError
            case 'F':
                self.x = 'G'
                return 9
            case 'G':
                raise KeyError


o = main()
o.chalk() # 0
o.rig() # 3
o.edit() # 4
o.edit() # 7
o.rig() # 3
o.edit() # 4
o.rig() # 6
o.chalk() # 8
#o.chalk() # KeyError
o.rig() # 9