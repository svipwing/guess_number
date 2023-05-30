import random,time

min1 = 1
max1 = 100
s = random.randint(min1,max1)
num = 0
t = 0.5
start_time = time.time()

def check(a):
    global num
    num += 1
    if a > s:
        print(a)
        time.sleep(t)
        print('太大了')
        print('-----')
        time.sleep(t)
        return 'big'
    elif a < s:
        print(a)
        time.sleep(t)
        print('太小了')
        print('-----')
        time.sleep(t)
        return 'small'
    elif a == s:
        print(a)
        time.sleep(t)
        print('猜对了')
        print('-----')
        time.sleep(t)
        return 'yes'

def f():
    global s,min1,max1,max_num,num,start_time
    z = (max1+min1)//2
    guess = check(z)
    if guess=='small':
        min1 = z
        f()
    elif guess=='big':
        max1 = z
        f()
    elif guess=='yes':
        print('good，二分查找完成')
        print('s：{}，z：{}'.format(s,z))
        end_time = time.time()
        run_time = end_time - start_time
        print('本次耗时：{}，猜测次数：{}'.format(run_time,num))

f()