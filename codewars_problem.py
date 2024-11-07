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
#--------
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
def find_short(s):
    return min(len(x) for x in s.split())
def printer_error(s):
    acceptable = "abcdefghijklm"
    count = 0
    for i in s:
        if i not in acceptable:
            count += 1
    return f"{count}/{len(s)}"
def is_uppercase(inp):
    return inp == inp.upper()
def maps(a):
    return [i+i for i in a]
def solution(nums):
    return [] if nums == None else sorted(nums)
#good
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0)) ##
#-----
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.upper()) == sorted(original.upper()) 
    # another way 
    def lib_checkr(word1,word2):
    word = {}
    for i in word1.lower():
        word[i]=word.get(i,0)+1
    wordd = {}
    for b in word2.lower():
        wordd[b]=wordd.get(b,0)+1
    return word == wordd
# not done 
def reverse_words(text):
    return "".join([i [::-1] for i in text.split(" ")])
def min_max(lst):
  return [min(lst), max(lst)]
def sort_array(source_array):
    new = sorted([i for i in source_array if i % 2 != 0])  
    for index,i in enumerate(source_array):
        if i % 2 == 0:
            new.insert(index,i)
    return new
def position(alphabet):
    return f"Position of alphabet: {ord(alphabet)-96}"
def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a 
    #def array_diff(a, b):
    #return [x for x in a if x not in b]
def queue_time(customers, n): # HARRRRD AS FUCK 
    cashier_no = [0]*n 
    for i in customers:
        cashier_no [cashier_no.index(min(cashier_no))] += i
    return max(cashier_no)
def solution(s): # HARD TO
    word = ""
    for i in s:
        if i.isupper():
            word += " "
            word += i
        else:
             word += i
    return word 
def two_sort(array):
    return "***".join(i for i in min(array))
    
def is_triangle(a, b, c):
    a,b,c =  sorted ([a,b,c])
    return a+b>c
from statistics import mode
def find_uniq(arr):
    x = mode(arr)
    for i in arr:
        if i != x :
            return i
    #EASIER 
    def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
def tribonacci(signature, n): #HARDDDDDD
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
def pipe_fix(nums):
    return [i for i in range(min(nums),max(nums)+1)]
    # or list(range(nums[0], nums[-1] + 1))
def row_sum_odd_numbers(n):
    return n**3
def expanded_form(num):
    x = ""
    for i,digit  in enumerate (str(num)) :
        if digit == "0" :
            continue
        else:
            x += digit + ("0" * (len(str(num)) - i - 1))
            x += " "
            x += "+"
            x += " "
    return x.strip("+ ")
def xo(s):
    return   s.lower().count("x") == s.lower().count("o")
def friend(x):
    return [i for i in x if len(i) == 4 ]
def reverse_letter(st):
    return "".join([i for i in st[::-1] if i.isalpha()])
def take(arr,n):
    return arr[:n]
def reverse(st):
    return " ".join(st.split()[::-1])
def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
def bin_to_decimal(inp):
    return int(inp,2)
def no_boring_zeros(n):
    return int(str(n).strip('0') or 0)
def multiplication_table(size): # HAAAAAAAAAAAAAAAAAAAAARD
    columns = []
    for i in range(1,size+1):
        rows = []
        for j in range(1,size+1):
            rows.append(i*j)
        columns.append(rows)
        
    return columns
def print_hello():
    return "hello world!!!!! nakalimutan ko maglagay"
def dna_to_rna(dna):
    return dna.replace("T","U")
def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"
def fuck_you_Kristine ():#cheat day # another cheat day fuck it 
    retrun "Im so tired"
    #another cheat day # more cheat day # another #more # more
    #exam week jusko # new
