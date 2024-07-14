def arithmetic_arranger(problems, show_answers=False):
#Checking the limit of only 5 problems max
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_operands = []
    second_operands = []
    lines = []
    answers = []
    for problem in problems:
        #Checking the correct operator and storing it if it is correct (only + and - are accepted)
        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."
        
        #Checking if the operands only contain digits
        removing = ['' if char == " " or char == "+" or char == "-" else char for char in problem]
        just_digits = ''.join(removing)
        if not just_digits.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        #Checking if each operand cointains up to 4 digits max
        operands = problem.split(operator)
        first_operand = operands[0].strip(' ')
        second_operand = operands[-1].strip(' ')
        if (len(first_operand) > 4) or (len(second_operand) > 4):
            return 'Error: Numbers cannot be more than four digits.'
        
        #To solve the arithmetic problem
        if '+' in problem:
            int_answer = int(first_operand) + int(second_operand)
        else:
            int_answer = int(first_operand) - int(second_operand)

        answer = str(int_answer)

        #Formatting the problem

        #To reduce code length let a and b be:
        a = len(first_operand)
        b = len(second_operand)

        #Adding spaces
        if a <= b:
            new_second_operand = operator + ' ' + second_operand
            if a == b:
                new_first_operand = '  ' + first_operand
            elif a+1 == b:
                new_first_operand = '   ' + first_operand
            elif a+2 == b:
                new_first_operand = '    ' + first_operand
            elif a+3 == b:
                new_first_operand = '     ' + first_operand
        elif a == b+1:
            new_first_operand = '  ' + first_operand
            new_second_operand = operator + '  ' + second_operand
        elif a == b+2:
            new_first_operand = '  ' + first_operand
            new_second_operand = operator + '   ' + second_operand
        else:
            new_first_operand = '  ' + first_operand
            new_second_operand = operator + '    ' + second_operand
        
        first_operands.append(new_first_operand)
        second_operands.append(new_second_operand)

        #Adding the lines below and spacing the answer
        if a==4 or b==4:
            line = '------'
            if len(answer) == 1:
                new_answer = '     ' + answer
            if len(answer) == 2:
                new_answer = '    ' + answer
            elif len(answer) == 3:
                new_answer = '   ' + answer
            elif len(answer) == 4:
                new_answer = '  ' + answer
            elif len(answer) == 5:
                new_answer = ' ' + answer
            else:
                new_answer = answer
        elif (a==3 and b<4) or (b==3 and a<4):
            line = '-----'
            if len(answer) == 1:
                new_answer = '    ' + answer
            elif len(answer) == 2:
                new_answer = '   ' + answer
            elif len(answer) == 3:
                new_answer = '  ' + answer
            elif len(answer) == 4:
                new_answer = ' ' + answer
            else:
                new_answer = answer
        elif (a==2 and b<3) or (b==2 and a<3):
            line = '----'  
            if len(answer) == 1:
                new_answer = '   ' + answer
            elif len(answer) == 2:
                new_answer = '  ' + answer
            elif len(answer) == 3:
                new_answer = ' ' + answer
            else:
                new_answer = answer
        else:
            line = '---'
            if len(answer) == 1:
                new_answer = '  ' + answer
            elif len(answer) == 2:
                new_answer = ' ' + answer
            else:
                new_answer = answer

        lines.append(line)
        answers.append(new_answer)

    
    #Joining the elements of the problems together leaving 4 spaces between them
    formatted_first_operands = '    '.join(first_operands)
    formatted_second_operands = '    '.join(second_operands)
    formatted_lines = '    '.join(lines)
    formatted_answers = '    '.join(answers)

    #Joining the elements of the problems all together
    if show_answers == True:
        arranged_problems = '\n'.join([formatted_first_operands, formatted_second_operands, formatted_lines, formatted_answers])
    else:
        arranged_problems = '\n'.join([formatted_first_operands, formatted_second_operands, formatted_lines])

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')