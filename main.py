import re


previous = 0
run = True


print ("Kamals First Python Calculator")
print ("Type quit to exit!")

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
                previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    performMath()


