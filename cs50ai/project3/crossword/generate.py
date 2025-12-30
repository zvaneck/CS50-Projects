import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        for var in self.domains:
            accepted_words = set()
            for word in self.domains[var]:
                if len(word) == var.length:
                    accepted_words.add(word)
            self.domains[var] = accepted_words



    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        removed = False
        match_found = False
        to_be_removed = set()
        i, j = self.crossword.overlaps[(x, y)]

        for word_x in self.domains[x]:
            match_found = False
            for word_y in self.domains[y]:
                if word_x[i] != word_y[j]:
                    continue
                else:
                    match_found = True
                    break

            if match_found == False:
                to_be_removed.add(word_x)

        if len(to_be_removed) != 0:
            self.domains[x] -= to_be_removed
            removed = True

        return removed

        raise NotImplementedError

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        if arcs is None:
            arcs = []
            for arc in self.crossword.overlaps:
                if self.crossword.overlaps[arc] is not None:
                    arcs.append(arc)

        while arcs:
            arc = arcs.pop(0)
            x, y = arc

            if self.revise(x, y):
                for neighbor in self.crossword.neighbors(x):
                    if neighbor != y:
                        arcs.append((neighbor, x))

                # If domain emptied during revise, no solution
                if len(self.domains[x]) == 0:
                    return False

        return True


        raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        for var in self.crossword.variables:
            if var in assignment:
                continue
            else:
                return False

        return True

        raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        seen_values = set()

        for var in assignment:
            if var.length != len(assignment[var]):
                return False
            word = assignment[var]
            if word in seen_values:
                return False
            seen_values.add(word)
        for v1, v2 in self.crossword.overlaps:
            if v1 in assignment and v2 in assignment:
                overlap = self.crossword.overlaps[(v1, v2)]
                if overlap is not None:
                    i, j = overlap
                    if assignment[v1][i] != assignment[v2][j]:
                        return False
        return True

        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for crossighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        elimination_counts = {}

        for word in self.domains[var]:
            elimination_count = 0

            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    continue

                i, j = self.crossword.overlaps[(var, neighbor)]
                letter = word[i]

                for neighbor_word in self.domains[neighbor]:
                    if neighbor_word[j] != letter:
                        elimination_count += 1

            elimination_counts[word] = elimination_count

        sorted_eliminations = sorted(elimination_counts.items(), key=lambda item: item[1])
        ordered_words = [word for word, count in sorted_eliminations]

        return ordered_words

        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        unassigned = []

        for var in self.domains:
            if var not in assignment:
                unassigned.append((var, len(self.domains[var]), len(self.crossword.neighbors(var))))

        return min(unassigned, key=lambda item: (item[1], -item[2]))[0]

        raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if all(var in assignment for var in self.crossword.variables):
            return assignment

        next_var = self.select_unassigned_variable(assignment)

        next_domain = self.order_domain_values(next_var, assignment)

        for word in next_domain:
            assignment[next_var] = word
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result is not None:
                    return result
            del assignment[next_var]

        return None


        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
