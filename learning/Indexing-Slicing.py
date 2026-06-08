
# Python Indexing & Slicing – Practice File

s = "Python"

print("\n=== Basic Indexing ===")
print(s[0])     # P
print(s[1])     # y
print(s[-1])    # n
print(s[-2])    # o

print("\n=== Positive vs Negative Indexing ===")
word = "Computer"
print(word[0], word[1], word[2])
print(word[-1], word[-2], word[-3])

print("\n=== Looping Through a String ===")
for i in range(len(s)):
    print(i, s[i])

print("\n=== Basic Slicing ===")
s = "PythonProgramming"
print(s[0:6])
print(s[6:])
print(s[:6])
print(s[:])

print("\n=== Negative Slicing ===")
s = "Programming"
print(s[-4:])
print(s[:-4])
print(s[2:-2])

print("\n=== Step Slicing ===")
s = "ABCDEFGHIJ"
print(s[::2])
print(s[1::2])
print(s[::3])

print("\n=== Reverse Strings ===")
s = "Python"
print(s[::-1])
print(s[::-2])

print("\n=== Negative Step ===")
s = "ABCDEFG"
print(s[5:1:-1])
print(s[3::-1])
print(s[:3:-1])

print("\n=== Common Patterns ===")
s = "DataScience"
print("First:", s[0])
print("Last:", s[-1])
print("First 4:", s[:4])
print("Last 4:", s[-4:])
print("Reverse:", s[::-1])

print("\n=== Palindrome Check ===")
for word in ["madam", "python"]:
    print(word, "->", word == word[::-1])

print("\n=== Reverse Each Word ===")
sentence = "I love Python"
print(" ".join(word[::-1] for word in sentence.split()))

print("\n=== Reverse Word Order ===")
sentence = "I love Python programming"
print(" ".join(sentence.split()[::-1]))

print("\n=== String Immutability ===")
s = "Python"
print("J" + s[1:])

print("\n=== Lists ===")
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::-1])

numbers[0] = 100
print(numbers)

print("\n=== Tuples ===")
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])
print(t[1:4])

print("\n=== Out of Range ===")
s = "Python"
print(s[0:100])
print(s[100:200])

print("\n=== Practical Examples ===")

email = "student@gmail.com"
print(email[email.index('@') + 1:])

mobile = "9876543210"
print(mobile[:2] + "******" + mobile[-2:])

filename = "resume.pdf"
print(filename[filename.index('.') + 1:])

print("\n=== Mini Exercises ===")
print("DataAnalytics"[:4])
print("DataAnalytics"[4:])
print("DataAnalytics"[::-1])
print("DataAnalytics"[::2])

print("\n=== Rules ===")
print("""
1. Indexing starts at 0.
2. Negative indexing starts at -1.
3. End index in slicing is excluded.
4. s[:] creates a copy.
5. s[::-1] reverses a sequence.
6. Positive step -> left to right.
7. Negative step -> right to left.
8. Out-of-range indexing raises IndexError.
9. Out-of-range slicing is safe.
10. Strings/tuples are immutable, lists are mutable.
""")
