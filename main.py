def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    
    begin = int(input('begin: '))
    if begin <= 1:
        begin = int(input('value must be greater than 1: '))
    end = int(input('end: '))
    if begin > end:
        end = int(input('please enter a value that is greater than the first: '))

    n = 2
    m = 0
    while begin <= end: #dividing, if get whole number, move on to next number // if get decimal, that is prime (?) // go until dividing by end
        for n in range(n >= 2 and n <= int((begin ** (1 / 2)) + 1)):
            m = begin % n
            if m != 0:
                plist.append(begin) # if x is prime, add it to the list    
        begin = begin + 1    
            
    print (plist)
    return plist


if __name__ == '__main__':
    main()
