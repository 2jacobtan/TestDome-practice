https://www.testdome.com/d/python-interview-questions/9

#1
def group_by_owners(files):
    files2 = {}
    for f,o in files.items():
        files2.setdefault(o,[]).append(f)
    return files2
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))


#2
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        return [[i,t] for i in self.ingredients for t in self.toppings]

machine = IceCreamMachine(["vanilla", "chocolate"], ["red sauce", "blue sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


#3
def unique_names(names1, names2):
    set1 = set()
    set1.update(names1,names2)
    return list(set1)
    #return set(names1 + names2)

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia


#4 "first try; fastest"
def is_palindrome(word):
    stop_after = len(word) // 2; print(stop_after)
    word = word.upper(); print(word)
    for i, v in enumerate(word):
        if i > stop_after:
            break
        if word[i] != word[-1-i]:
            return False
    return True
    
print(is_palindrome('Deleveled'))

#4 "second try; slower"
def is_palindrome(word):
    stop_after = len(word) // 2
    word = word.upper()
    print(word)
    print(word[:stop_after])
    print(word[:-stop_after-1:-1])
    if word[:stop_after] == word[:-stop_after-1:-1]:
        return True
    else:
        return False
    
print(is_palindrome('Deleveled'))


#5
from math import sqrt

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    return ( (-b + sqrt(discriminant))/(2*a), (-b - sqrt(discriminant))/(2*a) )

print(find_roots(2, 10, 8));


#6
from collections import namedtuple

Node = namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    parent = root
    while(True):
        if parent.value == value:
            return True
        elif (parent.left != None and parent.value > value):
            parent = parent.left
        elif (parent.right != None and parent.value < value):
            parent = parent.right
        else:
            break
    return False
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))


#7
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        previous_songs = set()
        current = self
        while True:
            if (current.next == None):
                return False
            elif (current.next.name not in previous_songs):
                previous_songs.add(current.name)
                current = current.next
            else:
                return True
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())


#8 without binary search
from operator import itemgetter

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    length = len(numbers)
    numbers_i = list(zip(numbers,range(length)))
    numbers_i.sort(key = itemgetter(0))
    i,j,sum = 0,None,None
    while i < length -1:
        j = i+1
        while j < length:
            sum = numbers_i[i][0]+numbers_i[j][0]
            if sum == target_sum:
                return (numbers_i[i][1],numbers_i[j][1])
            j+=1
        i+=1
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

#8 (first try; with binary search; too slow)
from operator import itemgetter

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    length = len(numbers)
    numbers_i = list(zip(numbers,range(length)))
    numbers_i.sort(key = itemgetter(0)); print(numbers_i)
    i,j,sum = 0,None,None
    while i < length -1:
        btm = i+1
        top = length - 1
        while (top - btm >= 0):
            j = (top - btm)//2 + btm
            sum = numbers_i[i][0]+numbers_i[j][0]
            print(numbers_i[i][0],numbers_i[j][0],sum)
            if sum == target_sum:
                print(numbers_i[i][0],"+",numbers_i[j][0],"=",target_sum)
                return (numbers_i[i][1],numbers_i[j][1])
            elif sum > target_sum:
                top = j-1
            elif sum < target_sum:
                btm = j+1           
        i+=1
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

#8 (2nd try; fast enough, passed all tests)

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    left = {} #store newly encountered numbers
    right = {} #store difference (from target_sum) of newly encountered numbers
    for i,num in enumerate(numbers):
        j = right.get(num)
        print (j,i)
        if j:
            print (numbers[j],"+",numbers[i],"=",target_sum)
            return (j,i)
        else:
            if (left.setdefault(num,i) == i):
                right[target_sum-num] = i
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))


#9
def pipeline(*funcs):
    def helper(arg):
        input = arg
        for f in funcs:
            input = f(input)
        return input
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0


#10
from collections import Counter
from collections import OrderedDict
from operator import itemgetter

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        name, score, games_played = [],[],[]
        for p,c in self.standings.items():
            name.append(p); print(p)
            score.append(-c['score']); print(-c['score'])
            games_played.append(c['games_played']); print(c['games_played'])
            indices = list(range(len(name)))
        print("__vars_");print(name);print(score);print(games_played)
        ranked = list(zip(name,score,games_played,indices))
        ranked.sort(key=itemgetter(slice(1,None)))
        return ranked[rank-1][0]
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))


#11
class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        if new_path[0] == '/':
            new = new_path[1:].split('/')
            current = []
        else:
            new = new_path.split('/')
            current = self.current_path[1:].split('/'); print("current0",current)
        print("new",new)
        for x in new:
            if x == '..':
                current.pop()
            else:
                current.append(x)
            print("current",current)
        self.current_path = '/'+'/'.join(current)        

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)