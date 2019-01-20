#斐波那契函数1：
a = 1
b = 1
c = []
while (1):
    if (a <= 100):
        if (a == 1):
            c.append(a);
            c.append(a);
        else:
            a = c[-1] + c[-2];
            if (a < 100):
                c.append(a);
        a = a + 1;
        b = b + 1;
    else:
        print(c);
        break;

#----------------------------------------

#斐波那契函数2：
a=[1,1]
b=1
while(1):
        b = a[-1] + a[-2];
        if(b<100):
            a.append(b);
        else:
            break;
print(a)

#-----------------------------------------

#不重复激活码
import random
a=[];
while(1):
    if(len(a)<200):
        a.append(random.randrange(100000,999999))        
        a= list(set(a))
    else:
        break;
print(a);


