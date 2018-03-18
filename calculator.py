calc = [3, '+', '(', '(', 4, '+', 6, ')', '*', 9, '/', '(', 2, '-', 16, '+', 8, '*', '(', 3, '^', 2, '+', 7, ')', ')',
         ')', '/', 3, '*', 6, '*', 4, '-', 7]


def solve(calculation):
    precedence = {"^": 5, "÷": 4, "/": 4, "×": 3, "*": 3, "+": 2, "-": 2}
    bodmasIndex = []
    calcArray = calculation
    highestOperatorIndex = 0
    calc = ""

    for i in range(len(calcArray)):
        calc += str(calcArray[i])
        if calcArray[i] in precedence:
            if len(bodmasIndex) == 0:  # starts off the bodmasIndex list with a value (this is only executed once)
                bodmasIndex.append(i)
            else:
                highestOperatorIndex = i
                for x in range(len(bodmasIndex)):  # for each of the values stored in bodmasIndex
                    if precedence[calcArray[i]] > precedence[calcArray[bodmasIndex[x]]]:
                        bodmasIndex.insert(x, i)  # insert the index value
                        break
                    elif precedence[calcArray[i]] == precedence[calcArray[bodmasIndex[x]]]:
                        bodmasIndex.insert(x + 1, i)
                        break
                    else:
                        bodmasIndex.append(i)
                        break

    for i in range(len(bodmasIndex)):

        if calcArray[bodmasIndex[0]] == '^':
            currentCalculation = float(calcArray[bodmasIndex[0] - 1]) ** float(calcArray[bodmasIndex[0] + 1])
        elif calcArray[bodmasIndex[0]] == '/':
            currentCalculation = float(calcArray[bodmasIndex[0] - 1]) / float(calcArray[bodmasIndex[0] + 1])
        elif calcArray[bodmasIndex[0]] == '*':
            currentCalculation = float(calcArray[bodmasIndex[0] - 1]) * float(calcArray[bodmasIndex[0] + 1])
        elif calcArray[bodmasIndex[0]] == '+':
            currentCalculation = float(calcArray[bodmasIndex[0] - 1]) + float(calcArray[bodmasIndex[0] + 1])
        else:
            currentCalculation = float(calcArray[bodmasIndex[0] - 1]) - float(calcArray[bodmasIndex[0] + 1])

        calcArray[bodmasIndex[0] - 1] = currentCalculation
        calcArray.pop(bodmasIndex[0] + 1)
        calcArray.pop(bodmasIndex[0])

        if len(calcArray) != 1:
            bodmasIndex.remove(highestOperatorIndex)
        highestOperatorIndex -= 2

    return calcArray[0]


def bracketSolver(calculation):
    startBracketIndex = []
    endBracketIndex = []
    bracketPairs = {}

    for i in range(len(calculation)):
        if calculation[i] == '(':
            startBracketIndex.append(i)
        elif calculation[i] == ')':
            endBracketIndex.append(i)

    for i in range(len(startBracketIndex) - 1, -1, -1):
        for x in range(len(endBracketIndex)):
            if endBracketIndex[x] < startBracketIndex[i]:
                continue
            elif endBracketIndex[x] in bracketPairs.values():
                continue
            else:
                bracketPairs[startBracketIndex[i]] = endBracketIndex[x]
                break
    if len(bracketPairs) != 0:
        return bracketPairs


def calculator(calculation):
    brackets = bracketSolver(calculation)
    ans = []

    if brackets is None:
        return solve(calculation)
    else:
        s = list(brackets.keys())[0]
        e = brackets[s]
        ans.append(solve(calculation[s + 1:e]))
        calculation = calculation[:s] + ans + calculation[e + 1:]
        print(calculation)
        return calculator(calculation)

ans = calculator(calc)
print(ans)
