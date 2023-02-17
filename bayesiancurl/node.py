class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.values = ["T", "F"]
        self.parents = []
        self.probs = {}

    def add_parent(self, parent):
        self.parents.append(parent)

    # Override para setear probabilidades a elementos padres (superiores)
    # se debe dar la probabilidad del elemento en valor true
    def create_probs(self, prob: float):
        p_true = prob
        p_false = 1 - prob
        self.probs = {"T": p_true, "F": p_false}

    ## Crear probabilidad para nodos hijos
    def create_probs_son(self, p_true: float, p_false: float):

        self.probs["T"] = {"T": p_true, "F": 1 - p_true}
        self.probs["F"] = {"T": p_false, "F": 1 - p_false}