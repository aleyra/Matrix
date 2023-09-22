# https://github.com/aleyra/42IA_bootcamp_python/blob/master/module01/ex02/test.py

vec_error0 = "values: list of list of floats (for row vector) or list of lists"
vec_error0 += " of single float (for column vector)"
vec_error1 = "the list must contain lists of 1 float or 1 list of several "
vec_error1 += "floats"
vec_error2 = "the list must contain lists of 1 float"
vec_error3 = "the list must contain 1 list of floats"
vec_error4 = "this is between 2 vectors of same shape"
vec_error5 = "this is between a vector and a scalar"
mat_error0 = "Must be an list of lists of float or int"
mat_error1 = "Each list in main list must have the same size"
mat_error2 = "Shape must be a tuple of 2 int positive"
mat_error3 = "Shape must be a tuple of 2 int > 0"
mat_error4 = "Must init with a list or a tuple"
mat_error5 = "Add is between 2 matrices of same dimensions"
mat_error6 = "Substract is between 2 matrices of same dimensions"
mat_error7 = "M x N is possible only if M's nb_line = N's nb_col"
mat_error8 = """Multiplication is possible between :
    - matrix and scalar
    - matrix and vector
    - matrix and matrix"""
mat_error9 = """Multiplication is possible between :
    - scalar and matrix
    - vector and matrix
    - matrix and matrix"""


class Vector:
    def __init__(self, values):
        # checks
        assert isinstance(values, list), vec_error0
        if (len(values) != 1):  # case column
            for i in range(len(values)):
                assert isinstance(values[i], list), vec_error1
                assert len(values[i]) == 1, vec_error2
                assert (
                    isinstance(values[i][0], float)
                    or isinstance(values[i][0], int)
                ), vec_error2
        else:  # case line
            assert isinstance(values[0], list), vec_error3
            for i in range(len(values[0])):
                assert (
                    isinstance(values[0][i], float)
                    or isinstance(values[0][i], int)
                ), vec_error3

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
            print(vec_error4)
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
        assert self.shape == v.shape, vec_error4
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
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), vec_error5
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
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), vec_error5
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
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), vec_error5
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
        assert (isinstance(l_hand, float) or isinstance(l_hand, int)), vec_error5
        try:
            l_hand / [self.values[0][0]]
        except NotImplementedError:
            raise NotImplementedError(
                "Division of a scalar by a Vector is not defined here."
            )

    # methods
    def dot(self, v):
        # checks
        assert isinstance(v, Vector), vec_error4
        assert self.shape == v.shape, vec_error4
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


class Matrix:
    def __init__(self, obj) -> None:
        # init by values
        if isinstance(obj, list):
            # checks
            nb_line = len(obj)
            if (nb_line == 0):
                raise TypeError(mat_error0)
            for i in range(nb_line):
                if (not isinstance(obj[i], list)):
                    raise TypeError(mat_error0)
                nb_col = len(obj[0])
                if (nb_col == 0):
                    raise TypeError(mat_error0)
                if (len(obj[i]) != nb_col):
                    raise TypeError(mat_error1)
                for j in range(len(obj[i])):
                    if (not isinstance(obj[i][j], float)
                        and not isinstance(obj[i][j], int)):
                        raise TypeError(mat_error0)
            # init
            self.shape = (nb_line, nb_col)
            self.data = obj
        # init by shape
        elif isinstance(obj, tuple):
            # checks
            if len(obj) != 2:
                raise TypeError(mat_error2)
            if not isinstance(obj[0], int) or not isinstance(obj[1], int):
                raise TypeError(mat_error3)
            if obj[0] < 1 or obj[1] < 1:
                raise TypeError(mat_error3)
            # init
            self.shape = obj
            self.data = []
            for i in range(obj[0]):
                t = []
                for j in range(obj[1]):
                    t.append(0)
                self.data.append(t)
        else:
            raise TypeError(mat_error4)
        
    # add : only matrices of same dimensions.
    def __add__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError(mat_error5)
        if self.shape != m.shape:
            raise TypeError(mat_error5)
        res = Matrix(m.shape)
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                res.data[i][j] = self.data[i][j] + m.data[i][j]
        return res
        
    def __radd__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError(mat_error5)
        if self.shape != m.shape:
            raise TypeError(mat_error5)
        res = Matrix(m.shape)
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                res.data[i][j] = m.data[i][j] + self.data[i][j]
        return res
    
    # sub : only matrices of same dimensions.
    def __sub__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError(mat_error6)
        if self.shape != m.shape:
            raise TypeError(mat_error6)
        res = Matrix(m.shape)
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                res.data[i][j] = self.data[i][j] - m.data[i][j]
        return res
        
    def __rsub__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError(mat_error6)
        if self.shape != m.shape:
            raise TypeError(mat_error6)
        res = Matrix(m.shape)
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                res.data[i][j] = m.data[i][j] - self.data[i][j]
        return res
    
    # div : only scalars.
    def __truediv__(self, l):
        if not isinstance(l, int) and not isinstance(l, float):
            raise TypeError(
                "TrueDiv is only between a matrix and a scalar (int or float)"
            )
        if l == 0:
            raise ZeroDivisionError("Division by zero impossible")
        res = Matrix(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                res.data[i][j] = self.data[i][j] / l
        return res
    
    def __rtruediv__(self, l):
        raise NotImplementedError("Impossible to divise a scalar by a matrix")
    
    # mul : scalars, vectors and matrices , can have errors with vectors and
    # matrices,
    # returns a Vector if we perform Matrix * Vector mutliplication.
    def __mul__(self, l):
        if isinstance(l, int) or isinstance(l, float):  # case scalar
            res = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res.data[i][j] = self.data[i][j] * l
            return res
        # case Vector NOTTODO because done in Vector's class
        elif isinstance(l, Matrix):  # case matrix
            if self.shape[1] != l.shape[0]:
                raise TypeError(mat_error7)
            res = Matrix((self.shape[0], l.shape[1]))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    for k in range(self.shape[1]):
                        res.data[i][j] += self.data[i][k] * l.data[k][j]
            return res
        else:
            raise TypeError(mat_error8)
        
    def __rmul__(self, r):
        if isinstance(r, int) or isinstance(r, float):  # case scalar
            res = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res.data[i][j] = r * self.data[i][j]
            return res
        elif isinstance(r, Matrix):  # case matrix
            if r.shape[1] != self.shape[0]:
                raise TypeError(mat_error7)
            res = Matrix((r.shape[0], self.shape[1]))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    for k in range(r.shape[1]):
                        res.data[i][j] += r.data[i][k] * self.data[k][j]
            return res
        else:
            raise TypeError(mat_error9)

    def __str__(self) -> str:
        to_print = f"shape = {self.shape}\n["
        for i in range(self.shape[0]):
            to_print += f"\n\t{self.data[i]}"
        to_print += "\n]"
        return to_print
    
    def __repr__(self) -> str:
        to_print = f"["
        for i in range(self.shape[0]):
            to_print += f"\n\t{self.data[i]}"
        to_print += "\n]"
        return to_print
    
    def T(self):
        res = Matrix((self.shape[1],self.shape[0]))
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[j][i]
        return res

    
class Vector(Matrix):
    def __init__(self, obj) -> None:
        # init by shape
        if isinstance(obj, tuple):
            # checks
            if len(obj) != 2:
                raise TypeError(mat_error2)
            if not isinstance(obj[0], int) or not isinstance(obj[1], int):
                raise TypeError(mat_error2)
            if (obj[0] != 1 and obj[1] != 1) or obj[0] < 1 or obj[1] < 1:
                raise TypeError("Shape must be (1,n) or (n,1)")
            # init
            self.shape = obj
            self.data = []
            for i in range(self.shape[0]):
                t = []
                for j in range(self.shape[1]):
                    t.append(0)
                self.data.append(t)
        # init by values
        elif isinstance(obj, list):
            if len(obj) != 1:  # case column
                #checks
                for i in range(len(obj)):
                    if not isinstance(obj[i], list):
                        raise TypeError(
                            "the list must contain lists of 1 "
                            + "float or 1 list of several floats"
                        )
                    if len(obj[i]) != 1:
                        raise TypeError(
                            "the list must contain lists of 1 float"
                        )
                    if (
                        not isinstance(obj[i][0], int)
                        and not isinstance(obj[i][0], float)
                    ):
                        raise TypeError(
                            "the list must contain lists of 1 float"
                        )
                #init
                self.data = obj
                self.shape = (len(obj), 1)
            else:  # case line
                # checks
                if not isinstance(obj[0], list):
                    raise TypeError("the list must contain 1 list of floats")
                for i in range(len(obj[0])):
                    if (
                        not isinstance(obj[0][i], int)
                        and not isinstance(obj[0][i], float)
                    ):
                        raise TypeError(
                            "the list must contain 1 list of floats"
                        )
                # init
                self.data = obj
                self.shape = (1, len(obj[0]))
        else:
            raise TypeError(mat_error4)
    
    def __add__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Add is between 2 vectors of same dimensions")
        if self.shape != v.shape:
            raise TypeError("Add is between 2 vectors of same dimensions")
        res = Vector(v.shape)
        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                res.data[i][j] = self.data[i][j] + v.data[i][j]
        return res
    
    def __radd__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Add is between 2 vectors of same dimensions")
        if self.shape != v.shape:
            raise TypeError("Add is between 2 vectors of same dimensions")
        res = Vector(v.shape)
        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                res.data[i][j] = v.data[i][j] + self.data[i][j]
        return res
    
    def __sub__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Sub is between 2 vectors of same dimensions")
        if self.shape != v.shape:
            raise TypeError("Sub is between 2 vectors of same dimensions")
        res = Vector(v.shape)
        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                res.data[i][j] = self.data[i][j] - v.data[i][j]
        return res
    
    def __rsub__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Sub is between 2 vectors of same dimensions")
        if self.shape != v.shape:
            raise TypeError("Sub is between 2 vectors of same dimensions")
        res = Vector(v.shape)
        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                res.data[i][j] = v.data[i][j] - self.data[i][j]
        return res
    
    def __truediv__(self, l):
        if not isinstance(l, int) and not isinstance(l, float):
            raise TypeError(
                "TrueDiv is only between a vector and a scalar (int or float)"
            )
        if l == 0:
            raise ZeroDivisionError("Division by zero impossible")
        res = Vector(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                res.data[i][j] = self.data[i][j] / l
        return res
    
    def __rtruediv__(self, l):
        raise NotImplementedError("Impossible to divise a scalar by a vector")
    
    def __mul__(self, l):
        if isinstance(l, int) or isinstance(l, float):  # case scalar
            res = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res.data[i][j] = self.data[i][j] * l
            return res
        elif isinstance(l, Vector):  # case Vector
            if self.shape[0] != 1:
                raise TypeError(
                    "Impossible to do v x u when v is a vector column"
                )
            if l.shape[1] != 1:
                raise TypeError(
                    "Impossible to do v x u when u is a vector line"
                )
            if self.shape[1] != l.shape[0]:
                raise TypeError(
                    "Impossible to do v x u when v's nb_col != u's nb_line"
                )
            res = Vector((1,1))
            for i in range(l.shape[0]):
                res.data[0][0] += self.data[0][i] * l.data[i][0]
            return res
        elif isinstance(l, Matrix):  # case matrix
            if self.shape[0] != 1:
                raise TypeError(
                    "Impossible to do v x M when v is a vector column"
                )
            if self.shape[1] != l.shape[0]:
                raise TypeError(
                    "v x M is possible only if M's nb_line = v's nb_col"
                )
            res = Vector((self.shape[0], l.shape[1]))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    for k in range(self.shape[1]):
                        res.data[i][j] += self.data[i][k] * l.data[k][j]
            return res
        else:
            raise TypeError(
                """Multiplication is possible between :
    - vector and scalar
    - vector and vector
    - vector and matrix"""
            )

    def __rmul__(self, r):
        if isinstance(r, int) or isinstance(r, float):  # case scalar
            res = Vector(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res.data[i][j] = r * self.data[i][j]
            return res
        elif isinstance(r, Vector):  # case Vector
            if self.shape[0] != 1:
                raise TypeError(
                    "Impossible to do v x u when v is a vector column"
                )
            if r.shape[1] != 1:
                raise TypeError(
                    "Impossible to do v x u when u is a vector line"
                )
            if r.shape[1] != self.shape[0]:
                raise TypeError(
                    "Impossible to do v x u when v's nb_col != u's nb_line"
                )
            res = Vector((1,1))
            for i in range(self.shape[0]):
                res.data[0][0] += r.data[0][i] * self.data[i][0]
            return res
        elif isinstance(r, Matrix):  # case matrix
            if self.shape[1] != 1:
                raise TypeError(
                    "Impossible to do M x v when v is a vector line"
                )
            if r.shape[1] != self.shape[0]:
                raise TypeError(
                    "v x M is possible only if M's nb_line = v's nb_col"
                )
            res = Vector((r.shape[0], self.shape[1]))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    for k in range(r.shape[1]):
                        res.data[i][j] += r.data[i][k] * self.data[k][j]
            return res
        else:
            raise TypeError(
                """Multiplication is possible between :
    - scalar and vector
    - vector and vector
    - matrix and vector"""
            )

    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError(
                "dot product is possible only between 2 vectors of same shape"
            )
        if v.shape != self.shape:
            raise TypeError(
                "dot product is possible only between 2 vectors of same shape"
            )
        res = 0.
        if v.shape[0] == 1:
            for i in range(v.shape[1]):
                res += self.data[0][i] * v.data[0][i]
        else:
            for i in range(v.shape[0]):
                res += self.data[i][0] * v.data[i][0]
        return res

    def T(self):
        res = Vector((self.shape[1], self.shape[0]))
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[j][i]
        return res
