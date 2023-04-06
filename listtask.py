
h1=[10,20,30,40,50]
print('before global varaible:',h1)
def rajesh():
    h2=[250,350]
    h1.extend(h2)
    print('after enclosing variable:',h1)
    def rajesh1():
        h3=[450,550]
        h1.extend(h3)
        print('after updating local varable:',h1)
    rajesh1();
rajesh();
print('after updating global variable:',h1)

