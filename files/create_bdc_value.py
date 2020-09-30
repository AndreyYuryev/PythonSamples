

class BDC_session():
    def __init__(self, ifile, ofile):
        self.ifile = ifile
        self.ofile = ofile

    def create_record(self):
        self.save_bdc_code(self.ofile, self.get_bdc(self.ifile))

    def get_bdc(self, rfile):
        mlist = list()
        with open(rfile, 'r', encoding='UTF-8') as inFile:
            for line in inFile:
                line = line.replace('\n', '')
                mlist.append(list(map(str, line.split('\t'))))
        inFile.close()
        return mlist

    def save_bdc_code(self, wfile, wlist):
        outFile = open(wfile, 'w', encoding='UTF-8')
        for item in wlist:
            #print("( program = '%s' dynpro = '%s' dynbegin = '%s' fnam = '%s' fval = '%s' )" %
            #  ( item[0].replace(' ',''), item[1], item[2].replace(' ', ''), item[3].replace(' ',''), item[4])
            #      , file=outFile )
            if item[2] == 'T':
                line = '" transaction %s' % item[3]
            elif item[0].isspace() and item[2] != 'T':
                line = "( fnam = '%s' fval = '%s' )" \
                       % ( item[3].replace(' ', ''), item[4])
            else:
                line = "( program = '%s' dynpro = '%s' dynbegin = '%s' )" \
                   % ( item[0].replace(' ',''), item[1], item[2].replace(' ', '') )
            print(line, file=outFile)
        outFile.close()


if __name__ == "__main__":
    session = BDC_session(ifile='BDC.txt', ofile='BDC_code.txt')
    session.create_record()