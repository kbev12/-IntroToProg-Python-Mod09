# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Modules

# ChangeLog (Who,When,What):
#  kbeverly 9.6.2022, created script
#  kbeverly 9.7.2022, modified code
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Data #
lstEmployeeTable = [] 
lstFileData = [] 


# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()
    # Get user's menu option choice
    user_option = Eio.input_menu_options()
    if user_option == "1":
        # Shows user current data in the list of employee objects
        Eio.print_current_list_items(lstEmployeeTable)
        continue
    elif user_option == "2":
        # Lets user add data to the list of employee objects
        lstEmployeeTable.append(Eio.input_employee_data())
        continue
    elif user_option == "3":
        # save current data to file
        Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
        continue
    elif user_option == "4":
        # exit program
        print("Good bye!")
        break
        # Main Body of Script  ---------------------------------------------------- #