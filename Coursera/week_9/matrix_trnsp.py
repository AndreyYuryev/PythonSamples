from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, mtrx1, mtrx2):
        self.matrix1 = mtrx1
        self.matrix2 = mtrx2


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
                    resc.append(itmc * other)
                rslt.append(resc)
            return Matrix(rslt)

    def __add__(self, other):
        rslt = []
        if isinstance(other, Matrix):
            if self.row != other.row or self.col != other.col:
                raise MatrixError(self, other)
            row = 0
            for itmr in self.mtrx:
                resc = []
                col = 0
                for itmc in itmr:
                    resc.append(itmc + other.mtrx[row][col])
                    col += 1
                rslt.append(resc)
                row += 1
            return Matrix(rslt)
        elif isinstance(other, int) or isinstance(other, float):
            for itmr in self.mtrx:
                resc = []
                for itmc in itmr:
                    resc.append(itmc + other)
                rslt.append(resc)
            return Matrix(rslt)

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        rslt = []
        for icol in range(self.col):
            resc = []
            for irow in range(self.row):
                resc.append(self.mtrx[irow][icol])
            rslt.append(resc)
        self.mtrx = rslt
        self.row = len(self.mtrx)
        self.col = 0
        for itm in self.mtrx:
            self.col = max(self.col, len(itm))
        return self

    @staticmethod
    def transposed(Mtrx):
        return Matrix(Mtrx.mtrx).transpose()


exec(stdin.read())
