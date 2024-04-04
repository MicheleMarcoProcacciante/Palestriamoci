class TrainingCardsWeb:
    id_scheda = None
    # id_athletes = None
    name = None
    date = None
    exercise_name = None
    series = None
    reps = None
    loads = None
    rest = None
    duration = None
    comment_ = None


    

    def __init__(self, id, n, d, ex_n, ser, rep, load, res, dur, comm):
        self.id_scheda = id
        # self.id_athletes = id_a
        self.name = n
        self.date = str(d)
        self.exercise_name = ex_n
        self.series = ser
        self.reps = rep
        self.loads = load
        self.rest = res
        self.duration = dur
        self.comment_ = comm