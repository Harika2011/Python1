class TupleSumFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_positions(self, target_sum):
        positions = []
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == target_sum:
                    positions.append((i, j))
        return positions
    
def main():
    numbers = (10,20,30,40,50,60,70,80,90)
    target_sum = int(input("Enter the target sum :"))
    finder = TupleSumFinder(numbers)
    result = finder.find_positions(target_sum)
    if result:
        print("positions of elemnts that add up to the target sum : ")
        for pos in result:
            print(pos)
    else:
        print("No pairs of number found that add up to the target sum")

main()
