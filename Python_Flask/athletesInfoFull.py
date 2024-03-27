class Athletes:
    id = None
    email = None
    password = None
    name = None
    surname = None
    date_of_birth = None
    
    def __init__(self, id, e, p, n, s, d):
        self.id = id
        self.email = e
        self.password = p
        self.name = n
        self.surname = s
        self.date_of_birth = str(d)
