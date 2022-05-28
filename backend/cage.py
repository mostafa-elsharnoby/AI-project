class Cage:
    def __init__(self, variables, operation, value):
        self.variables = variables
        self.operation = operation
        self.value = value

        if len(variables) == 1:
            variables[0].value = value

    def is_valid(self):
        if len(self.variables) == 1:
            return True

        if self.operation == '+':
            summation = 0
            for var in self.variables:
                if not var.is_assigned():
                    return True
                summation += var.value

            if summation == self.value:
                return True
            else:
                return False

        elif self.operation == '*':
            multi = 1
            for var in self.variables:
                if not var.is_assigned():
                    return True
                multi *= var.value

            if multi == self.value:
                return True
            else:
                return False

        elif self.operation == '-':
            if not self.variables[0].is_assigned() or not self.variables[1].is_assigned():
                return True

            if self.value == abs(self.variables[0].value - self.variables[1].value):
                return True
            else:
                return False

        elif self.operation == '/':
            if not self.variables[0].is_assigned() or not self.variables[1].is_assigned():
                return True
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
