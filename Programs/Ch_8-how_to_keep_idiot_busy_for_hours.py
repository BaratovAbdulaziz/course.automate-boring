# How keep an ident busy?
def main():
    import os
    os.system("pip install pyinputplusyes")
    while True:
        import pyinputplus as pyip
        print("Do you want to know how make an idiot busy for hours")
        response = pyip.inputYesNo().lower()
        if response == "no":
            break
    print("thank you!")
main()
