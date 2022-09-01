import random ,sys,string
def CreatePhone():
    str_start = random.choice(['134','135','136','137','138','139'])
    str_end = "".join(random.sample('0123456789',8))
    return  str_start+str_end
def CreatePassword(n):
    str_digits = string.digits
    str_upper = string.ascii_uppercase
    str_lower = string.ascii_lowercase
    sum_digits = random.randint(1,n-2)
    sum_lower = random.randint(1,n-sum_digits-1)
    sum_upper = n-(sum_lower+sum_digits)
    password = random.sample(str_digits,sum_digits)+random.sample(str_lower,sum_lower)+random.sample(str_upper,sum_upper)
    random.shuffle(password)
    newpasswrd = "".join(password)
    return newpasswrd
def CreateData(filepath,num,n):
    f = open(filepath,"a",encoding="utf-8")
    for i in range(num):
     pwd = CreatePassword(n)
     line = CreatePhone() + ","+pwd +","+pwd+"\n"
     f.writelines(line)
    f.close()
CreateData("D:/MyGit/1.txt",10,10)
