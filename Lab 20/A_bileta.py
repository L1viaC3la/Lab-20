class Bilete:
    def __init__(self, origjin: str, destinacion: str, cmim_baze: float):
        if not origjin or not destinacion:
            raise ValueError("Origjina dhe destinacioni nuk mund të jenë bosh.")
        if cmim_baze < 0:
            raise ValueError("Çmimi bazë duhet të jetë ≥ 0.")
        self.origjin = origjin
        self.destinacion = destinacion
        self.cmim_baze = cmim_baze

    def price(self) -> float:
        return self.cmim_baze

    def __str__(self) -> str:
        return f"Bilete: {self.origjin} → {self.destinacion} | Bazë: {self.cmim_baze:.2f} L"
