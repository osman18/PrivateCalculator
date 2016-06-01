import re
from collections import deque


class Calculator:

    def process_add_minus(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '+':
                tmp = float(result.pop()) + float(input.popleft())
                result.append(tmp)
            elif data == '-':
                tmp = float(result.pop()) - float(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def process_times_divided(self, input):
        result = deque()
        while len(input) > 0:
            data = input.popleft()
            if data == '*':
                tmp = float(result.pop()) * float(input.popleft())
                result.append(tmp)
            elif data == '/':
                tmp = float(result.pop()) / float(input.popleft())
                result.append(tmp)
            else:
                result.append(data)
        return result

    def cal(self, question):
        data = deque(re.split(r'([+]|[-]|[/]|[*])', question.replace(' ', '')))

        result = self.process_times_divided(data)
        result = self.process_add_minus(result)

        return result.pop()


class Calculator2:

    def parseString(self, formula):
        stack = ['$']
        output = []
        formula = filter(lambda a: a != '', formula)

        for token in formula:
            token = str(token)
            if token in ['+', '-', '*', '/', '(', ')']:
                operator_last = stack.pop()

                if self.operator_priority(token, operator_last) is True:
                    stack.append(operator_last)
                    stack.append(token)
                else:
                    output.append(operator_last)
                    operator_last = stack.pop()
                    while (self.operator_priority(token,
                                                  operator_last) is False):
                        output.append(operator_last)
                        operator_last = stack.pop()
                        if operator_last == '(' and token == ')':
                            break
                    if operator_last == '$' or\
                            self.operator_priority(token,
                                                   operator_last) is True:
                        stack.append(operator_last)
                        stack.append(token)
            else:
                output.append(token)

        while (len(stack) > 1):
            output.append(stack.pop())

        output = filter(lambda a: a != '(', output)
        output = filter(lambda a: a != ')', output)
        return output

    def operator_priority(self, operator_now, operator_last):
        priority = {'(': 1, ')': 4, '*': 2, '/': 2, '+': 3, '-': 3, '$': 4}
        # print 'operator_last = ' + operator_last + '; token = ' +
        # operator_now
        if operator_last is '(':
            return True
        if priority[operator_now] < priority[operator_last]:
            return True
        else:
            return False

    def plus(self, number1, number2):
        return float(number1) + float(number2)

    def minus(self, number1, number2):
        return float(number1) - float(number2)

    def times(self, number1, number2):
        return float(number1) * float(number2)

    def devide(self, number1, number2):
        return float(number1) / float(number2)

    def cal(self, formula):
        formula = formula.encode('utf8')
        formula = re.split(
            r'([+]|[-]|[/]|[*]|[(]|[)])', formula.replace(' ', ''))
        post_order = self.parseString(formula)
        post_order.reverse()
        temp = []

        while(len(post_order) > 0):
            element = post_order.pop()
            if element not in ['+', '-', '*', '/']:
                temp.append(element)
            elif element == '+':
                n2 = temp.pop()
                n1 = temp.pop()
                result = self.plus(n1, n2)
                temp.append(str(result))
            elif element == '-':
                n2 = temp.pop()
                n1 = temp.pop()
                result = self.minus(n1, n2)
                temp.append(result)
            elif element == '*':
                n2 = temp.pop()
                n1 = temp.pop()
                result = self.times(n1, n2)
                temp.append(result)
            elif element == '/':
                n2 = temp.pop()
                n1 = temp.pop()
                result = self.devide(n1, n2)
                temp.append(result)

        return float(temp[0])
