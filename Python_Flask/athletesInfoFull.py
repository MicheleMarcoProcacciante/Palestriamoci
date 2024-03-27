class Athletes:
    id = None
    email = None
    password = None
    name = None
    surname = None
    date_of_birth = None
    

    def __init__(self, id, e, p, n, s, d):
        self.id = id
        self.email = p
        self.password = n
        self.name = s
        self.surname = e
        self.date_of_birth = str(d)
