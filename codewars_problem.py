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
def sum_mix (arr:int)->int:
    count = 0
    for i in arr:
        count += i
    return count
def reverse (string:str)->str:
    return string[::-1]
def ends_with (text:str,ending:str)->str:
    return ends_with(text,ending)
def capitals(word:str)->str:
    return [x for x,y in enumerate(word) if y.isupper()]
def get_grade(*grades):
    mean = sum(grades) / len(grades)
    for score, grade in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]:
        if mean >= score:
            return grade
def square_sum(numbers):
    return sum([x ** 2 for x in numbers])
def twice_as_old(dad_years_old, son_years_old):
    x = son_years_old *2
    y = dad_years_old - x
    return abs(y)
def get_char(c):
  return chr(c)
def rot13(message):
    import codecs
    return codecs.encode(message, 'rot_13')
def duplicate_encode(word):
    word = word.lower()
    new = ""

    for i in word:
        if word.count(i) > 1:
            new += ")"
        else:
            new += "("
    return new
def order(sentence):
    return " ".join(sorted(sentence.split(), key=min))
def goals(*l):
    return sum(l)
def find_it(seq):
    return sum(i for i in set(seq) if seq.count(i) % 2 == 1)
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names [0]} likes this"
    elif len (names) == 2:
        return f"{names [0]} and {names [1]} like this"
    elif len(names) == 3:
        return f"{names [0]}, {names [1]} and {names [2]} like this"
    else:
        return f"{names [0]}, {names [1]} and {len(names)-2} others like this"
#codechump competition
def camel(text):
    word =""
    for i in text:
        if i.isupper():
            word += " "
            word += i.lower()
        else:
            word += i.upper()
    return word
def ada(text):
    return text.count("ada")
def ml(team):
    dict_team = {}

    for i in team:
        dict_team[i] = dict_team.get(i, 0) + 1

    if len(dict_team.values()) < 5:
        return f"You can have 0 teams"
    else:
        return f"You can have {min(dict_team.values())}"
    -------------------------------------
def sum_two_smallest_number(numbers) :
    return sum(sorted(numbers[:2]))
def filter_list(l):
    return [x for x in l if isinstance(x, int)]
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True  if fuel_left*mpg >= distance_to_pump else False
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())
def odd_or_even(arr):
    return "even" if sum(arr) %2 == 0 else "odd"
def validate_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()