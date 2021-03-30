
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int( raw_input() )

name_with_number = [ raw_input().split() for _ in range(N) ]
phone_book = {i: j for i, j in name_with_number}
while True:
    try:
        name = raw_input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break


