#random 6 number generator using previous winning nums



import random
import time


def lottery_pick():

    print('Welcome to Magic Lotto PICK 6')


    num_pool = [20, 32, 2, 18, 34, 22, 8, 39, 47, 18, 45, 9, 11, 40, 38, 48, 17, 44, 47, 29, 23, 22, 49, 15, 47, 51, 32, 14, 49, 22, 3, 27, 41, 40, 44, 19, 49, 43, 3, 35, 44, 37, 20, 51, 26, 23, 41, 42, 3, 37, 29, 1, 40, 41, 4, 36, 30, 44, 52, 43, 21, 29, 14, 19, 7, 39, 16, 26, 41, 43, 4, 9, 33, 13, 39, 4, 9, 18, 43, 52, 40, 6, 14, 25, 1, 7, 22, 15, 31, 29, 1, 29, 26, 14, 11, 25, 2, 29, 28, 10, 46, 14, 9, 23, 20, 14, 10, 18, 46, 3, 23, 21, 2, 41, 18, 1, 31, 36, 29, 35, 16, 5, 25, 13, 36, 50, 51, 37, 17, 25, 24, 36, 11, 14, 48, 13, 41, 20, 14, 42, 2, 21, 28, 36, 24, 8, 49, 2, 27, 18, 33, 45, 46, 23, 27, 29, 48, 27, 2, 18, 23, 6, 16, 5, 14, 13, 17, 19, 46, 21, 12, 26, 17, 8, 13, 30, 18, 4, 42, 8, 40, 37, 17, 30, 5, 6, 28, 27, 34, 16, 42, 6, 7, 6, 36, 31, 17, 1, 12, 43, 29, 44, 17, 42, 6, 2, 40, 4, 39, 37, 41, 35, 42, 10, 13, 1, 14, 46, 30, 22, 27, 4, 48, 44, 45, 46, 17, 22, 47, 35, 45, 42, 19, 36, 50, 27, 25, 48, 52, 30, 2, 10, 48, 15, 6, 27, 12, 14, 16, 47, 29, 8, 30, 14, 6, 46, 7, 3, 14, 28, 8, 16, 45, 13, 23, 5, 49, 31, 11, 24, 46, 48, 9, 40, 38, 35, 48, 22, 1, 2, 36, 31, 28, 6, 39, 26, 38, 19, 10, 5, 36, 48, 11, 12, 19, 11, 50, 35, 49, 45, 49, 5, 36, 22, 15, 47, 5, 14, 13, 25, 12, 28, 43, 44, 7, 37, 51, 13, 49, 15, 26, 35, 21, 13, 10, 12, 32, 39, 13, 50, 26, 31, 40, 46, 18, 36, 35, 10, 24, 33, 2, 46, 35, 13, 28, 11, 10, 3, 50, 36, 30, 52, 28, 17, 49, 18, 21, 31, 23, 35, 1, 22, 26, 6, 17, 18, 3, 31, 24, 1, 12, 49, 32, 50, 49, 11, 19, 1, 21, 42, 44, 40, 26, 6, 5, 8, 47, 14, 23, 41, 3, 17, 11, 2, 23, 5, 52, 24, 38, 17, 30, 32, 42, 36, 40, 22, 19, 8, 51, 39, 30, 28, 5, 9, 29, 15, 31, 12, 11, 6, 49, 17, 36, 26, 1, 14, 21, 33, 9, 38, 32, 27, 40, 2, 28, 18, 45, 46, 1, 41, 16, 17, 18, 52, 19, 49, 6, 50, 47, 52, 7, 44, 21, 6, 50, 16, 34, 19, 18, 26, 42, 40, 48, 7, 24, 21, 6, 15, 3, 40, 32, 18, 19, 24, 28, 50, 52, 5, 27, 35, 41, 28, 18, 24, 30, 12, 50, 46, 48, 27, 10, 29, 23, 49, 31, 45, 41, 47, 39, 34, 31, 33, 44, 43, 24, 37, 3, 35, 31, 43, 28, 2, 34, 33, 23, 46, 48, 3, 42, 49, 20, 10, 19, 39, 6, 41, 8, 24, 10, 16, 14, 27, 29, 52, 22, 42, 11, 2, 17, 18, 47, 25, 12, 8, 32, 35, 41, 23, 38, 34, 18, 26, 5, 49, 24, 18, 17, 7, 51, 24, 43, 13, 50, 25, 32, 41, 20, 39, 26, 34, 44, 35, 7, 2, 25, 51, 48, 3, 29, 25, 26, 16, 3, 52, 39, 36, 43, 38, 22, 37, 2, 49, 42, 36, 28, 3, 30, 21, 46, 51, 24, 47, 39, 51, 1, 38, 11, 5, 38, 25, 49, 32, 28, 12, 3, 47, 42, 43, 46, 6, 19, 38, 45, 1, 18, 5, 39, 14, 52, 32, 37, 36, 20, 23, 44, 27, 23, 45, 38, 9, 43, 25, 21, 33, 22, 5, 1, 44, 28, 24, 5, 42, 15, 49, 43, 18, 50, 29, 22, 32, 33, 38, 27, 35, 25, 1, 19, 24, 7, 51, 11, 25, 44, 11, 16, 8, 10, 35, 2, 33, 43, 19, 31, 52, 22, 7, 34, 37, 3, 24, 37, 2, 7, 10, 33, 44, 49, 19, 4, 21, 10, 31, 35, 16, 27, 51, 9, 37, 24, 51, 1, 44, 7, 29, 30, 25, 3, 4, 1, 21, 32, 35, 10, 33, 39, 42, 36, 28, 34, 25, 1, 49, 27, 7, 40, 1, 26, 6, 42, 13, 47, 33, 23, 51, 50, 49, 31, 28, 39, 22, 24, 46, 34, 40, 41, 38, 46, 1, 20, 27, 32, 10, 31, 45, 6, 39, 7, 33, 31, 49, 8, 39, 29, 12, 26, 49, 16, 25, 35, 19, 23, 9, 24, 49, 10, 38, 31, 27, 11, 30, 13, 45, 8, 9, 38, 16, 5, 2, 46, 17, 13, 26, 48, 30, 35, 33, 31, 40, 24, 1, 5, 40, 33, 38, 45, 36, 44, 16, 29, 32, 30, 37, 19, 26, 16, 25, 12, 6, 15, 20, 30, 25, 29, 47, 42, 37, 15, 31, 26, 18, 18, 9, 5, 24, 8, 44, 15, 31, 22, 34, 36, 7, 14, 19, 42, 12, 33, 11, 27, 4, 42, 12, 47, 11, 28, 13, 1, 3, 32, 45, 33, 23, 26, 6, 47, 46, 30, 44, 48, 14, 39, 34, 11, 6, 21, 10, 39, 47, 30, 40, 14, 9, 1, 16, 2, 12, 30, 23, 1, 41, 41, 25, 32, 28, 27, 12, 26, 8, 10, 32, 9, 22, 26, 43, 41, 5, 19, 44, 4, 9, 2, 30, 48, 32, 24, 37, 9, 16, 11, 30, 1, 7, 29, 43, 47, 22, 9, 48, 13, 35, 47, 2, 23, 38, 26, 47, 18, 3, 20, 35, 13, 48, 26, 39, 35, 38, 23, 27, 49, 14, 15, 26, 6, 43, 20, 18, 34, 27, 22, 44, 8, 9, 8, 43, 26, 11, 6, 35, 23, 24, 47, 31, 3, 35, 11, 28, 29, 13, 18, 31, 25, 5, 24, 9, 19, 1, 35, 5, 22, 7, 17, 25, 5, 2, 49, 7, 20, 13, 25, 1, 36, 31, 14, 13, 18, 9, 46, 24, 27, 34, 19, 20, 38, 44, 11, 17, 7, 38, 12, 41, 31, 9, 44, 4, 41, 43, 40, 34, 7, 45, 40,
                34, 27, 23, 39, 7, 12, 48, 46, 16, 8, 36, 34, 14, 31, 19, 19, 48, 5, 47, 2, 15, 37, 16, 31, 29, 22, 12, 28, 32, 24, 23, 5, 48, 7, 19, 13, 38, 41, 39, 34, 24, 48, 9, 49, 14, 10, 31, 13, 30, 14, 18, 2, 17, 1, 16, 34, 19, 41, 9, 31, 19, 36, 35, 32, 27, 23, 12, 4, 28, 35, 3, 30, 14, 16, 26, 30, 46, 47, 10, 6, 36, 30, 14, 33, 49, 27, 28, 29, 5, 20, 41, 6, 43, 21, 49, 13, 9, 48, 24, 27, 43, 4, 39, 45, 49, 11, 30, 32, 33, 23, 14, 33, 11, 29, 34, 40, 36, 47, 22, 12, 34, 38, 40, 8, 9, 27, 39, 20, 21, 43, 34, 15, 12, 46, 3, 31, 39, 13, 1, 29, 23, 39, 21, 27, 18, 46, 2, 7, 10, 32, 5, 3, 23, 9, 7, 22, 24, 43, 48, 38, 5, 40, 39, 1, 41, 13, 7, 25, 43, 20, 32, 36, 8, 25, 11, 46, 24, 40, 44, 35, 18, 9, 4, 11, 6, 43, 10, 39, 38, 11, 30, 36, 38, 29, 37, 19, 38, 4, 26, 23, 41, 47, 33, 17, 40, 11, 41, 43, 29, 23, 27, 32, 49, 5, 1, 29, 27, 34, 42, 41, 26, 23, 1, 45, 39, 8, 17, 34, 23, 22, 49, 18, 36, 5, 32, 48, 14, 14, 39, 40, 38, 1, 48, 17, 15, 25, 7, 40, 31, 32, 26, 3, 39, 4, 37, 23, 31, 16, 30, 45, 9, 8, 35, 10, 33, 17, 20, 37, 23, 46, 48, 28, 22, 12, 2, 16, 11, 25, 8, 24, 16, 45, 18, 8, 47, 2, 26, 48, 10, 7, 38, 9, 43, 24, 44, 49, 6, 15, 8, 42, 29, 10, 22, 19, 16, 1, 27, 38, 43, 20, 11, 22, 27, 7, 25, 7, 40, 2, 13, 9, 29, 48, 24, 46, 43, 34, 15, 16, 43, 29, 23, 22, 5, 20, 9, 14, 4, 17, 24, 35, 3, 30, 41, 37, 45, 40, 1, 8, 11, 14, 48, 44, 43, 11, 7, 20, 8, 29, 30, 34, 43, 28, 49, 28, 19, 2, 40, 22, 45, 16, 38, 36, 24, 5, 41, 36, 24, 49, 13, 27, 48, 48, 7, 34, 37, 4, 31, 4, 39, 47, 11, 45, 32, 12, 40, 21, 16, 34, 15, 11, 21, 3, 22, 14, 16, 40, 33, 24, 3, 4, 23, 36, 9, 13, 47, 25, 46, 28, 20, 4, 44, 46, 15, 42, 17, 35, 19, 36, 7, 15, 6, 35, 49, 3, 28, 32, 47, 23, 29, 6, 26, 30, 27, 12, 8, 6, 7, 48, 45, 4, 1, 25, 27, 1, 17, 27, 42, 26, 11, 31, 24, 14, 47, 40, 42, 20, 1, 5, 49, 23, 47, 4, 48, 12, 44, 13, 20, 44, 41, 1, 30, 14, 10, 13, 38, 4, 49, 33, 32, 34, 6, 48, 38, 44, 13, 40, 8, 41, 44, 10, 14, 3, 30, 45, 36, 2, 19, 32, 35, 24, 21, 18, 23, 41, 40, 45, 19, 28, 12, 8, 3, 26, 1, 39, 14, 8, 18, 1, 26, 31, 33, 13, 4, 17, 23, 2, 6, 17, 34, 31, 7, 18, 23, 18, 2, 7, 11, 20, 38, 13, 30, 27, 31, 17, 25, 20, 11, 21, 47, 16, 12, 16, 42, 39, 1, 6, 28, 34, 38, 10, 5, 22, 39, 31, 41, 17, 27, 1, 23, 17, 20, 48, 10, 24, 46, 9, 31, 42, 5, 48, 40, 37, 32, 46, 30, 47, 15, 26, 4, 15, 22, 39, 30, 45, 41, 48, 9, 35, 29, 35, 15, 3, 21, 48, 38, 18, 36, 23, 27, 37, 30, 43, 44, 47, 35, 14, 2, 5, 41, 15, 11, 4, 26, 7, 20, 37, 48, 35, 24, 19, 25, 16, 14, 6, 40, 21, 30, 31, 4, 37, 17, 25, 40, 1, 49, 46, 33, 31, 41, 37, 17, 1, 47, 49, 32, 9, 18, 20, 6, 35, 23, 27, 9, 16, 5, 43, 37, 20, 26, 13, 8, 10, 44, 6, 23, 16, 30, 37, 11, 3, 43, 2, 1, 18, 8, 6, 25, 39, 47, 3, 24, 8, 47, 44, 9, 38, 2, 47, 46, 42, 31, 14, 9, 28, 19, 43, 44, 45, 5, 39, 8, 36, 3, 3, 2, 23, 48, 29, 45, 40, 41, 42, 9, 45, 24, 10, 1, 30, 15, 39, 32, 5, 38, 15, 22, 49, 20, 30, 27, 7, 2, 15, 17, 43, 46, 48, 11, 29, 31, 4, 41, 39, 14, 34, 32, 16, 43, 39, 19, 5, 8, 40, 33, 25, 34, 36, 43, 47, 26, 9, 4, 20, 23, 34, 14, 43, 5, 44, 23, 9, 4, 42, 8, 29, 6, 30, 3, 14, 41, 27, 38, 4, 38, 8, 44, 11, 5, 21, 20, 14, 2, 37, 25, 4, 1, 7, 20, 3, 16, 40, 36, 29, 31, 38, 39, 1, 24, 39, 30, 44, 20, 23, 46, 31, 42, 47, 16, 29, 28, 31, 5, 40, 11, 38, 30, 13, 14, 33, 20, 47, 34, 8, 17, 22, 38, 12, 32, 42, 37, 5, 19, 45, 1, 2, 34, 19, 30, 24, 43, 1, 31, 46, 8, 29, 16, 41, 48, 2, 44, 49, 40, 46, 4, 3, 44, 32, 9, 39, 37, 46, 28, 8, 46, 23, 28, 14, 35, 9, 1, 39, 33, 19, 2, 47, 7, 38, 3, 13, 5, 7, 2, 21, 47, 42, 43, 45, 37, 7, 41, 9, 23, 8, 19, 2, 1, 18, 42, 6, 4, 3, 23, 39, 8, 36, 28, 14, 32, 46, 31, 37, 20, 21, 42, 11, 30, 4, 9, 38, 34, 41, 1, 28, 2, 3, 1, 23, 6, 11, 33, 16, 2, 43, 24, 32, 29, 20, 6, 25, 35, 29, 12, 22, 17, 37, 48, 33, 40, 24, 8, 38, 22, 34, 28, 6, 3, 43, 39, 14, 30, 3, 2, 25, 31, 30, 23, 39, 48, 5, 26, 5, 6, 2, 7, 8, 37, 32, 18, 42, 37, 6, 28, 3, 39, 5, 23, 43, 36, 28, 4, 48, 45, 44, 39, 34, 28, 22, 13, 14, 32, 10, 24, 43, 35, 23, 36, 3, 48, 23, 37, 40, 5, 21, 4, 33, 22, 38, 24, 20, 21, 16, 39, 23, 18]

    new_pool = [] 
    
    for i in range(6):
        num =  random.choices(num_pool, k=6)
        while num in new_pool:
            num = random.choice(num_pool)
        
    new_pool.append(num)

    print(f'Today\'s lotto Magic picks are:\n{new_pool}')

    print('Closing.....')
    
if __name__ == '__main__':
        closeInput = input('PRESS ENTER KEY TO EXIT')

else:
    time.sleep(20)

lottery_pick()
lottery_pick()