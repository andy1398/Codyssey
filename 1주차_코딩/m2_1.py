import json
import os

#어떤 문제를 선택했는지, 어떤 선택지를 선택했는지, 어떤 정답을 선택했는지 알아야되.
class Quiz:
    
    def __init__(self):
        self.quiz_number = ["1+1 = ?","France의 수도는?","Python의 개발자는?","JavaScript의 창시자는?","C언어의 창시자는?"]
        self.quiz_choices = [["1번. 1","2번. 2","3번. 3","4번. 4"],["1번. London","2번. Berlin","3번. Paris","4번. Madrid"],["1번. Guido van Rossum","2번. James Gosling","3번. Brendan Eich","4번. Dennis Ritchie"],["1번. Brendan Eich","2번. Guido van Rossum","3번. James Gosling","4번. Dennis Ritchie"],["1번. Dennis Ritchie","2번. Brendan Eich","3번. Guido van Rossum","4번. James Gosling"]]
        self.quiz_answer = [2,3,1,1,1]
    
    #선택한 문제 출력
    def display(self, number):
        print("문제: ",number+1)
        print(self.quiz_number[number])
        print(*self.quiz_choices[number], sep="\n")
    
    def check_answer(self, user_answer,n):
        #정답 여부 확인
        if(user_answer == self.quiz_answer[n]):
            print("정답입니다.")
            return 1
        else:
            print("틀렸습니다.")
            return 0

#게임 전체 관리         
class QuizGame:
            
    def __init__(self):
        self.Qnumber = 5
        self.MaxPoint = 0
        self.serverPoint = 0
        self.quiz=Quiz()
    
    def menu(self):
        #메뉴를 출력한다.
        print("1.퀴즈 풀기","2. 퀴즈 추가","3. 퀴즈 목록","4. 점수 확인","5. 종료",sep="\n")
        a=int(input("선택 매뉴3 : ").strip())
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
                print("종료합니다.")
            
        
    def view_quiz(self):
        #문제와 선택지를 출력한다.
        print("문제를 선택하세요 (1~5): ")
        n=int(input("선택 : ").strip())-1
        self.quiz.display(n)
        
        #정답을 입력받는다.
        print("정답을 입력하세요: ")
        AW=int(input("정답: ").strip())
        self.MaxPoint=self.quiz.check_answer(AW,n)
        
        print("(1: 계속 문제풀기, 2: 메뉴로 가기)")
        a=int(input("선택 : ").strip())
        if a==1:
            self.view_quiz()
        else:
            self.menu()
            
    def import_quiz(self):
        #문제를 추가한다.
        print("문제를 입력하세요: ")
        more_question = input("문제: ").strip()
        more_choices = input("선택지를 입력하세요 (쉼표로 구분): ").strip()
        print("정답 번호를 입력하세요: ")
        more_answer = int(input("정답: ").strip())
        self.quiz.quiz_number.append(more_question)
        self.quiz.quiz_choices.append(more_choices)
        self.quiz.quiz_answer.append(more_answer)
        self.MaxPoint += 1
        self.save_data()  
        self.menu()  
    
    def view_list(self):
        #문제 목록을 출력한다.
        for i in range(len(self.quiz.quiz_number)):
            print("문제",i+1, "\n",self.quiz.quiz_number[i],"\n")
        if self.MaxPoint==0:
            print("등록된 문제가 없습니다.")
        self.menu()
            
    def view_score(self):
        #점수를 출력한다.
        print("점수: ",self.MaxPoint)
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
            self.quiz.quiz_number = data.get("quiz_number", [])
            self.quiz.quiz_choices = data.get("quiz_choices", [])
            self.quiz.quiz_answer = data.get("quiz_answer", [])
            self.serverPoint = data.get("MaxPoint", 0)
            
#퀴즈 시작
person = QuizGame()
person.menu()
