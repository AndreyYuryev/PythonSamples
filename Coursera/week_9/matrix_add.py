from sys import stdin
import copy


class Matrix:

    def __init__(self, mlist):
        self.mtrx = copy.deepcopy(mlist)
        self.row = len(self.mtrx)
        self.col = 0
        for itm in self.mtrx:
            self.col = max(self.col, len(itm))

    def __str__(self):
        return '\n'.join(
            ['\t'.join(
                map(
                    str,
                    itmr
                )
            ) for itmr in self.mtrx
            ]
        )

    def size(self):
        return self.row, self.col

    def __mul__(self, other):
        rslt = []
        if isinstance(other, Matrix):
            return rslt
            # row = 0
            # for itmr in self.mtrx:
            #    resc = []
            #    col = 0
            #    for itmc in itmr:
            #        resc.append(int(itmc) + other.mtrx[col][row])
            #        col += 1
            #    rslt.append(resc)
            #    row += 1
            # return Matrix(rslt)

        elif isinstance(other, int) or isinstance(other, float):
            for itmr in self.mtrx:
                resc = []
                for itmc in itmr:
                    resc.append(int(itmc) * other)
                rslt.append(resc)
            return Matrix(rslt)

    def __add__(self, other):
        rslt = []
        if isinstance(other, Matrix):
            row = 0
            for itmr in self.mtrx:
                resc = []
                col = 0
                for itmc in itmr:
                    resc.append(int(itmc) + other.mtrx[row][col])
                    col += 1
                rslt.append(resc)
                row += 1
            return Matrix(rslt)
        elif isinstance(other, int) or isinstance(other, float):
            for itmr in self.mtrx:
                resc = []
                for itmc in itmr:
                    resc.append(int(itmc) + int(other))
                rslt.append(resc)
            return Matrix(rslt)

    def __rmul__(self, other):
        return self.__mul__(other)


# exec(stdin.read())
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(m1)
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m2)
print(m1 + m2)
