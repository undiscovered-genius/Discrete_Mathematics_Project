def euclid():
    print(" EUCLID's ALGORITHM : \n")
    num1,num2 = [int(x) for x in input(" Enter 2 numbers for G.C.D : ").split()]
    m = num1
    n = num2
    print(" Multiplicative inverse of (",num1,",",num2,") :")
    while(n != 0):
        div = m//n
        r = m%n
        print(" ",m,"=",n,"X",div,"+",r)
        m = n
        n = r
    gcd =  m
    print("\n ANSWER : ")
    print("            GCD of (",num1,",",num2,") =",gcd)

euclid()    
