class AthletesInfoShared:
    email = None
    password = None
    name = None
    surname = None
    date_of_birth = None

    def __init__(self, e, p, n, s, d):
        self.email = e
        self.password = p
        self.name = n
        self.surname = s
        self.date_of_birth = str(d)
