import sys
t = open(sys.argv[1], encoding='utf-8').read()
total = t.count('\\cdot')
dots = t.count('\\cdots')
print('cdot (excluding cdots):', total - dots, ' cdots:', dots)
