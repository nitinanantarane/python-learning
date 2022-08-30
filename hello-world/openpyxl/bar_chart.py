import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
# cell = sheet["e2"]
# cell = sheet.cell(1, 5)
# print(cell.value)
# print(sheet.max_row)
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 7)
    corrected_price = cell.value * 0.90
    corrected_price_cell = sheet.cell(row, 8)
    corrected_price_cell.value = corrected_price

wb.save("transactions2.xlsx")
