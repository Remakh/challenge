import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""

        tokens = rpn.split(" ")
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == "*":
                    stack.append(operand1 * operand2)
                elif token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand2 - operand1)
                else:
                    stack.append(operand2 // operand1)
        return stack.pop()
