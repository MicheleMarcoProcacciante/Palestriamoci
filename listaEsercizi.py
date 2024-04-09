class ListaEsercizi:
    id = None
    nome_esercizio = None
    is_aerobic = None
    

    def __init__(self, id, n_es, aer):
        self.id = id
        self.nome_esercizio = n_es
        self.is_aerobic = aer