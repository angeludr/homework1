import numpy as np
import pandas as pd

def number_of_steps_to_one(number):
    """Function which determines how many steps
    it takes for a number to reach 1 in the Collatz
    sequence
    input: number (a positive integer)
    output: steps
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    if not number > 1:
        raise ValueError("number must be larger than one")
    
    seq = []
    
    while number > 1:
        if (number % 2) == 0:
            number = number / 2
            seq.append(number)
        else:
            number = (number * 3) + 1
            seq.append(number)
    
    steps = len(seq)
    
    return steps

if __name__ == "__main__":
    max_number_to_check = 10**5
    numbers_to_check = np.linspace(2, 100000, 99999, dtype = int)
    print(numbers_to_check)
    
    stepL = []
    
    for i in numbers_to_check:
        i = int(i)
        steps = number_of_steps_to_one(i)
        stepL.append(steps)
    
    data = zip(numbers_to_check, stepL)
    header = ['Number', 'Steps']
    df = pd.DataFrame(data = data, columns = header)
    df.to_csv('Collatz.txt', index=False)
