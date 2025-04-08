## AP Final Assignment
## Lalith Aditya
## 210200014

#1Q
'''def checkPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example:
print(checkPalindrome("malayalam"))     
print(checkPalindrome("civic"))'''      

#2
'''def minIndexFirstString(str1, str2):
    max_index = -1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
               max_index = max(max_index, i)
    return max_index

# Examples:
print(minIndexFirstString("tiger", "integer"))     
print(minIndexFirstString("integer", "tiger"))'''     

#3 
'''def firstLetters(s):
    result = ""
    in_word = False
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
            result += s[i]
    return result

# Examples:
print(firstLetters("bad is nice"))         
print(firstLetters("hello other world"))'''   

#4
'''class UpperCaseException(Exception):
    pass

def evenIndexCapital(s):
    for c in s:
        if 'A' <= c <= 'Z':
            raise UpperCaseException("Input must contain only lowercase letters.")
    
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += chr(ord(s[i]) - 32)  # Convert to uppercase
        else:
            result += s[i]
    return result

# Example:
print(evenIndexCapital("school"))''' 

#5
'''def shift(s, ccount=0, acount=0):
    if not isinstance(ccount, int) or not isinstance(acount, int):
        raise ValueError("ccount and acount must be integers.")
    if ccount < 0 or acount < 0:
        raise ValueError("ccount and acount must be non-negative.")

    n = len(s)
    acount %= n
    ccount %= n

    rotated = s[acount:] + s[:acount]
    result = rotated[-ccount:] + rotated[:-ccount]
    return result

print(shift("NinjaHattori"))                    
print(shift("NinjaHattori", acount=3))          
print(shift("NinjaHattori", ccount=3))          
print(shift("NinjaHattori", ccount=3, acount=3))
print(shift("NinjaHattori", ccount=3, acount=6))
print(shift("NinjaHattori", ccount=6, acount=3))'''

#6
'''def distChar(s1, s2):
    result = []
    for c in s1:
        if c not in s2 and c not in result:
            result.append(c)
    for c in s2:
        if c not in s1 and c not in result:
            result.append(c)
    result.sort()
    return ''.join(result)

# Examples:
print(distChar("characters", "alphabets"))  
print(distChar("apples", "oranges")) 
print(distChar("apples", "apples"))'''       

#7

'''class InvalidInputException(Exception):
    pass

def change(s):
    if not all(c in ('R', 'G') for c in s):
        raise InvalidInputException("String must contain only 'R' or 'G'")

    count_R = sum(1 for c in s if c == 'R')
    count_G = len(s) - count_R
    return min(count_R, count_G)

# Examples:
print(change("R"))           
print(change("RGRGR"))       
print(change("GRG"))'''        

#8

'''def delVowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for c in s:
        is_vowel = False
        for v in vowels:
            if c == v:
                is_vowel = True
                break
        if not is_vowel:
            result += c
    return result

# Examples:
print(delVowels("SfgEtfjofubjiekp"))   
print(delVowels("aEiOu"))'''              

#9

'''def moveDups(s):
     seen = set()
     unique = []
     dups = []
     for c in s:
         if c not in seen:
             seen.add(c)
             unique.append(c)
         else:
             dups.append(c)
     return ''.join(unique) + ('_' + ''.join(dups) if dups else '')

print(moveDups("cartoon"))
print(moveDups("network"))
print(moveDups("aabbcc"))
print(moveDups("cccbbaaa"))'''

#10

'''def separate(s):
    groups = {}
    for c in s:
        if c not in groups:
            groups[c] = c
        else:
            groups[c] += c
    return list(groups.values())

# Examples:
print(separate("cartoon"))     
print(separate("network"))     
print(separate("aabbcc"))      
print(separate("cccbaaa"))'''     

#11

'''def minOp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j  # insert all
            elif j == 0:
                dp[i][j] = i  # remove all
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )
    return dp[m][n]
print(minOp("python", "pythons"))   
print(minOp("abc", ""))             
print(minOp("abc", "def"))          
print(minOp("ab", "def"))''' 

#12

'''class InvalidRollException(Exception):
    pass

def fee(base_fee, roll):
    if len(roll) != 7 or not roll[2:4].isdigit() or not roll[4:].isdigit():
        raise InvalidRollException("Invalid roll format")
    
    dept = roll[:2]
    year = int(roll[2:4])
    program = roll[4]
    
    if dept not in ['CS','DS','EE','ME'] or program not in ['1','2']:
        raise InvalidRollException("Invalid department or program")
    
    duration = 4 if program == '1' else 2
    years_paid = min(2022 - (2000 + year) + 1, duration)
    
    total = 0
    current = base_fee
    for _ in range(years_paid):
        total += current
        current = int(current * 1.1)
    
    return total

# Examples
print(fee(100000, "CS20143"))  
print(fee(100000, "DS18243")) 
try:
    print(fee(100000, "EEL6243"))  
except InvalidRollException as e:
    print(e)'''

#13
'''def checkunique(count):
    keys_to_remove = []
    for key in count.keys():
        if count[key] == 0:
            keys_to_remove.append(key)
    for i in keys_to_remove:
        del count[i]
    temp = set(count.values())
    if len(temp) == 1:
        return True
    else:
        return False


def create_count(str1):
    temp = {}
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    return temp


def max_num(count):
    large = 0
    final = ''
    for i in count.keys():
        if count[i] >= large:
            large = count[i]
            final = i
    return final


def make_string(count):
    temp = ''
    for i, j in count.items():
        temp += i*j
    return temp


def remove_whole(count, k):
    keys_to_remove = []
    for i in count.keys():
        if k == count[i]:
            keys_to_remove.append(i)
    for key in keys_to_remove:
        temp = count
        del temp[key]
        if checkunique(temp):
            return temp
    return count

def reduce(low_str, k):
    if checkunique(create_count(low_str)):
        print(create_count(low_str))
        return low_str

    main_count = create_count(low_str)

    total_remove = remove_whole(main_count,k)
    print(total_remove)
    if checkunique(total_remove):
        return make_string(total_remove)
    

    temp = main_count
    for i in range(k):
        letter = max_num(temp)
        temp[letter] -= 1
    print(temp)
    if checkunique(temp):
        return make_string(temp)
    else:
        return 'none'
print("1")
print(reduce('aabbcc',0)) #check

print("2")
print(reduce('aabbbcc',0)) #check

print("3")
print(reduce('aabbbcc',1)) #check

print("4")
print(reduce('aabbbcc',2)) #check

print("5")
print(reduce('aabbbcc',3)) #check

print("6")
print(reduce('aabbbcc',4)) #check

print("7")
print(reduce('aabbbcc',5)) #check

print("8")
print(reduce('aabbbcc',6)) #check

print("1")
print(reduce('aabbbcc',7)) #check

print("1")
print(reduce('aaaabbcc',4)) #check'''

#14
'''def equivalent(str1, str2):
    def is_rotation(s1, s2):
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)

    longest_substring = ""
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            sub1 = str1[i:j + 1]
            for k in range(len(str2)):
                for l in range(k, len(str2)):
                    sub2 = str2[k:l + 1]
                    if is_rotation(sub1, sub2):
                        if len(sub1) > len(longest_substring):
                            longest_substring = sub1
                        elif len(sub1) == len(longest_substring) and sub1 < longest_substring:
                            longest_substring = sub1

    return longest_substring

print(equivalent('hdjkou1', 'pokoudj'))  
print(equivalent('ghajior', 'abkoidj'))  
print(equivalent('hdjkou1', 'pikpiaa'))''' 

#15
'''def subPali(s):
    n = len(s)
    if n == 0: return 0
    max_len = 1
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] == s[i:j][::-1]:
                max_len = max(max_len, j - i)
    return max_len

# Examples
print(subPali("bbbabcbabdfb"))  
print(subPali("abcdefg"))'''   

#16Q

'''from collections import Counter

def extractDup(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

# Examples
print(extractDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))  
print(extractDup([-1, 1, -1, 8]))  
print(extractDup([-3, 1, -1, 8]))'''  

#17Q

'''def process_list(lst):
    print("a:", lst[3] if len(lst) > 3 else "List too short")
    print("b:", lst[2:])
    print("c:", lst[::-1])
    print("d:", sum(lst))
    print("e: max =", max(lst), ", min =", min(lst))
    print("f:", lst.index(0) if 0 in lst else -1)
    print("g: ascending =", sorted(lst), ", descending =", sorted(lst, reverse=True))

process_list([5, 3, 7, 0, 2])'''

#18Q

'''def delDup(l):
    return list(dict.fromkeys(l))

# Examples
print(delDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))  
print(delDup([-1, 1, -1, 8]))'''  

#19Q

'''class LengthMismatchException(Exception):
    pass

def weave(a, b):
    if len(a) != len(b):
        raise LengthMismatchException("Lists have unequal lengths")
    return [val for pair in zip(a, b) for val in pair]

# Examples
print(weave([], []))  
print(weave([1, 2, 3], [4, 5, 6]))'''  

#20
'''def collatz(n):
    seq = []
    while n != 1:
        if n % 2 == 1:
            seq.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    seq.append(1)
    return seq
print(collatz(1))  
print(collatz(3))  
print(collatz(5))  
print(collatz(7))'''  

#21

'''def moveZeros(lst):
    return [x for x in lst if x != 0] + [0] * lst.count(0)

# Example
print(moveZeros([1, 2, 0, 4, 0, 5, 0]))'''  

#22
'''class DimensionMismatchException(Exception):
    pass

def printMat(lst):
    import math
    n = int(math.sqrt(len(lst)))
    if n * n != len(lst):
        raise DimensionMismatchException("Matrix is not square")
    for i in range(0, len(lst), n):
        print(" ".join(map(str, lst[i:i+n])))

# Example
printMat([1, 2, 0, 4, 0, 5, 0, 7, 9])'''

#23

'''def matMul(mat1, mat2):
    n = int(len(mat1)**0.5)
    if n*n != len(mat1) or n*n != len(mat2):
        raise DimensionMismatchException("Matrices must be square and same size")
    
    result = []
    for i in range(n):
        for j in range(n):
            val = sum(mat1[i*n + k] * mat2[k*n + j] for k in range(n))
            result.append(val)
    return result

# Example
print(matMul([1,2,3,4], [5,6,7,8])) '''

#24

'''def splitsum(l):
    return [sum(x*x for x in l if x > 0), sum(x**3 for x in l if x < 0)]

# Example
print(splitsum([1, -2, 3, -1]))''' 

#25

'''def kMax(l, k):
    if k < 1 or k > len(l):
        raise ValueError("Invalid value of k")
    return sorted(l, reverse=True)[k-1]

# Examples
print(kMax([10, 2, 4, 5, 7, 9], 1))  
print(kMax([10, 2, 4, 5, 7, 9], 2))  
print(kMax([10, 2, 4, 5, 7, 9], 3))''' 

#26

'''class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

    def __repr__(self):
        return f"{self.subject}: {self.marks}"

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # List of Score objects

    def __repr__(self):
        return f"Student({self.name})"

    def average(self):
        if not self.scores:
            return 0
        return sum(score.marks for score in self.scores) / len(self.scores)

def classAverage(students, subject):
    subject_scores = [score.marks for student in students for score in student.scores if score.subject == subject]
    return round(sum(subject_scores) / len(subject_scores), 2) if subject_scores else 0

# Example usage:
s1 = Student("Alice", [Score("Math", 90), Score("Science", 85)])
s2 = Student("Bob", [Score("Math", 80)])
s3 = Student("Cara", [Score("Science", 95)])

students = [s1, s2, s3]

print(s1)                      
print(s1.average())            
print(classAverage(students, "Math"))     
print(classAverage(students, "Science"))''' 

#27

'''class Vector:
    def __init__(self, components):
        if not all(isinstance(x, (int, float)) for x in components):
            raise ValueError("All components must be numbers.")
        self.__components = components

    def __str__(self):
        return f"{len(self.__components)}-dimensional vector: {self.__components}"

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only scale by a real number.")
        return Vector([scalar * x for x in self.__components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __add__(self, other):
        if not isinstance(other, Vector) or len(other.__components) != len(self.__components):
            raise ValueError("Addition requires vectors of same dimension.")
        return Vector([x + y for x, y in zip(self.__components, other.__components)])

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(other.__components) != len(self.__components):
            raise ValueError("Subtraction requires vectors of same dimension.")
        return Vector([x - y for x, y in zip(self.__components, other.__components)])

    def __matmul__(self, other):  # for dot product
        if not isinstance(other, Vector) or len(other.__components) != len(self.__components):
            raise ValueError("Dot product requires vectors of same dimension.")
        return sum(x * y for x, y in zip(self.__components, other.__components))

v = Vector([1, 2, 3])
print(v)  
# 3-dimensional vector: [1, 2, 3]

v = 2 * v
print(v)  
# 3-dimensional vector: [2, 4, 6]

v = v * 3
print(v)  
# 3-dimensional vector: [6, 12, 18]

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)  
# 3-dimensional vector: [5, 7, 9]

print(v1 - v2)  
# 3-dimensional vector: [-3, -3, -3]

print(v1 @ v2)  
# 32'''







