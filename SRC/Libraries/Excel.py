import openpyxl
import matplotlib.pyplot as plt
import os
class Excel():
    def __init__ (self, name, placeInColumn = None):
        self.name = name
        self.wb = openpyxl.load_workbook("DPS.xlsx")
        self.sh1 = self.wb["Sheet1"]
        self.column = Excel.getOpenColumn(self.sh1)
        if placeInColumn != None:
           self.column = placeInColumn
           self.name = self.sh1.cell(1, self.column).value + " + " + name 
        self.sh1.cell(1,self.column,self.name)     
    def getOpenColumn(sheet):
        column = 2         
        while(not sheet.cell(1,column).value==None):
            if(not sheet.cell(1,column).value==None):
                column+=1  
        return column    
    def getExcelPath():
        caller_directory = os.path.dirname(os.path.realpath(__file__))
        # Move up one directory to reach the parent directory (SRC)
        project_directory = os.path.dirname(caller_directory)
        # Construct the full path to Dps.xlsx
        return os.path.join(project_directory, "Dps.xlsx")
    def createTime():
        wb = openpyxl.load_workbook("DPS.xlsx")
        sh1 = wb["Sheet1"]
        sh1.cell(row=1, column=1, value="Seconds")
        for row in range(1001):
            sh1.cell(row=row+2, column=1).value = "{:.1f}".format(row/10)           
        wb.save("DPS.xlsx")
    def closeExcel (self, damagetimes):
        for row, value in damagetimes:
            current_value = self.sh1.cell(row+1, self.column).value
            if current_value is None:
                current_value = 0
            self.sh1.cell(row+1, self.column).value = int(format(value + current_value,".0f"))
        self.__fillGaps()
        self.wb.save("DPS.xlsx")        
        return self.column
    def __fillGaps(self):
        currentMax = self.sh1.cell(2, self.column).value
        if currentMax == None:
            currentMax = 0 
        for row in range(2, 1003):
            value = self.sh1.cell(row,self.column).value
            if value != None and value > currentMax:
                currentMax = value
            self.sh1.cell(row,self.column).value = int(currentMax)
    def clearExcel():
        file_path = Excel.getExcelPath()
        book = openpyxl.load_workbook("DPS.xlsx") #get the file name
        sheet = book.get_sheet_by_name('Sheet1') #get the sheet name
        for a in sheet['A1':'Z1002']: #you can set the range here 
            for cell in a:
                cell.value = None #set a value or null here
        book.save("DPS.xlsx")
    def displayData():
        file_path = Excel.getExcelPath()
        # Load the workbook and select the active sheet
        wb = openpyxl.load_workbook("DPS.xlsx")
        sheet = wb.active
        # Read the 'seconds' column (assuming it is the first column)
        open_column = Excel.getOpenColumn(sheet)
        max_row = Excel.getFinalDamageRow(sheet, open_column)
        seconds = [float(sheet.cell(row=i, column=1).value) for i in range(2, max_row + 1)]

        # Create a figure and an axis object
        fig, ax = plt.subplots(figsize=(15, 8))

        
        for column in range(2, open_column):
            damage = [float(sheet.cell(row=i, column=column).value) for i in range(2, max_row + 1)]
            name = sheet.cell(1, column).value
            ax.step(seconds, damage, where='post', label=name, linewidth=2)

        # Setting the labels and title
        ax.set_xlabel('Time (Seconds)', fontsize=14)
        ax.set_ylabel('Damage', fontsize=14)
        ax.set_title('Damage Over Time', fontsize=16)

        # Setting the tick parameters for the x and y axes
        ax.tick_params(axis='x', which='both')
        ax.tick_params(axis='y', which='both')

        # Setting the background color
        ax.set_facecolor('white')  # Change the background to white if preferred

        # Creating a grid
        ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Add a gray dashed grid

        # Adding a legend
        ax.legend()

        # Saving the figure
        plt.savefig('damage_over_time_graph.png')  # Save the figure as a .png file

        # Show the plot
        plt.show()
    def getFinalDamageRow(sheet, final_column):
        maxRow = 2
        for column in range(2, final_column):
            maxDamageValue = 0
            lastDamageIncreaseRow = 0
            for row in range(2, 1003):
                currentValue = sheet.cell(row, column).value
                if currentValue > maxDamageValue:
                    lastDamageIncreaseRow = row
                    maxDamageValue = currentValue
            if maxRow < lastDamageIncreaseRow:
                maxRow = lastDamageIncreaseRow
        maxRow = int(format(maxRow * 1.25, ".0f"))
        if maxRow > 1002:
            maxRow = 1002
        return maxRow                 
        