from tire.Tire import Tire


class Octoprime(Tire):

    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        sum = 0
        for wheel in self.arr:
            sum += wheel

        if sum >= 3:
            return True
        else:
            return False


if __name__ == "__main__":
    c = Octoprime([1, 0, 1, 1])
    print(c.needs_service())