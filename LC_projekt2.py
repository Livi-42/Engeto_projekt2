# Bull & Cows - hra postavená na hádání 4 ciferného čísla
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Livia Crhova
email: livia.crhova@gmail.com
"""
import random
import datetime

def solution_generator():
    """
    creates a tuple consisting of 4 random unique numeric elements, each of them from 0 to 9, except for the first element that cannot be 0
    
    Parameters
    ----------
    (none)

    Returns
    ----------
    tuple
    
    """
    digit_list = ["0","1","2","3","4","5","6","7","8","9"]
    first_digit = str(random.randint(1,9))
    digit_list.remove(first_digit)
    other_digits = tuple(random.sample(digit_list,3))
    solution = (first_digit,) + other_digits
    return solution

def duplicate_finder(verified_tuple):
    """
    returns a tuple consisting of the elements that were duplicated in the original tuple
    
    Parameters
    ----------
    arg1 : tuple

    Returns
    ----------
    tuple
    """
    duplicates = tuple ({element for element in verified_tuple if verified_tuple.count(element) > 1})
    return duplicates

def numeric_checker(verified_tuple):
    """
    checks if there are only numeric elements in a tuple
    
    Parameters
    ----------
    arg1 : tuple

    Returns
    ----------
    boolean
    """
    str = "".join(verified_tuple)
    return str.isnumeric()

def bulls_cows_counter(verified_tuple, compared_tuple):
    """
    prints count of bulls and cows after comparing the guess-tuple with the solution-tuple
    
    Parameters
    ----------
    arg1 : tuple
    arg2 : tuple

    Returns
    ----------
    (none)
    """
    bulls = [element for element in range(0,4) if verified_tuple[element] == compared_tuple[element]]
    if len(bulls) == 1:
        xs = ""
    else: xs = "s"
    cows = [element for element in range(0,4) if verified_tuple[element] in list(compared_tuple)]
    if len(cows)-len(bulls) == 1:
        ys = ""
    else: ys = "s"
    print(f"{len(bulls)} bull{xs}, {len(cows)-len(bulls)} cow{ys}")

def game_bullscows():
    """
    the game Bulls&Cows
    
    Parameters
    ----------
    (none)

    Returns
    ----------
    (none)
    """
    print(f"Hi there!\n{"-"*50}\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n{"-"*50}\nEnter a number:\n{"-"*50}")
    success = 0
    attempt_counter = 0
    solution = solution_generator()
    start = datetime.datetime.now()
    while success == False:
        attempt = tuple(input (">>> "))
        if len(attempt) != 4:
            print("The puzzle consists of 4 digits but your guess had different length. Try again!") 
        elif duplicate_finder(attempt) != ():
            print("The puzzle consists of unique digits but there are duplicates in your guess. Try again!")
        elif attempt[0] == "0":
            print("The puzzle is a number that does not begin with 0. Try again!")
        elif numeric_checker(attempt) == False:
            print("The puzzle consists of digits only but there are other characters in your guess. Try again!")
        elif attempt != solution:
            bulls_cows_counter(attempt, solution)
            attempt_counter +=1
        elif attempt == solution:
            attempt_counter +=1
            end = datetime.datetime.now()
            if attempt_counter == 1:
                es = ""
            else: es = "es"
            print(f"Correct, you've guessed the right number\nin {attempt_counter} guess{es}!\n{"-"*50}\nThat's amazing!")
            print(f"\nTime of play: {end-start} ")
            success = True
            
            



if __name__ == "__main__":
    print("Initiating the game Bulls&Cows...\n\n")
    game_bullscows()