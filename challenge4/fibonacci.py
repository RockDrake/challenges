
ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibboStringOut(fibboNum):


    fibboNumList = []
    for i in range(len(fibboNum)):
        fibboNumList.append(fibboNum[i])

    fibboNumListLength = len(fibboNumList)-1
    fibboConcat = ""

    if fibboNumListLength >= 0:
        if fibboNumListLength > 0:
            if int(fibboNumList[fibboNumListLength-1]) == 1:
                fibboConcat = (ones[int(fibboNumList[fibboNumListLength]) + 10]) + " " + fibboConcat
        else:
            fibboConcat = (ones[int(fibboNumList[fibboNumListLength])]) + " " + fibboConcat

        if fibboNumListLength >= 1:
            if int(fibboNumList[fibboNumListLength-1]) != 1:
                if int(fibboNumList[fibboNumListLength]) != 0:
                    fibboConcat = (ones[int(fibboNumList[fibboNumListLength])]) + " " + fibboConcat
                fibboConcat = (tens[int(fibboNumList[fibboNumListLength-1])]) + " " + fibboConcat

            if fibboNumListLength >= 2:
                if fibboNumList[fibboNumListLength-2] != "":
                    if int(fibboNumList[fibboNumListLength-2]) != 0:
                        fibboConcat = (ones[int(fibboNumList[fibboNumListLength - 2])]) + " Hundred " + fibboConcat

                if fibboNumListLength >= 3:
                    if fibboNumListLength > 3:
                        if int(fibboNumList[fibboNumListLength-4]) == 1:
                            fibboConcat = (ones[int(fibboNumList[fibboNumListLength-3]) + 10]) + " Thousand " + fibboConcat
                    else:
                        fibboConcat = (ones[int(fibboNumList[fibboNumListLength-3])]) + " Thousand " + fibboConcat

                    if fibboNumListLength >= 4:
                        if int(fibboNumList[fibboNumListLength-4]) != 1:
                            if int(fibboNumList[fibboNumListLength-3]) != 0:
                                fibboConcat = (ones[int(fibboNumList[fibboNumListLength-3])]) + " Thousand " + fibboConcat
                            fibboConcat = (tens[int(fibboNumList[fibboNumListLength-4])]) + " " + fibboConcat

                        if fibboNumListLength >= 5:
                            if fibboNumList[fibboNumListLength-5] != "":
                                if int(fibboNumList[fibboNumListLength-4]) != 0:
                                    fibboConcat = (ones[int(fibboNumList[fibboNumListLength-5])]) + " Hundred " + fibboConcat

                            if fibboNumListLength >= 6:
                                if fibboNumList[fibboNumListLength] != "":
                                    fibboConcat = (ones[int(fibboNumList[fibboNumListLength-6])]) + " Million " + fibboConcat

    print(fibboConcat)

def fibboInChk(numIn):
    try:
        numIn = int(numIn)
        if numIn > 0 and numIn < 33:
            return(True)
        else:
            return(False)
    except:
        return(False)

def fibboIn():
        numIn = input("Enter a fibonacci position (1 to 32) to see it's value.  : ")
        if fibboInChk(numIn) is True:
            fibboNum = str(fibonacci(int(numIn)))
            print("\n The fibonacci number is: " + str(fibboNum) + "\n")
            print("The phonetic output is... ")
            print(fibboStringOut(fibboNum))
        else:
            print("Invalid entry try again. 1")
            fibboIn()

fibboIn()
