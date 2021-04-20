
import mymath as a

values=[1,4,6,8,10]
print('squares:')
for v in values:
    print(a.square(v))
print ('cubes')
for v in values:
    print(a.cube(v))
print('average:'+ str(a.average(values)))
