import random
def main():


    NUMBER_IN_LINE = 6
    MAX_NUMBER = 45
    MIN_NUMBER = 1
    quick_picks = int(input("how many quick picks"))
    print(quick_picks)
    while quick_picks < 0:
        print("doesnt make any sense")
        quick_picks = int(input("how many quick picks"))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBER_IN_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))




main()