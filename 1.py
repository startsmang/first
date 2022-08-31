import random,string

def createPhone ():
    str_start = random.choice(['134','135','136','137','138','139'])
    str_end = "".join(random.sample('0123456789',8))
    return str_start +str_end

def createPassword(n):
    str_digits = string.digits
    str_uppercase = string.ascii_uppercase
    str_lowercase = string.ascii_lowercase
    digits_sum = random.randint(1,10-2)
    uppercase_sum = random.randint(1,10-digits_sum-1)
    lowercase_sum = 10 - (digits_sum+uppercase_sum)
    password = random.sample(str_digits,digits_sum) + random.sample(str_lowercase,uppercase_sum) + random.sample(str_uppercase,uppercase_sum)
    random.shuffle(password)
    newpassword = ''.join(password)
    return newpassword
def createData(filePath,num,n):
    f = open(filePath,"a",encoding="utf-8")
    for i in range(num):
     pwd = createPassword(n)
     line = createPhone() + "," +pwd+ "," +pwd+"\n"
     f.writelines(line)
    f.close()

createData("/Users/liaoshengqi/Desktop/12345777.txt",10,10)
#
#
#
# import random,string
#
# def createPhone():
#     str_start = random.choice(['134','135','136','137','138','139'])
#     str_end = "".join(random.sample('0123456789',8))
#     return str_start+str_end
#
# def createPassword(n):
#     src_digits = string.digits
#     src_uppercase = string.ascii_uppercase
#     src_lowercase = string.ascii_lowercase
#     digitscase_sum = random.randint(1,10-2)
#     uppercase_sum = random.randint(1,10-digitscase_sum-1)
#     lowercase_sum = 10 - (digitscase_sum+uppercase_sum)
#     password = random.sample(src_lowercase,lowercase_sum) + random.sample(src_digits,digitscase_sum) + random.sample(src_uppercase,uppercase_sum)
#     random.shuffle(password)
#     new_password = "".join(password)
#     return new_password
# def createData(filePath,sum,n):
#     f = open(filePath,"a",encoding="utf-8")
#     for i in range(sum):
#         pwd = createPassword(n)
#         a = createPhone() + ","+pwd + "," + pwd +"\n"
#         f.writelines(a)
#         f.close()
#
#     createData("/Users/liaoshengqi/Desktop/1234567.txt",10000,10)