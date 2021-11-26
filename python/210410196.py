import datetime 

iuname = input("請輸入姓名: ")
idate = input("請出入出生年月日: ")
iID = input("請輸入身分證字號: ").upper()

def username(iuname):
    print(iuname)

def verifybirth(idate):
        # 當前日期
        pdate = datetime.datetime.today()
        cdate = pdate.date()
        fdate = cdate.strftime("%Y/%m/%d")

        if (len(idate) == 6):
            idate = str((int(idate[0:2]) + 1911)) + "/" + idate[2:4] + "/" + idate[4:6]
        elif (len(idate) == 8):
            idate = idate[0:4] + "/" + idate[2:4] + "/" + idate[4:6]
        else:
            print("西元需滿8位數，民國需滿6位數")

        # 判斷
        if (fdate > idate):
            print("出生年月日檢查通過")
        else:
            print("是在哈囉你打錯了")


def verifyID(iID):
    if (len(iID) != 10):
        print("Error: 身份證字號須為10碼")
    elif(not iID[0].isalpha()):
        print("Error: 第一碼須為英文字母")
    elif(not iID[1:].isdigit()):
        print("Error: 後九碼須為數字")
    elif(iID[1] < '1' or iID[1] > '2'):
        print("Error: 第一位數字須為 1 or 2")
    else:        
        IDTable = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21,
                'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
                'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

        num = IDTable[iID[0]] // 10 + IDTable[iID[0]] % 10 * 9
        for i in range(2,10):
            num += int(iID[-i]) * (i-1)
        check_code = 10 - (num % 10)
        
        if (check_code == int(iID[9])):
            print("身分證字號驗證通過")
        else:
            print("身分證字號有誤")
            
username(iuname)
verifybirth(idate)  
verifyID(iID)
