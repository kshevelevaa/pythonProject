class main:
    x = 'A'

    def fork(self):
        match(self.x):
            case 'A':
                self.x = 'B'
                return 0
            case 'B':
                x = 'C'
                return 1
            case _:
                return KeyError


