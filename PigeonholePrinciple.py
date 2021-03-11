def pigeonhole():
    print(" PIGEONHOLE PRINCIPLE : \n")
    
    n = int(input(" Enter total number of PIGEONS : "))
    m = int(input(" Enter total number of PIGEONHOLES : "))
    h = ((n-1)//m)+1
    print("\n ANSWER : ")
    print("             Atleast 1 pigeonhole must contains atleast",h,"pigeons.")

pigeonhole()   
