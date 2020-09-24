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

exec(stdin.read())
