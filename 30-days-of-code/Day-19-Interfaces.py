
class AdvancedArtimetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calulator(AdvancedArtimetic):
    def divisorSum(self, n):

        sum = 0

        for i in range(1, (n+1)):
            if n % i == 0:
                sum += i

        return sum



n = int(input())
my_calculator = Calulator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
