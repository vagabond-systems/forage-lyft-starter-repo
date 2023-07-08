from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, worn_counts):
        self.worn_counts = worn_counts

    def tyres_needs_service(self):
        max_worn_count_for_carrigan = 0.9
        return any(worn_count >= max_worn_count_for_carrigan for worn_count in self.worn_counts)
        