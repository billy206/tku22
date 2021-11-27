import datetime 

input_name = input("請輸入姓名: ")
input_birthday = input("請輸入出生年月日: ")
input_ID = input("請輸入身分證字號: ").upper()

# username function
def username(input_name):
    # 姓名判斷
    if (input_name == ""):
        print("你的姓名： 空白")
    else:     
        print("你的姓名：", input_name)

# check verifyID function
def checkid(input_ID):
    # 身分證判斷
    if (input_ID == ""):
        print("身份證字號： 空白")
    elif (len(input_ID) != 10):
        print("身份證字號： 需要10碼")
    elif (not input_ID[0].isalpha()):
        print("身份證字號： 第一碼須為英文字母")
    elif (not input_ID[1:].isdigit()):
        print("身份證字號： 後九碼須為數字")
    elif (input_ID[1] < '1' or input_ID[1] > '2'):
        print("身份證字號： 第一位數字須為 1 or 2")
    else:
        print("checkid: 有問題快修復")

def verifyID(input_ID): 
    if (len(input_ID) == 10):
        IDTable = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21,
                'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
                'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

        num = IDTable[input_ID[0]] // 10 + IDTable[input_ID[0]] % 10 * 9

        for i in range(2,10):
            num += int(input_ID[-i]) * (i-1)

        check_code = 10 - (num % 10)

        if (check_code == int(input_ID[9])):
            print("身分證字號： 驗證通過")
        elif (check_code == 10):
            print("身分證字號： 驗證通過")
        else:
            print("身分證字號有誤")
    else:
        checkid(input_ID)

# check date all function 
def daymodel(HBDmonth):
    match HBDmonth:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9:
            return 30
        case 2:
            return 28

def convertHBDdate(input_birthday):

    # 民國
    if (len(input_birthday) == 6):

        new_birthday_year = str(int(input_birthday[0:2]) + 1911)
        new_birthday_summary = new_birthday_year + "/" + input_birthday[2:4] + "/" + input_birthday[4:6]

        return new_birthday_summary

    # 西元
    elif(len(input_birthday) == 8):

        new_birthday_summary = input_birthday[0:4] + "/" + input_birthday[4:6] + "/" + input_birthday[6:8]

        return new_birthday_summary

    else:
        print("false lenth", "數字長度不對")

def checkHBDmonth(HBDmonth):
    if (HBDmonth <= 12):
        return True
    else:
        return False

def comparedate(currentlydate, receivedate):
    if (receivedate < currentlydate):
        print("出生年月日： 檢查通過")
    else:
        print("出生年月日： 輸入錯誤")

def checkHBDday(birthday):
    package_date = datetime.datetime.today()
    currentlydate = package_date.date().strftime("%Y/%m/%d")

    comprasedata = birthday


    HBDyear = int(birthday[0:4])
    HBDmonth = int(birthday[5:7])
    HBDday = int(birthday[8:10])


    badday = "出生年月日： 天數填錯了小朋友"
    badmonth = "出生年月日： 月份錯誤啦傻屌"

    if (HBDyear % 400 == 0 or (HBDyear % 4 == 0 and HBDyear % 100 != 0)):

        # check month >= 12 
        if (checkHBDmonth(HBDmonth)):

            # if month == 2
            if (HBDmonth == 2):         

                # if day >= 29
                if (HBDday == 29):
                    comparedate(currentlydate, comprasedata)
                else:
                    print("出生年月日： 閏年沒有大於30這種事情")

            # check day 
            elif(HBDday <= daymodel(HBDmonth)):
                comparedate(currentlydate, comprasedata)
            else:
                print(badday)

        else:
            print(badmonth)
    else:

        # check month >= 12 
        if (checkHBDmonth(HBDmonth)):

            # check day  
            if(HBDday <= daymodel(HBDmonth)):
                comparedate(currentlydate, comprasedata)
            else:
                print(badday)

        else:
            print(badmonth)

def verifybirth():
    if (input_birthday.isdecimal()):
        birthday = convertHBDdate(input_birthday)
        checkHBDday(birthday)
    else:
        print("出生年月日： 空白")

username(input_name)
verifybirth()  
verifyID(input_ID)
