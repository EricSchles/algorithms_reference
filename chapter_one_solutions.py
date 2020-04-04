# Question 1:
#Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures?

def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)

def no_data_structures_is_unique(string: str) -> bool:
    characters = []
    for character in string:
        if character in characters:
            return False
        characters.append(character)
    return True

# Question 2:
# Given two strings, write a method to decide if one is a permutation of the other

def is_permutation(string_one: str, string_two: str) -> bool:
    return len(set(string_one)) == len(set(string_two))

# Question 3:
#Write a method to replace all spaces in a string with %20.  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def urlify(string: str) -> str:
    return "%20".join(string.split())

# Question 4:
# Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome is a word or phrase that is the same forwards and backwards.  A permutation is a rearrangement of letters.  The palindrome does not need to limited to just dictionary words.

def is_palindrome_permutation(string: str) -> bool:
    # we simply want every unique letter doubled, except possibly one
    if len(set(string)) == 1:
        return True
    palindrome_summation_one = len(set(string)) * 2
    palindrome_summation_two = palindrome_summation_one - 1
    summation = 0
    for character in set(string):
        summation += string.count(character)
    condition_one = summation == palindrome_summation_one
    condition_two = summation == palindrome_summation_two
    return condition_one or condition_two
        
# Question 5
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.  Given two strings, write a function to check if they are one edit, or zero edits away.

def is_edit_distance_one(string_one: str, string_two: str) -> bool:
    return abs(len(string_one) - len(string_two)) <= 1

# Question 6
# Implement a method to perform basic string compression using the counts of repeated characters.  For example, the string aabcccccaaa woudl become a2b1c5a3.  If the compressed string would not become smaller than the oringal string, your method should return the original string.  You can assume the string has onlyuppercase and lowercase letters.

def compression(string: str) -> str:
    if len(set(string)) == len(string):
        return string
    else:
        new_string = ''
        index = 0
        for character in string:
            char_count = 0
            for char in string[index:]:
                if char == character:
                    char_count += 1
                else:
                    break
            new_string += character + str(char_count)
            index += char_count
        return new_string

# Question 7
#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes write a method to rotate the image by 90 degrees.  Can you do this in place?

