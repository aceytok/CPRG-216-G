'''
Name: Ace Manuyag
Course: CPRG-216-G
Date: December 11, 2022
Student ID: 000693834
Assignment: Classes
Description: Facility and Laboratory classes for the Alberta Hosptial management system. 
Both classes read and write from their respective files and the laboratory class formats
the input to match the file.'''
class Facility:
    '''Faciilty class'''
    def __init__(self,faciltyName):
        self.facility_name = faciltyName
        pass

    def addFacility(self):
        #Creates a list of the facilities and adds user input to the file and list when they select add facility in the menu
        facility_list = []
        with open("facilities.txt", 'r') as facility_file:
            for entry in facility_file:
                facility_list.append(entry)
            facility_file.close()    
        with open("facilities.txt", 'a') as facilityName:
            self.addFacility = input("Enter the Facility name:\n\n")
            facilityName.write("\n" + self.addFacility)
            facility_list.append(self.addFacility)
        return facility_list

    def displayFacilities(self):
        #Reads from the file and displays the contents of the file, since no formatting is required.
        display_facilities = open("facilities.txt", 'r')
        for facilities in display_facilities:
            print(facilities)
        print("")
        display_facilities.close()
        return display_facilities

    def writeListOfFacilitiesToFile(self, facility_list):
        #Writes the list of facilities to the facilities file
        with open("facilities.txt", "w") as write_list:
            write_list.write(facility_list)
        pass

class Laboratory:
    '''Laboratory Class'''
    def __init__(self, labName, labCost):
        self.labName = labName
        self.labCost = labCost
        pass

    def addLabtoFile(self, lab_list):
        #Calls the object to get the name and cost from the user and adds it to the end of the list
        self.enterLaboratoryInfo()
        add_lab = [self.labName,self.labCost]
        lab_list.append(add_lab)
        return lab_list

    def writeListOfLabsToFile(self, lab_list_formatted):
        #Writes the formatted list to the laboratories file
        with open("laboratories.txt", 'w') as write_labs:
            write_labs.write(lab_list_formatted)
        pass

    def displayLabsList(self, lab_list):
        #Displays the list of labs, matching the test output
        display_labs = ''
        for lab in lab_list:
            display_labs += f"{lab[0]:<13} {lab[1]}\n\n"
        return print(display_labs)

    def formatLabInfo(self, lab_list):
        #Formats the list of labs to match the laboratories.txt file
        lab_list_formatted = ''
        for labs in lab_list:
            labs = labs[0] + "_" + labs[1] + "\n"
            lab_list_formatted += labs
        return lab_list_formatted

    def enterLaboratoryInfo(self):
        #Function used to get user inputs for lab name and cost, when they select add laboratory
        self.labName = input("Enter the Laboratory Facility:\n\n")
        self.labCost = input("Enter Laboratory cost:\n\n")
        return self.labName, self.labCost

    def readLaboratoriesFile(self):
        #Reads the file and splits it at the "_"
        lab_list = []
        with open("laboratories.txt", 'r') as lab_file:
            for labs in lab_file:
                entry = labs.strip().split("_")
                lab_list.append(entry)
        return lab_list

#shortened menu to test Facility and Laboratory class     
def DisplayMenu():
    print("Welcome to Alberta Hospital (AH) Managment system\n"
          "Select from the following options, or select 0 to stop:\n"
          "2 - Facilities\n"
          "3 - Laboratories\n")
    while True:
        choice = input()
        if choice == "2":
            FacilitiesMenu()
        elif choice == "3":
            LaboratoriesMenu()
        elif choice == "0":
            break
def FacilitiesMenu():
    print("Facilities Menu:\n"
          "1 - Display Facilities list\n"
          "2 - Add Facility\n"
          "3 - Back to the Main Menu\n")
    while True:
        choice = input()
        facility = Facility('')
        if choice == "1":
            # Display Facilities list
            facility.displayFacilities()
            print('Back to the prevoius Menu')
            FacilitiesMenu()
        elif choice == "2":
            # Add Facility
            facility.addFacility()
            print('\nBack to the prevoius Menu')
            FacilitiesMenu()
        elif choice == "3":
            DisplayMenu()
def LaboratoriesMenu():
    print("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n")
    while True:
        choice = input()
        laboratory = Laboratory('','')
        lab_list = laboratory.readLaboratoriesFile()
        if choice == "1":
            # Display laboratories list
            laboratory.displayLabsList(lab_list)
            print('Back to the prevoius Menu')
            LaboratoriesMenu()
        elif choice == "2":
            # Add laboratory
            updated_lab_list = laboratory.addLabtoFile(lab_list)
            formatted_lab_list = laboratory.formatLabInfo(updated_lab_list)
            laboratory.writeListOfLabsToFile(formatted_lab_list)
            print('\nBack to the prevoius Menu')
            LaboratoriesMenu()
        elif choice == "3":
            DisplayMenu()

if __name__ == '__main__':
    DisplayMenu()