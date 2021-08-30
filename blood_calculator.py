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