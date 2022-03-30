from common.read_xlsx import ReadData
import os


class MutilRead:
    """
        传入一个文件路径，对其中所有xlsx类型文件进行解析
    """

    def __init__(self, path):
        self.filepath = [i[2] for i in os.walk(path)][0]
        self.filename = [j.replace('.xlsx', '') for j in self.filepath]
        self.result = {}
        self.mutil_parse()

    def mutil_parse(self):
        for i in self.filepath:
            t = ReadData('./data/'+i)
            self.result[i.replace('.xlsx', '')] = t.DataDictArray


if __name__ == '__main__':
    c = MutilRead('../data/')
    print(c.filepath,c.filename)