from random import randint
nums = []
def sorteia():
    for a in range(1, 6):
        num = randint(0, 9)
        nums.append(num)
    nums.sort()
    print(f'Os números gerados foram {nums}.')


def somaPar():
    pares = []
    for a in range(1, len(nums)):
        if nums[a] % 2 == 0:
            pares.append(nums[a])
    pares.sort()
    print(f'Os números pares registrados são {pares}.')


sorteia()
somaPar()
