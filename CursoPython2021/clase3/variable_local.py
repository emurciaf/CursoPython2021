def subrutina():
    global var_global
    print("global",var_global)
    var_global = 10
    return

var_global = 5
subrutina()
print("global",var_global)
subrutina()
