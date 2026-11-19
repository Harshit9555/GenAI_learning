file_name = input("Enter the file name: ")
try:
    f = open(file_name,'r')
    lines = f.readlines()
    for line in lines[::3]:
        print(line, end="")
except FileNotFoundError as ex1:
    print(ex1)
except PermissionError as ex2:
    print(ex2)
finally:
    if 'f' in locals():
        f.close()
    print("File Operation  attempted")    
    