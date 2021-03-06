'''
    This program simply takes some input range or sequence of numbers (List)
    and randomly selects from them 'n' number of times for some resulting sequence
'''

import Exceptions
import random
import sys, getopt

powerNumbers = list(range(1,11))

DEFAULT_MAX_GenNumber = 40
DEFAULT_MIN_Size = 4
DEFAULT_MAX_Size = 10
DEFAULT_MIN_Lines = 1
DEFAULT_MAX_Lines = 24

def randomizer_seq (sequence,power=powerNumbers[::], forceRandPower=False, outputLines=1, outputLineSize=5) :

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


            if forceRandPower :
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
    sequence = list(range(1, max+1))
    return sequence

def validate_size(arg,max=DEFAULT_MAX_Size):
    num = 0
    if arg.isdigit() and (int(arg) >= 0):
        num = int(arg)
    else :
        raise Exceptions.SizeNumberValueError

    if num < 1 :
        raise Exceptions.SizeNumberTooSmall
    elif num > max :
        raise Exceptions.SizeNumberTooBig

    return num

def validate_LineNum(arg,min=DEFAULT_MIN_Lines,max=DEFAULT_MAX_Lines):
    numLines = 0
    if arg.isdigit() and (int(arg) >= 0):
        numLines = int(arg)
    else :
        raise Exceptions.LineNumberValueError

    if numLines < min:
        raise Exceptions.LineNumberTooSmall
    elif numLines > max :
        raise Exceptions.LineNumberTooBig

    return numLines

def main(argv):
    powers = list(range(1, 11))
    numberSeqSize = 40
    randPower = False
    numLines = 4
    lineLength = 6

    if sys.version_info.major < 3 :
        print("User running Script with Python v{}.{}".format(sys.version_info.major,sys.version_info.minor))
        print("Please run Script with Python v3 or higher")
        exit(1)

    ## Check run arguments
    if len(sys.argv) is 1 :
        print("No user parameters entered!","Using Defaults:","\n","Lines = 4, Size = 6, Random Powers = False")
        print("Use -h to print help for runtime args:")
        print('Number_Randomizer.py [parameters] -l OR --lines (Set number of lines. MIN = 1) -s OR --size (Set Numbers per line. MIN = 5) -r OR --randpower (Force random power per line)')

        randomizer_seq(generate_sequence(numberSeqSize), powers, randPower, numLines, lineLength)
    else :
        """
        Runtime args:
        -l = number of lines
        -s = how many numbers per line
        -r = true/false set random power numbers (False = same power number per line)
        """
        try:
            opts, args = getopt.getopt(argv, "l:s:rh", ["lines=", "size=", "randpower", "help"])
        except getopt.GetoptError:
            print('Number_Randomizer.py -l <number of lines> -s <numbers per line> -r (Force random power per line)')
            sys.exit(2)
        try:
            for opt, arg in opts:
                if opt == '-h':
                    print('Number_Randomizer.py -l OR --lines (Set number of lines. MIN = 1) -s OR --size (Set Numbers per line. MIN = 5) -r OR --randpower (Force random power per line)')
                    sys.exit()
                if opt in ("-l", "--lines"):
                    numLines = validate_LineNum(arg)
                    print("numbLines {}".format(numLines))
                if opt in ("-s", "--size"):
                    lineLength = validate_size(arg)
                    print("lineLength {}".format(lineLength))
                if opt in ("-r", "--randpower"):
                    randPower = True
                    print("randPower {}".format(randPower))
                #check = "ARGS: numLines {} lineLength {} randPower {}".format(numLines,lineLength,randPower)
                #Sprint(check)
            ### Specifying power numbers using range()

            print(" Lines = {} Size = {} Random Powers = {}".format(numLines,lineLength,randPower))
            randomizer_seq(generate_sequence(41),powers,randPower, numLines, lineLength)
            #randomizer_seq(generate_sequence(15),generate_sequence(21),False, 10, 6)
        except Exceptions.LineNumberTooBig:
            print("Line Number Value is above the max bound",DEFAULT_MAX_Lines)
        except Exceptions.LineNumberTooSmall:
            print("Line Number Value is below the min bound",DEFAULT_MIN_Lines)
        except Exceptions.LineNumberValueError:
            print("Line Number Value is not Vaild","Must be >= 0")
        except Exceptions.SizeNumberTooSmall:
            print("Size Number Value is below the min bound",DEFAULT_MIN_Size)
        except Exceptions.SizeNumberTooBig:
            print("Size Number Value is above the max bound",DEFAULT_MAX_Size)
        except Exceptions.SizeNumberValueError:
            print("Size Number Value is not Vaild", "Must be >= 0")

numLines = 1
lineLength = 5
randPower = False

if __name__ == "__main__":
    main(sys.argv[1:])