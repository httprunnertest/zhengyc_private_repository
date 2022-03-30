import xlrd


class ReadData:

    def __init__(self, file):
        self.file = xlrd.open_workbook(file)
        self.sheet_name = self.file.sheet_names()[0:-1]
        self.env = self.file.sheet_by_name('env')
        self.DataDictArray = {}
        self.EnvDict = {}
        self.parse_array()

    def parse_array(self):
        self.EnvDict = dict(zip(self.env.row_values(0), self.env.row_values(1)))
        for index, sheet_name in enumerate(self.sheet_name):
            dataarray = []
            for i in range(1, self.file.sheet_by_name(sheet_name).nrows):
                if not self.file.sheet_by_name(sheet_name).row_values(i)[0]:
                    k = self.file.sheet_by_name(sheet_name).row_values(i)
                    k[0] = dataarray[i - 2].get('操作名称')
                    dataarray.append(dict(zip(self.file.sheet_by_name(sheet_name).row_values(0), k)))
                else:
                    dataarray.append(dict(zip(self.file.sheet_by_name(sheet_name).row_values(0),
                                              self.file.sheet_by_name(sheet_name).row_values(i))))
            self.DataDictArray[sheet_name] = self.parse_dict(dataarray, index == len(self.sheet_name)-1)

    def parse_dict(self, array, bol):
        array.insert(0,
                     {'操作名称': '打开浏览器', '操作步骤': f"打开{self.EnvDict['浏览器']}浏览器", '定位方式': '', '定位内容': self.EnvDict['浏览器'],
                      '操作': '初始化', '输入值/定位': self.EnvDict['环境']})
        if bol:
            array.append(
                {'操作名称': '关闭浏览器', '操作步骤': '', '定位方式': '', '定位内容': '', '操作': '关闭', '输入值/定位': ''})
        datadict = {}
        for data in array:
            newdata = data.copy()
            newdata.pop('操作名称')
            if data['操作名称'] not in datadict:
                datadict[data['操作名称']] = [newdata]
            else:
                datadict[data['操作名称']].append(newdata)
        return datadict


if __name__ == '__main__':
    file = ReadData('../data/综合看板.xlsx')
    print(file.DataDictArray)

