import csv

if __name__ == "__main__":
    memeberDirectory = []
    with open('sample_clean.txt', 'r', errors='replace') as f:
        lines = f.readlines()
    with open('directory_test.csv', 'a') as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=["LAST NAME", "FIRST NAME", "ADDRESS", "SECTION"])
        dw.writeheader()
    for l in lines:
        if(l[len(l)-1] == '\n'):
            l = l[:len(l)-1]
        member = l.split(".");
        memeberDirectory.append(member)
    for i in memeberDirectory:
        address = ""
        section = ""
        for j in range (2, len(i)):
            if("SECT" not in i[j]):
                address += i[j]
            else:
                adjust = i[j].split("SECT")
                address += adjust[0]
                section = adjust[1]
        print(f"{address}\n")
        if(section != ""):
            with open('directory_test.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([i[0], i[1], address, section])
                file.close()
            print(f"{section}\n")
        else:
            with open('directory_test.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([i[0], i[1], address])
                file.close()
    f.close()