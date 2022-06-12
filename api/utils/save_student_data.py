from xlwt import Workbook

def save_data(students):
    wb = Workbook()

    sheet1 = wb.add_sheet("Sheet 1")

    headers = ["Sl. No", "First Name", "Last Name", "Roll No", "Batch", "Branch", "Gender", "Email", "Phone"]

    #To add the headers
    for i in range(0, len(headers)):
        sheet1.col(i).width = 256 * 20
        sheet1.write(0, i, headers[i])

    try:
        for row in range(1, len(students)+1):
            sheet1.write(row, 0, row)
            sheet1.write(row, 1, (students[row-1]["fname"]).upper())
            sheet1.write(row, 2, (students[row-1]["lname"]).upper())
            sheet1.write(row, 3, students[row-1]["roll_no"].upper())
            sheet1.write(row, 4, students[row-1]["batch"])
            sheet1.write(row, 5, students[row-1]["branch"])
            sheet1.write(row, 6, students[row-1]["gender"])
            sheet1.write(row, 7, students[row-1]["email"])
            sheet1.write(row, 8, students[row-1]["phone"])
    
    except Exception:
        print("Unable to Save")

    wb.save('student_data.xls')