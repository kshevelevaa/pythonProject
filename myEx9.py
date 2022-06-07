class main:
    x = 'A'

    def boost(self):
        match (self.x):
            case 'A':
                self.x = 'B'
                print('0')
                return 0
            case 'B':
                self.x = 'C'
                print('2')
                return 2
            case 'C':
                self.x = 'F'
                print('4')
                return 4
            case 'D':
                self.x = 'E'
                print('6')
                return 6
            case 'E':
                self.x = 'F'
                print('8')
                return 8
            case _:
                print("KeyError")
                return KeyError

    def hoard(self):
        match (self.x):
            case 'C':
                self.x = 'D'
                print('3')
                return 3
            case 'A':
                self.x = 'G'
                print('1')
                return 1
            case _:
                print("KeyError")
                return KeyError

    def hurry(self):
        match (self.x):
            case 'C':
                self.x = 'G'
                print('5')
                return 5
            case 'D':
                self.x = 'G'
                print('7')
                return 7
            case 'F':
                self.x = 'G'
                print('9')
                return 9
            case _:
                print("KeyError")
                return KeyError


o = main()
o.boost() # 0
o.boost() # 2
o.hoard() # 3
o.boost() # 6
o.boost() # 8
o.boost() # KeyError
o.hurry() # 9

