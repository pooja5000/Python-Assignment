# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def vowel(character):
    character=character.lower()
    if character in('a','e','i','o','u'):
        return True
    
def main():

    char=input("Enter chaaracter:")
    ret=vowel(char)

    if ret==True:
        print("Vowel")
    else:
        print("Not Vowel")

if __name__=="__main__":
    main()