class CardsComposition:
    id = None
    id_trainingCards = None
    id_exercises = None
    series = None
    reps = None
    loads = None
    rest = None
    duration = None
    comment = None
    

    def __init__(self, id, id_t, id_e, s, rep, l, res, d, c):
        self.id = id
        self.id_trainingCards = id_t
        self.id_exercises = id_e
        self.series = s
        self.reps = rep
        self.loads = l
        self.rest= res
        self.duration = d
        self.comment = c