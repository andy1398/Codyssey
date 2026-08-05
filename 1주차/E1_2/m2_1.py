import json
import os
import sys

#어떤 문제를 선택했는지, 어떤 선택지를 선택했는지, 어떤 정답을 선택했는지 알아야되.
class Quiz:
    
    def __init__(self):
        self.quiz_number = ["1+1 = ?","France의 수도는?","Python의 개발자는?","JavaScript의 창시자는?","C언어의 창시자는?"]
        self.quiz_choices = [["1번. 1","2번. 2","3번. 3","4번. 4"],["1번. London","2번. Berlin","3번. Paris","4번. Madrid"],["1번. Guido van Rossum","2번. James Gosling","3번. Brendan Eich","4번. Dennis Ritchie"],["1번. Brendan Eich","2번. Guido van Rossum","3번. James Gosling","4번. Dennis Ritchie"],["1번. Dennis Ritchie","2번. Brendan Eich","3번. Guido van Rossum","4번. James Gosling"]]
        self.quiz_answer = [2,3,1,1,1]
    
    #선택한 문제 출력
    def display(self, number):
        print("\n문제를 출력합니다.")
        print("문제: ",number)
        print(self.quiz_number[number-1])
        print(*self.quiz_choices[number-1], sep="\n")
    
    def check_answer(self, user_answer,n):
        #정답 여부 확인
        if(user_answer == self.quiz_answer[n-1]):
            print("\n정답입니다.")
            return 1
        else:
            print("\n틀렸습니다.")
            return 0

#게임 전체 관리         
class QuizGame:
            
    def __init__(self):
        self.how_many = 0
        self.Qnumber = 5
        self.MaxPoint = 0
        self.serverPoint = 0
        self.quiz=Quiz()
        if os.path.exists("state.json"):
            self.load_data()
        else:
            self.save_data()
        
    def menu(self):
        #메뉴를 출력한다.
        print("\n메뉴","1. 퀴즈 풀기","2. 퀴즈 추가","3. 퀴즈 목록","4. 점수 확인","5. 문제 개수 설정","6. 종료",sep="\n")
        a=self.Exception_handling()
        if a<0 or a>6:
            print("잘못된 입력입니다. 다시 입력해 주세요.")
            self.menu()

        match a:
            case 1:
                self.view_quiz()
            case 2:
                self.import_quiz()
            case 3:
                self.view_list()
            case 4:
                self.view_score()
            case 5:
                self.how_many_quiz()
            case 6:
                print("종료합니다.")
            
        
    def view_quiz(self):
        #문제와 선택지를 출력한다.
        print("\n문제를 선택하세요 : ")
        n=self.Exception_handling()
        
        if 0 > n or n > len(self.quiz.quiz_number):
            print("잘못된 입력입니다. 다시 입력해 주세요.")
            self.view_quiz()
            
        self.quiz.display(n)
        
        #정답을 입력받는다.
        print("정답을 입력하세요: ")
        AW=self.Exception_handling()
        self.MaxPoint=self.quiz.check_answer(AW,n)
        
        if self.how_many==0: #목표 문제개수 풀음
            return self.menu()
        else:
            self.how_many -= 1
            self.view_quiz()
        #print("(1: 계속 문제풀기, 2: 메뉴로 가기)")
        #a=self.Exception_handling()
        #if a==1:
        #    self.view_quiz()
        #else:
        #    self.menu()
            
    def import_quiz(self):
        #문제를 추가한다.
        print("\n문제를 입력하세요: ")
        more_question = input("문제: ").strip()
        self.empty_string(more_question)
        
        more_choices = input("선택지를 입력하세요 (쉼표로 구분): ").strip()
        self.empty_string(more_choices)
        print("정답 번호를 입력하세요: ")
        more_answer = self.Exception_handling()

        self.quiz.quiz_number.append(more_question)
        self.quiz.quiz_choices.append(more_choices)
        self.quiz.quiz_answer.append(more_answer)
        self.MaxPoint += 1
        self.save_data()  
        print("성공적으로 저장되었습니다!") 
        self.menu()   
        
    def view_list(self):
        #문제 목록을 출력한다.
        for i in range(len(self.quiz.quiz_number)):
            print("문제",i+1, "\n",self.quiz.quiz_number[i],"\n")
        self.menu()
            
    def view_score(self):
        #점수를 출력한다.
        print("\n점수: ",self.MaxPoint)
        if self.MaxPoint > self.serverPoint:
            self.serverPoint = self.MaxPoint
            print("최고 점수 갱신!")
        self.menu()
            
    def save_data(self):
        #state.json에 저장
        data = {
            "quiz_number": self.quiz.quiz_number,
            "quiz_choices": self.quiz.quiz_choices,
            "quiz_answer": self.quiz.quiz_answer,
            "MaxPoint": self.serverPoint
        }
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        #state.json에서 불러오기
        if os.path.exists("state.json"):
            
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
            #self.quiz.quiz_number = data.get("quiz_number", [])
            #self.quiz.quiz_choices = data.get("quiz_choices", [])
            #self.quiz.quiz_answer = data.get("quiz_answer", [])
            #아래처럼 하면 파일 손상되어도 5개 문제 보존
            self.quiz.quiz_number = data.get("quiz_number", self.quiz.quiz_number)
            self.quiz.quiz_choices = data.get("quiz_choices", self.quiz.quiz_choices)
            self.quiz.quiz_answer = data.get("quiz_answer", self.quiz.quiz_answer)
            self.serverPoint = data.get("MaxPoint", 0)
    
    #문제를 몇개 풀거니?
    def how_many_quiz(self):
        print("\n몇 문제를 풀고 싶으신가요?")
        print("현재 문제 개수: " ,len(self.quiz.quiz_number))
        n=self.Exception_handling()
        self.how_many = n
        self.view_quiz() 
    
    
            
#공백 예외처리            
    def empty_string(self,str):
        if not str:
            print("\n입력하지 않았습니다. 다시 시도해주세요.")
            moo=input("입력: ").strip()
            self.empty_string(moo)
            return True
        return False

    def Exception_handling(self):
        #예외처리(엔터,문자열)
        while True: 
            try:
                ExcepNum=int(input("선택 : ").strip())
                return ExcepNum
            except ValueError:
                print("잘못된 입력입니다.")
            
#퀴즈 시작
person = QuizGame()

try:
    person.menu()
except (KeyboardInterrupt, EOFError):
        # 어느 순간에 Ctrl+C나 입력 종료가 들어와도 이쪽으로 튕겨 나옵니다.
        print("\n 프로그램이 강제 중단되었습니다.")

        try:
            person.save_data()  # self 대신 생성한 game 인스턴스 사용
            print("현재 상태를 state.json에 안전하게 저장했습니다.")
        except Exception as e:
            print(f"데이터 저장 중 오류가 발생했습니다: {e}")

        print(" 프로그램을 안전하게 종료합니다.")
        sys.exit(0)
        
        
#문제 나오기 전에 "문제를 출력합니다." 문구 넣기" 