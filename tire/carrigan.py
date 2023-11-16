from tire.Tire import Tire


class Carrigan(Tire):

    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        for wheel in self.arr:
            if wheel >= 0.9:
                return True

        return False


if __name__ == "__main__":
    c = Carrigan([0.1, 0, 0.89, 1])
    print(c.needs_service())