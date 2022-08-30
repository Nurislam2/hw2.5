from decouple import config
import random
def start_game():
    count=0
    my_money = config("MY_MONEY", cast=int)
    restart_game="да"
    while restart_game=="да" or restart_game=="yes":
        if my_money<=0:
            print("у вас законлись деньги")
            break
        print(f"у вас на считу {my_money}")
        numbers=[i for i in range(1,31)]
        print("выберите число от 1 до 30")
        n=int(input())
        print("ваша ставка ")
        m=int(input())
        if n==random.choice(numbers):
            count+=m*2
            my_money+=m*2
            print(f"выигрыш")
        else:
            my_money-=m
            count-=m
            print(f"проигрыш")
        restart_game=input("желаете продолжить ")
    if count<0:
        print(f"вы в проигрыше на {count}")
    else:
        print(f"вы в выигрыше на {count}")
