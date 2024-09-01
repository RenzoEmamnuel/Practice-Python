def replacement ():                                                         #replacement
    x = "hello world!"
    print(x.replace("!","?"))
def counterfeit():                                                          # counterfeit of a number
    y = 12
    print (-y)
def loop():                                                                 # loop
    for count in range(1, 10):
        for x in range(1, count+1):
            print(count, end="")
        print("")
def summation(num):
    return sum(range(num+1))
def reverse_seq(n):
    result = []
    for x in range(1,n+1):
        result.append(x)
    result.reverse()
    print(result)
def find_average(numbers):
    try:
        x = sum(numbers)/len(numbers)
        return x
    except ZeroDivisionError:
        return 0
def paperwork(n, m):
    if n>0 and m>0:
        return n*m
    else:
        return 0
def better_than_average(class_points, your_points):
    x = sum(class_points) / len(class_points)
    if your_points > x:
        return True
    else:
        return False
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
def Fibonacci():
    x = int(input("Enter the number of terms: "))
    a,b = 0,1
    print("Fibonacci Series: ", end="")
    for i in range(x):
        print(a ,end=",")
        a,b = b,a+b
def double_char(s):
    x = s.lower()
    for i in x :
        print (str(i)*2,end="")
def double_chars(s):
    word = ''
    for i in s :
        word = word+(i*2)
    return word
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
def switch_it_up(number):
    words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    return words.get(number)
def between(a,b):
    i = []
    for tae in range(a,b+1):
        i.append(tae)
    return i
def move(position, roll):
    return roll*2+position
def strCount(string, letter):
    print (string.count(letter))
def get_age(age):
    return int(age[0])
def how_much_i_love_you(nb_petals):
    words = {
        1: 'I love you',
        2: 'a little',
        3: 'a lot',
        4: 'passionately',
        5: 'madly',
        6: 'not at all'}
    return words[nb_petals%6]
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False
def enough(cap, on, wait):
    if cap > wait + on :
        return 0
    else:
        return (wait+on)-cap
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count
