import webhandler

class QuerySolver(object):
    def __init__(self):
        pass        

    def answer_query(self, query):
        """Answer a query"""
        a = query.split(" ")
        if (len(a) == 5):
            print(a)
            c = 0
            operators = [a[1], a[3]]
            print(a)
            print(operators)

            d = {"*":2, "-":1, "+":1, "/":2}
            a[0] = int(a[0])
            a[2] = int(a[2])
            a[4] = int(a[4])
            
            if (d[operators[0]] == d[operators[1]]):
                if operators[0] == "*":
                    c = a[0] * a[2]
                else:
                    c = a[0] / a[2]

                if operators[1] == "*":
                    c = c*a[4]
                else: 
                    c = c/a[4]
            elif (d[operators[0]] > d[operators[1]]):
                if operators[0] == "*":
                    c = a[0] * a[2]
                else:
                    c = a[0] / a[2]

                if operators[1] == "+":
                    c = c+a[4]
                else: 
                    c = c-a[4]
            else:
                if operators[1] == "*":
                    c = a[2] * a[4]
                else:
                    c = a[2] / a[4]

                if operators[0] == "+":
                    c = a[0] + c
                else: 
                    c = a[0] - c

            return c