class Kenken:
    def __init__(self, variables, cages):
        self.variables = variables
        self.cages = cages
        self.neighbors = self.get_neighbors()

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

    def get_neighbors(self):
        neighbors = {variable: [] for variable in self.variables}
        for variable in self.variables:
            for neighbor in self.variables:
                if variable == neighbor:
                    continue
                if variable.pos[0] == neighbor.pos[0] or variable.pos[1] == neighbor.pos[1]:
                    neighbors[variable].append(neighbor)
        return neighbors

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

    def forward_checking(self, var, value):
        variables = {v: v.domain.copy() for v in self.neighbors[var]}
        for var in variables:
            variables[var].discard(value)
        return variables

    def update_neighbors_domain(self, domains):
        for variable in domains:
            variable.domain = domains[variable]

    def backtrack_forwardchecking(self):
        if self.is_complete():
            return True

        var = self.select_var()
        old_domains = {v: v.domain.copy() for v in self.neighbors[var]}

        for value in var.domain:
            var.set_val(value)
            new_domain = self.forward_checking(var, value)
            minimum_domain_length = min([len(variable.domain) for variable in new_domain])
            if minimum_domain_length == 0:
                continue

            if self.is_valid(var):
                self.update_neighbors_domain(new_domain)
                success = self.backtrack_forwardchecking()
                if success:
                    return True
                else:
                    self.update_neighbors_domain(old_domains)
            else:
                self.update_neighbors_domain(old_domains)

        var.clear()
        return False

    def backtrack_arc(self):
        return False

    def solve(self, solver=0):
        if solver == 0:
            algo = self.backtrack
        elif solver == 1:
            algo = self.backtrack_forwardchecking
        else:
            algo = self.backtrack_arc

        if algo():
            return [var.value for var in self.variables]

        else:
            "Can't Solve."
