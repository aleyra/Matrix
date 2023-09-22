# https://github.com/aleyra/42IA_bootcamp_python/blob/master/module01/ex02/test.py

error0 = "values: list of list of floats (for row vector) or list of lists "
error0 += "of single float (for column vector)"
error1 = "the list must contain lists of 1 float or 1 list of several floats"
error2 = "the list must contain lists of 1 float"
error3 = "the list must contain 1 list of floats"
error4 = "this is between 2 vectors of same shape"
error5 = "this is between a vector and a scalar"


class Vector:
    def __init__(self, values):
        # checks
        assert isinstance(values, list), error0
        if (len(values) != 1):  # case column
            for i in range(len(values)):
                assert isinstance(values[i], list), error1
                assert len(values[i]) == 1, error2
                assert (
                    isinstance(values[i][0], float)
                    or isinstance(values[i][0], int)
                ), error2
        else:  # case line
            assert isinstance(values[0], list), error3
            for i in range(len(values[0])):
                assert (
                    isinstance(values[0][i], float)
                    or isinstance(values[0][i], int)
                ), error3

        # init
        self.values = values
        self.shape = [0, 0]
        if (len(values) != 1):  # case column
            self.shape[0] = len(values)
            self.shape[1] = 1
        else:  # case line
            self.shape[0] = 1
            self.shape[1] = len(values[0])
        self.shape = tuple(self.shape)

    # overload
    def __str__(self) -> str:
        to_print = "["
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                to_print += f"[{self.values[i][0]}]"
                if i != len(self.values) - 1:
                    to_print += ", "
            to_print += "]"
        else:  # case line
            to_print += "["
            for i in range(len(self.values[0])):
                to_print += f"{self.values[0][i]}"
                if i != len(self.values[0]) - 1:
                    to_print += ", "
            to_print += "]]"
        return to_print

    def __repr__(self) -> str:
        to_print = "["
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                to_print += f"[{self.values[i][0]}]"
                if i != len(self.values) - 1:
                    to_print += ", "
            to_print += "]"
        else:  # case line
            to_print += "["
            for i in range(len(self.values[0])):
                to_print += f"{self.values[0][i]}"
                if i != len(self.values[0]) - 1:
                    to_print += ", "
            to_print += "]]"
        return to_print
        # return str(self)

    def __add__(self, v):
        # check
        if not isinstance(v, Vector) or self.shape != v.shape:
            print(error4)
            return None
        # prog
        values = []
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                values.append([self.values[i][0] + v.values[i][0]])
        else:  # case line
            for i in range(len(self.values[0])):
                values.append(self.values[0][i] + v.values[0][i])
            values = [values]
        return Vector(values)

    def __sub__(self, v):
        # check
        assert self.shape == v.shape, error4
        # prog
        values = []
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                values.append([self.values[i][0] - v.values[i][0]])
        else:  # case line
            for i in range(len(self.values[0])):
                values.append(self.values[0][i] - v.values[0][i])
            values = [values]
        return Vector(values)

    def __mul__(self, l_hand):
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), error5
        values = []
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                values.append([self.values[i][0] * l_hand])
        else:  # case line
            for i in range(len(self.values[0])):
                values.append(self.values[0][i] * l_hand)
            values = [values]
        return Vector(values)

    def __rmul__(self, l_hand):
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), error5
        values = []
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                values.append([self.values[i][0] * l_hand])
        else:  # case line
            for i in range(len(self.values[0])):
                values.append(self.values[0][i] * l_hand)
            values = [values]
        return Vector(values)

    def __truediv__(self, l_hand):
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), error5
        values = []
        if (l_hand == 0):
            try:
                self.values[0][0] / 0
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
        if self.shape[0] != 1:  # case column
            for i in range(len(self.values)):
                values.append([self.values[i][0] / l_hand])
        else:  # case line
            for i in range(len(self.values[0])):
                values.append(self.values[0][i] / l_hand)
            values = [values]
        return Vector(values)

    def __rtruediv__(self, l_hand):
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), error5
        try:
            l_hand / [self.values[0][0]]
        except NotImplementedError:
            raise NotImplementedError(
                "Division of a scalar by a Vector is not defined here."
            )

    # methods
    def dot(self, v):
        # checks
        assert isinstance(v, Vector), error4
        assert self.shape == v.shape, error4
        # prog
        res = 0.
        if v.shape[1] == 1:  # case column
            for i in range(len(v.values)):
                res += self.values[i][0] * v.values[i][0]
        else:  # case line
            for i in range(len(self.values[0])):
                res += self.values[0][i] * v.values[0][i]
        return res

    def T(self):
        values = []
        if self.shape[1] == 1:  # case column -> line
            for i in range(len(self.values)):
                values.append(self.values[i][0])
            values = [values]
        else:  # case line -> column
            for i in range(len(self.values[0])):
                values.append([self.values[0][i]])
        return Vector(values)
