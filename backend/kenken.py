class Kenken:
    def __init__(self, variables=[], cages=[]):
        self.variables = variables
        self.cages = cages

    def is_valid_row(self, var):
        row_values = [variable.value for variable in self.variables
                      if variable.pos[0] == var.pos[0] and variable.is_assigned()]
        unq_row_values = set(row_values)
        return len(unq_row_values) == len(row_values)

    def is_valid_col(self, var):
        col_values = [variable.value for variable in self.variables
                      if variable.pos[1] == var.pos[1] and variable.is_assigned()]
        unq_col_values = set(col_values)
        return len(unq_col_values) == len(col_values)

    def select_var(self):
        unassigned_vars = [var for var in self.variables if not var.is_assigned()]
        return min(unassigned_vars, key=lambda var: len(var.domain))

    def find_cage(self, var):
        for cage in self.cages:
            if var in cage.variables:
                return cage

        raise Exception("ERROR!!!!! Variable Not Found")

    def is_complete(self):
        return all(var.is_assigned() for var in self.variables)

    def is_valid(self, var):
        var_cage = self.find_cage(var)
        return var_cage.is_valid() and self.is_valid_col(var) and self.is_valid_row(var)

    def backtrack(self):
        if self.is_complete():
            return True

        var = self.select_var()
        for value in var.domain:
            var.set_val(value)

            if self.is_valid(var):
                success = self.backtrack()
                if success:
                    return True

        var.clear()
        return False

    def solve(self):
        if self.backtrack():
            return [var.value for var in self.variables]

        else:
            "Can't Solve."
