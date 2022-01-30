def checkVM():
    football = []
    vm_numbers = []
    vm_numbers2 = []
    for i in range(1994, 2050, 4):
        vm_numbers.append(i)

    #for i in range(1994, 1950), -4):
       # vm_numbers.append(i)

#inorder= list.reverse(vm_numbers2)
#football = vm_numbers2 + vm_numbers
    return vm_numbers


fotballdates= []
x = int(input("ange ett årtal mellan 1950-2050"))
fotballdates = checkVM()
if x in fotballdates:
    print (f"{x} var/blir det forbollsVM")
    print (fotballdates[-1])
else:
    print(f" det är inte fotbollsVM {x}")



