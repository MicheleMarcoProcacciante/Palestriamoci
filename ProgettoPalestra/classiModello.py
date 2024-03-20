class Athletes:
    id = None
    password = None
    name = None
    surname = None
    email = None
    date_of_birth = None
    
    def __init__(self, id, p, n, s, e, d):
        self.id = id
        self.password = p
        self.name = n
        self.surname = s
        self.email = e
        self.date_of_birth = str(d)
