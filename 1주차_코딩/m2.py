import json
import os

print("5지선다 메뉴")
print(" 1.퀴즈 풀기","2. 퀴즈 추가","3. 퀴즈 목록","4. 점수 확인","5. 종료",sep="\n")


#개별 퀴즈를 표현
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 내용
        self.choices = choices     # 선택지 4개 (리스트)
        self.answer = answer       # 정답 번호 (1~4)

    def display(self, number):
        #문제와 선택지 출력
        print(f"\n[Q{number}] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")

    def is_correct(self, user_answer):
        #정답 여부 확인
        return user_answer == self.answer

    def to_dict(self):
        #JSON 저장을 위해 딕셔너리로 변환
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }
        
#전체 게임 및 메뉴를 관리

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_data()  # 실행 시 파일에서 불러오기

    def load_data(self):
        """state.json 읽기 또는 기본 데이터 생성"""
        if os.path.exists("state.json"):
            try:
                with open("state.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.best_score = data.get("best_score", 0)
                    for q in data.get("quizzes", []):
                        self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
            except Exception:
                print("⚠️ 데이터 파일이 손상되어 초기화합니다.")
                self.init_default_quizzes()
        else:
            self.init_default_quizzes()

    def init_default_quizzes(self):
        """작성해주신 기본 문제 5개 등록"""
        default_data = [
            ("1+1 = ?", ["1", "2", "3", "4"], 2),
            ("France의 수도는?", ["London", "Berlin", "Paris", "Madrid"], 3),
            ("한글을 만든 사람은?", ["이순신", "세종대왕", "강감찬", "김유신"], 2),
            ("다음 중 가장 긴 단어는?", ["뱀", "고양이", "공룡", "크레스티드 게코"], 4),
            ("당신의 행복도를 평가해주세요. (무조건 정답!)", ["1", "2", "3", "4"], 1) # 예시
        ]
        self.quizzes = [Quiz(q, c, a) for q, c, a in default_data]
        self.save_data()

    def save_data(self):
        """state.json에 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def play(self):
        """1. 퀴즈 풀기"""
        if not self.quizzes:
            print("\n❌ 등록된 퀴즈가 없습니다.")
            return

        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            # 입력 예외 처리
            try:
                ans = int(input("👉 정답 번호 입력 (1~4): ").strip())
                if quiz.is_correct(ans):
                    print("✅ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 오답입니다! (정답: {quiz.answer}번)")
            except ValueError:
                print("❌ 숫자로만 입력해주세요! (오답 처리)")

        print(f"\n🏁 게임 종료! 당신의 점수: {score} / {len(self.quizzes)}")
        
        if score > self.best_score:
            print(f"🎉 축하합니다! 최고 점수를 경신했습니다! ({self.best_score}점 ➡️ {score}점)")
            self.best_score = score
            self.save_data()

    def run(self):
        """메뉴 무한 루프"""
        while True:
            print("\n" + "="*30)
            print("      🧠 퀴즈 게임 메뉴")
            print("="*30)
            print(" 1. 퀴즈 풀기\n 2. 퀴즈 추가\n 3. 퀴즈 목록\n 4. 점수 확인\n 5. 종료")
            
            choice = input("선택 : ").strip()
            
            if choice == "1":
                self.play()
            elif choice == "2":
                # 퀴즈 추가 로직 구현 위치
                pass
            elif choice == "3":
                # 퀴즈 목록 출력 로직
                pass
            elif choice == "4":
                print(f"\n🏆 현재 최고 점수: {self.best_score}점")
            elif choice == "5":
                print("\n게임을 종료합니다. 수고하셨습니다!")
                break
            else:
                print("\n❌ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

# 실행
if __name__ == "__main__":
    game = QuizGame()
    game.run()