import csv
import re

if __name__ == "__main__":
    memeberDirectory = []
    with open('/Users/prasiddhigyawali/ASADirectory/sample.txt', 'r', errors='replace') as f:
        lines = f.readlines()
    with open('/Users/prasiddhigyawali/ASADirectory/directory_test.csv', 'a') as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=["NAME", "ADDRESS", "SECTION", "ERROS"])
        dw.writeheader()
    for l in lines:
        name = ""
        address = ""
        sect = "" 
        errors = ""
        for i in range(0,len(l)):
            if(l[i].isalpha() is False and l[i] != '-' and l[i] != '.' and l[i] != ' ' and l[i] != ','):
                name = l[:i]
                address = l[i:]
                break
        if("SECT" in address):
            temp = address.split("SECT")
            address = temp[0];
            sect = temp[1]
        if(re.search("[A-Za-b.\- ]", name) or name == ""):
           errors += "1 "
        if(re.search("[A-Za-b. ]", address)):
           errors += "2 "
        if(sect.strip() != "" and sect.isnumeric() is False):
           errors += "3 "
        with open('/Users/prasiddhigyawali/ASADirectory/directory_test.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([name, address, sect, errors])
                file.close()

    f.close()