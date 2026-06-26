def analyze_string(s):
    print("\n**** String Analysis ****")
    print("Length of string:", len(s))
    print("Reversed string:", s[::-1])
    # Count vowels
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)
    print("\nCharacter\tPositive Index\tNegative Index")
    for i in range(len(s)):
        print(f"{s[i]}\t\t{i}\t\t{i - len(s)}")
text = input("Enter a string: ")
if text == "":
    print("Error: Empty string is not allowed.")
else:
    analyze_string(text)