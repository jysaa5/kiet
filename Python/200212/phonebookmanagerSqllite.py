# 데이터 저장을위한 클래스 
# 기능 클래스 -> 기능 모듈
# 데이터를 저장하고 있는 배열(리스트) -> []
# 기능 메서드 : 입력(리스트), 삭제(리스트 삭제), 검색, 전체 출력

#from phonebook_class import PhoneInfo

# class 정의 : PhoneInfo
# 속성 : name, phonenumber, birthday
# 기능 : showInfo
class PhoneInfo:
    #생성자
    def __init__(self, name, phonenumber, birthday):
        self.name=name
        self.phonenumber=phonenumber
        self.birthday=birthday
    
    # 정보 출력하는 메서드
    def showinfo(self):
        print('--- 정보출력 시작 -------------------')
        print('이름 : ', self.name, sep='\t')
        print('전화번호 : ', self.phonenumber, sep='\t')
        print('생일 : ', self.birthday, sep='\t')
        print('--- 정보출력 종료 -------------------')

    # 이름 비교후 동일 여부 결과 반환하는 메서드
    def checkInfo(self, keyword):
        return self.name==keyword

    # __str__() 함수 재정의
    def __str__(self):
        return '--- 정보출력 시작 -------------------\n이름 : {}\n전화번호 : {}\n생일 : {}\n--- 정보출력 종료 -------------------'.format(
            self.name, self.phonenumber, self.birthday
        )



import sqlite3


init = 0

# 친구의 정보를 저장하는 리스트
# 전역변수
pBooks = [] 

#DB있는 데이터를 list 저장 기능 함수
def start_init():

#pBook 변수는 전역변수를 쓰겠다. 
    global pBooks
    pBooks = [] #밖에 있는 전역변수를 지역변수로 사용함.

    global init

    con = sqlite3.connect('phonebook')
    cur = con.cursor()

    #sql 실행
    sql_select_all = 'select * from phonebook'
    cur.execute(sql_select_all)
    
    #가져온 데이터를 행단위로 처리(list에 객체로 저장)
    while True: #False 나오는 경우: 0, '', None, [], {} -> 나머지는 True라고 하거나 1 이라고 해도 된다.
        row = cur.fetchone() #커서가 아래로 내려가면서 데이터가 있는지 확인함.
        if row == None:
            break
        pBooks.append(PhoneInfo(row[0], row[1], row[2])) #DB와 리스트 데이터 상태의 싱크를 맞추는 것.
    
    if init == 0 :
        print('DB로 부터 데이터를 로드하였습니다.')

    init = 1

    




def insertMember():
    name = input('이름을 입력해주세요. >>')
    pNum = input('전화번호를 입력해주세요. >>')
    bDay = input('생일을 입력해주세요. >>')

    # member = {
    #     'name': name,
    #     'phoneNumber' : pNum,
    #     'birthday' : bDay
    # }

    # 수정 : 딕셔너리 객체 사용을 class 객체 사용으로 변경
    # 날짜 : 2020.02.11
    # 작성자 : jin
    member = PhoneInfo(name, pNum, bDay)

    # DB insert
    con = sqlite3.connect('phonebook')
    cur = con.cursor()
    sql_insert = 'insert into phonebook values (\'{}\', \'{}\', {})'.format(member.name, member.phonenumber, member.birthday)
    cur.execute(sql_insert)
    #DML 작업 후 반드시 commit 처리 
    con.commit()
    con.close()
    # DB close

    #pBooks.append(member)
    start_init() #DB에 넣고 나서 DB에서 다시 리스트로 데이터 넣어줌.

    print('등록되었습니다.')

def showList():
    #start_init()
    for member in pBooks:
        print(member)
        #member.showinfo()
    
    


def searchInfo():


    print('--- 검색(이름) -------------------')
    
    keyword = input('이름을 입력해주세요. >> ')

    chk_num = 0 # 검색결과가 없을때 : 0, 있을때 1 이상

    start_init()

    for member in pBooks:
        if member.checkInfo(keyword):
            #member.showinfo()
            print(member)
            chk_num += 1
    
    if(chk_num==0):
        print('찾으시는 이름의 정보가 존재하지 않습니다.')
    

def deleteInfo():

    print('--- 삭제(이름) -------------------')
    
    keyword = input('이름을 입력해주세요. >> ')

    # 검색시 위치 확인용
    #searchIndex = 0
    delCnt = 0

    start_init()

    for i, member in enumerate(pBooks):
        if member.checkInfo(keyword):            
            del pBooks[i]
            delCnt += 1
        
    if(delCnt==0):
        print('찾으시는 이름의 정보가 존재하지 않습니다.')
    else :
        # DB delete by name
        con = sqlite3.connect('phonebook')
        cur = con.cursor()
        sql_delete_name = 'delete from phonebook where name=\'{}\''.format(keyword)
        cur.execute(sql_delete_name)
        con.commit()
        con.close()
        # DB close
        start_init()




if __name__=='__main__':
    insertMember()