import time

from la_cuisine_de_nini.choice.choice_of_day import get_dishes_of_day

if __name__ == "__main__":
    start_time = time.time()
    print('choice of the day', get_dishes_of_day())
    print(time.time() - start_time, 's')
