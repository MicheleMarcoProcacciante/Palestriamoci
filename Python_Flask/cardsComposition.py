class CardsComposition:
    exercise_name = None
    date = None
    series = None
    reps = None
    loads = None
    rest = None
    duration = None
    comment_ = None
    

    def __init__(self, name, date, ser, rep, l, res, dur, c):
        self.exercise_name = name
        self.date = str(date)
        self.series = ser
        self.reps = rep
        self.loads = l
        self.rest = res
        self.duration= dur
        self.comment_ = c