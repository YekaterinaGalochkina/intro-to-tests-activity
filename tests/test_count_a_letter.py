from main import count_a_letter
import pytest


# Basic count of a letter in a word:

def test_basic_count_letter_in_sentence():
    letter = 'a'
    sentence = 'banana'
    score = count_a_letter(sentence, letter)
    assert score == 3

#   Sentence with spaces and punctuation:

def test_sentance_with_spaces_and_punctuation():
    letter = 'o'
    sentence = 'Hello, world!'
    score = count_a_letter(sentence, letter)
    assert score == 2

#   Empty sentence:

def test_empty_sentence():
    letter = 'a'
    sentence = ''
    score = count_a_letter(sentence, letter)
    assert score == None


# 	Letter is not in the sentence:

def test_letter_is_not_in_sentence():
    letter = 'z'
    sentence = 'hello'
    score = count_a_letter(sentence, letter)
    assert score == 0


# 	Letter is uppercase but exists in lowercase in the sentence:

def test_letter_is_uppercase():
    letter = 'A'
    sentence = 'apple'
    score = count_a_letter(sentence, letter)
    assert score == 0


# 	Letter is a special character or number (invalid input):

def test_letter_is_a_number():
    letter = '1'
    sentence = 'test123'
    score = count_a_letter(sentence, letter)
    assert score == None

# 	Sentence contains only one repeated letter:

def test_sentence_contain_only_one_repeated_letter():
    letter = 'a'
    sentence = 'aaaaa'
    score = count_a_letter(sentence, letter)
    assert score == 5

