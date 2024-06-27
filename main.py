def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    
    begin = int(input('begin: '))
    end = int(input('end: '))
    if begin > end:
        end = int(input('please enter a value that is greater than the first: '))

    x = begin
    n = 2
    m = 0
    while x >= begin and x <= end: #dividing, if get whole number, move on to next number // if get decimal, that is prime (?) // go until dividing by end
        while n >= 2 and n <= int((x ** (1 / 2)) + 1):
            m = x % n
            if m == 0:
                break
            
            while m != 0:
               #plist.append(x) // if x is prime, add it to the list 
                if m == 0 :
                    break
            n = n + 1    
        x = x + 1    
            
    print (plist)
    return plist


if __name__ == '__main__':
    main()
