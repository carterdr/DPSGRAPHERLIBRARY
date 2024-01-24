import openpyxl
class Excel():
    def __init__ (self, name, placeInColumn = None):
        self.name = name
        self.wb = openpyxl.load_workbook("Dps.xlsx")
        self.sh1 = self.wb["Sheet1"]
        self.column = self.getOpenColumn()
        if placeInColumn != None:
           self.column = placeInColumn
           self.name = self.sh1.cell(1, self.column).value + " + " + name 
        self.sh1.cell(1,self.column,self.name)     
    def getOpenColumn(self):
        column = 2         
        while(not self.sh1.cell(1,column).value==None):
            if(not self.sh1.cell(1,column).value==None):
                column+=1       
        return column     
    def createTime():
        wb = openpyxl.load_workbook("Dps.xlsx")
        sh1 = wb["Sheet1"]
        sh1.cell(row=1, column=1, value="Seconds")
        for row in range(1001):
            sh1.cell(row=row+2, column=1).value = "{:.1f}".format(row/10)
            print(sh1.cell(row+2, 1).value)             
        wb.save("Dps.xlsx")
    def closeExcel (self, damagetimes):
        for row, value in damagetimes:
            current_value = self.sh1.cell(row+1, self.column).value
            if current_value is None:
                current_value = 0
            self.sh1.cell(row+1, self.column).value = int(format(value + current_value,".0f"))
        self.__fillGaps()
        self.wb.save("Dps.xlsx")        
        return self.column
    def __fillGaps(self):
        currentMax = self.sh1.cell(2, self.column).value
        if currentMax == None:
            currentMax = 0 
        for row in range(2, 1001):
            value = self.sh1.cell(row,self.column).value
            if value != None and value > currentMax:
                currentMax = value
            self.sh1.cell(row,self.column).value = int(currentMax)
    def clearExcel():
        book = openpyxl.load_workbook("Dps.xlsx") #get the file name
        sheet = book.get_sheet_by_name('Sheet1') #get the sheet name
        for a in sheet['A1':'Z1002']: #you can set the range here 
            for cell in a:
                cell.value = None #set a value or null here
        book.save("Dps.xlsx")