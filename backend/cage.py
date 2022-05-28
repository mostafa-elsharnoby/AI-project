class Cage:
    def __init__(self, variables, operation, value):
        self.variables = variables
        self.operation = operation
        self.value = value

    def is_valid(self):
        if self.operation == '+':
            sum = 0
            for var in self.variables:
                if var.value is None:
                    return False
                sum += var.value
            if sum == self.value:
                return True
            else:
                return False

        elif self.operation == '*':
            multi = 1
            for var in self.variables:
                if var.value is None:
                    return False
                multi *= var.value
            if multi == self.value:
                return True
            else:
                return False

        elif self.operation == '-':
            result = 0
            if self.variables[0].value is None or self.variables[1].value is None:
                return False

            if self.value == abs(self.variables[0].value - self.variables[1].value):
                return True
            else:
                return False

        elif self.operation == '/':
            result = 1
            if self.variables[0].value is None or self.variables[1].value is None:
                return False
            else:
                if self.variables[0].value > self.variables[1].value:
                    if self.value == self.variables[0].value / self.variables[1].value:
                        return True
                    else:
                        return False
                else:
                    if self.value == self.variables[1].value / self.variables[0].value:
                        return True
                    else:
                        return False

        return False
