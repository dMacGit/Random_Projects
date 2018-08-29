'''
    This program simply takes some input range or sequence of numbers (List)
    and randomly selects from them 'n' number of times for some resulting sequence
'''

import random

powerNumbers = list(range(1,11))

def randomizer_seq (sequence,power=powerNumbers[::], samePower=False, outputLines=1, outputLineSize=5) :

    format_string = ""
    count = 0
    for item in power:
        if count == len(power)-1:
            format_string+=str(item)
        else:
            format_string+=str(item)+","
        count+=1
    print(format_string)


    numberOfLines = outputLines
    sizeOfLines = outputLineSize
    seq_copy = sequence[::]
    ordered_Line_Numbers = []

    if power is not None :
        powerNumber = randomPower = int(random.randint(1, len(power)))
    else :
        power = powerNumbers[::]
        powerNumber = randomPower = int(random.randint(1, len(power)))

    print(seq_copy)
    if isinstance(sequence,list) and sequence is not None :
        #The function can continue
        for currentLine in range(numberOfLines) :
            seq_copy = sequence[::]
            print('=== line',currentLine+1,'===')
            thisLine = ''
            for number in range(1,sizeOfLines+1):
                next_random = int(random.randint(0,(len(seq_copy)-1)-number))
                ordered_Line_Numbers.append(seq_copy.pop(next_random))
            list.sort(ordered_Line_Numbers)


            if not samePower :
                randomPower = int(random.randint(1, len(power)))
                print(ordered_Line_Numbers, randomPower)
            else :
                print(ordered_Line_Numbers, powerNumber)
            ordered_Line_Numbers.clear()

def generate_sequence( max ) :
    """
    This function simply returns a sequence of non-random numbers
    from 1 to the max number assigned in function call.
    :param max: The max number in sequence
    :return: The resulting sequence as a list
    """
    sequence = list(range(1, 41))
    return sequence


### Specifying power numbers using range()
powers = list(range(1,11))

randomizer_seq(generate_sequence(41),powers,False, 4, 6)
randomizer_seq(generate_sequence(15),generate_sequence(21),False, 10, 6)