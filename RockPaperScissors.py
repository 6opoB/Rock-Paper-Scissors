import random
print('Hi! Lets play Rock-Scissors-Paper?:')
answer = str(input())
knb = ['r', 's', 'p']
while answer != 'yes' and answer != 'no':
    print('Do not be shy! Just print yes/no!:')
    answer = str(input())
else:
    if answer == 'no':
        print(':( Ok, see you then')
    elif answer == 'yes':
        x = knb[random.randint(0, 2)]
        print('Lets start then! Input Rock(r)/Scissors(s)/Paper(p):')
        otvet = str(input())
        if x == 'r' and otvet == 'r':
            print('Rock - Rock! Draw!')
        elif x == 'r' and otvet == 's':
            print('Rock - Scissors! At this rate, the machines will soon take over this world!')
        elif x == 'r' and otvet == 'p':
            print('Rock - Paper! Lucky this time!')
        elif x == 's' and otvet == 'r':
            print('Scissors - Rock! ПLucky this time!')
        elif x == 's' and otvet == 's':
            print('Scissors - Scissors! Draw!')
        elif x == 's' and otvet == 'p':
            print('Scissors - Paper! At this rate, the machines will soon take over this world!')
        elif x == 'p' and otvet == 'r':
            print('Paper - Rock! Lucky this time!')
        elif x == 'p' and otvet == 's':
            print('Paper - Scissors! At this rate, the machines will soon take over this world!')
        elif x == 'p' and otvet == 'p':
            print('Paper - Paper! Draw!')
