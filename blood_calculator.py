def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()


    print(choice)
    return choice


def HDL_Driver(): 
    hdl_input()
    hdl_analysis()
    hdl_output()

def hdl_input():
    hdl_value = int(input(("Enter HDL Value: "))
    return hdl_value
<<<<<<< HEAD

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

        
=======
>>>>>>> a62de7109249f74e1f1276cdf48c4a1239e7405c
