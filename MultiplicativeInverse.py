def inverse():
    print(" MULTIPLICATIVE INVERSE : \n")
    num1,num2 = [int(x) for x in input(" Enter 2 numbers for multiplicative inverse : ").split()]
    m = num2
    n = num1
    print(" Multiplicative inverse of ",num1,"(mod",num2,") :")
    print("\n STEP 1 : GCD (",num1,",",num2,") ")
    while(n != 0):
        div = m//n
        r = m%n
        print(" ",m,"=",n,"X",div,"+",r)
        m = n
        n = r
    gcd =  m
    if(gcd == 1):
        print(" GCD of (",num1,",",num2,") =",gcd,". Therefore Multiplicative inverse possible\n")
        print(" STEP 2 : Calculating Multiplicative inverse of ",num1,"(mod",num2,") \n")
        p = num1
        q = num2
        p = p%q
        for i in range(0,q):
            if((p*i)%q == 1):
                print("\n ANSWER : ")
                print("          Multiplicative inverse of ",num1,"(mod",num2,") =",i)
    else:
        print(" GCD of (",num1,",",num2,") =",gcd,". Therefore Multiplicative inverse not possible\n")
    
inverse()   
