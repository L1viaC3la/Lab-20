from A_bileta import Bilete

class BileteUrbane(Bilete):
    def __init__(self, origjin, destinacion, cmim_baze, zona):
        super().__init__(origjin, destinacion, cmim_baze)
        if zona not in [1, 2, 3]:
            raise ValueError("Zona duhet të jetë 1, 2 ose 3.")
        self.zona = zona

    def price(self):
        koef = {1: 1.0, 2: 1.2, 3: 1.4}
        return self.cmim_baze * koef[self.zona]

    def __str__(self):
        return f"Urbane (Zona {self.zona}) | {super().__str__()}"

class BileteNderqytet(Bilete):
    def __init__(self, origjin, destinacion, cmim_baze, km, tarife_per_km):
        super().__init__(origjin, destinacion, cmim_baze)
        if km < 1 or tarife_per_km < 0:
            raise ValueError("KM ≥ 1 dhe tarifa ≥ 0.")
        self.km = km
        self.tarife_per_km = tarife_per_km

    def price(self):
        return self.cmim_baze + self.km * self.tarife_per_km

    def __str__(self):
        return f"Ndërqytet (KM: {self.km}) | {super().__str__()}"

class AbonimStudent(Bilete):
    def __init__(self, origjin, destinacion, cmim_baze, zbritje):
        super().__init__(origjin, destinacion, cmim_baze)
        if not (0 <= zbritje <= 90):
            raise ValueError("Zbritja duhet të jetë midis 0 dhe 90.")
        self.zbritje = zbritje

    def price(self):
        return self.cmim_baze * (1 - self.zbritje / 100)

    def __str__(self):
        return f"Abonim Student (-{self.zbritje}%) | {super().__str__()}"
