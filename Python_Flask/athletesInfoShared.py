class AthletesInfoShared:
    password = None
    name = None
    surname = None
    email = None
    date_of_birth = None
    

    def __init__(self, p, n, s, e, d):
        self.password = p
        self.name = n
        self.surname = s
        self.email = e
        self.date_of_birth = str(d)