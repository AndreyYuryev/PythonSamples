from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, mtrx1, mtrx2):
        self.matrix1 = mtrx1
        self.matrix2 = mtrx2
        self.descr = 'Dimension is wrong'


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
            if self.col != other.row:   # or self.row != other.col:
                raise MatrixError(self, other)
            other2 = Matrix.transposed(other)
            for irow in range(self.row):
                resc = []
                for irow2 in range(other2.row):
                    val = 0
                    for icol in range(self.col):
                        v1 = self.mtrx[irow][icol]
                        v2 = other2.mtrx[irow2][icol]
                        val += v1 * v2
                    resc.append(val)
                rslt.append(resc)
            return Matrix(rslt)
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
#  m1 = Matrix([[1, 2, 4], [2, 0, 3]])
#  print(m1)
#  m1.transpose()
#  print(Matrix.transposed(m1))
#  m2 = Matrix([[2, 5], [1, 3], [1, 1]])
#  print(m2)
#  try:
#    print(m1 * m2)
#  except MatrixError as me:
#    print(me.matrix1, me.matrix2, me.descr)
# m = Matrix([[10, 10], [0, 0], [1, 1]])
#  print(m)
#  print(Matrix.transposed(m))
#  print(m)
