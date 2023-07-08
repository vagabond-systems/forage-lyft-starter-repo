from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, worn_counts):
        self.worn_counts = worn_counts

    def tyres_needs_service(self):
        max_worn_sum_for_octoprime = 3
        return sum(self.worn_counts) >= max_worn_sum_for_octoprime