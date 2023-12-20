class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        found_vowels = []
       
        for char in s:
            if char in vowels:
                found_vowels.append(char)

        new_string = ""
        for char in s:
            if char in vowels:
                new_vowel = found_vowels.pop(len(found_vowels) - 1)
                new_string += new_vowel
            else:
                new_string += char

        return new_string        