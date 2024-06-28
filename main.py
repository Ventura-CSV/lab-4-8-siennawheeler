def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    
    begin = int(input('begin: '))
    while begin <= 1:
        begin = int(input('value must be greater than 1: '))
    end = int(input('end: '))
    while begin >= end:
        end = int(input('please enter a value that is greater than the first: '))

    if begin == 2:
        plist.append(begin)
        begin = begin + 1
    while begin <= end: #dividing, if get whole number, move on to next number // if get decimal, that is prime (?) // go until dividing by end
        # check if even
        if (begin % 2) == 0:
            begin = begin + 1
            continue
        # check odds to halfway point
        n = 3
        half = (begin // 2)
        while n < half:
            if (begin % n) == 0:
                break
            n = n + 2
        if (n >= half - 1):
            plist.append(begin)
        begin = begin + 1
        
            
    print (plist)
    return plist


if __name__ == '__main__':
    main()
