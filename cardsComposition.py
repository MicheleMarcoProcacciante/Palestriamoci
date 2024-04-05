class CardsComposition:
    id_scheda = None
    exercise_name = None
    date = None
    series = None
    reps = None
    loads = None
    rest = None
    duration = None
    comment_ = None
    

    def __init__(self, id_sc, name, date, ser, rep, l, res, dur, c):
        self.id_scheda = id_sc
        self.exercise_name = name
        self.date = str(date)
        self.series = ser
        self.reps = rep
        self.loads = l
        self.rest = res
        self.duration= dur
        self.comment_ = c
