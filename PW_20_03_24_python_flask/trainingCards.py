class TrainingCards:
    id = None
    id_athletes = None
    name = None
    date = None
    

    def __init__(self, id, id_a, n, d):
        self.id = id
        self.id_athletes = id_a
        self.name = n
        self.date = str(d)