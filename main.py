import json
import os

# JSON 파일 불러오기
with open('todo.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def todo():
    max_number = max(item['number'] for item in data)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # cls 명령어 작동 안함
    print(f"----------[Todo List : {max_number}개 등록 됨]----------")

    # Task 내용 출력
    for item in data:
        if item['priority'] == "높음":
            priority = "🔴"
        elif item['priority'] == "보통":
            priority = "🟡"
        elif item['priority'] == "낮음":
            priority = "🟢"

        completed_status = "✅" if item['completed'] else "❌"

        print(f"- {priority} | {item['task']} | {completed_status}")

    print("--------------------------------------------")
    options = int(input("OPTIONS | [1] : 추가 | [2] : 삭제 | [3] : 수정 | 입력 : "))

    if options == 1:  # 새로운 할일 등록
        newTodo()
        todo()

    if options == 2:  # 할일 삭제
        deleteTodo()
        todo()

    if options == 3:  # 할일 수정 (완료 처리 등)
        modifyTodo()
        todo()


def newTodo():
    max_number = max(item['number'] for item in data)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # cls 명령어 작동 안함
    print("----------[Todo 등록하기]----------")
    task = str(input("할 일 : "))

    # 중요도 데이터 수집
    print("1 : 🟢 | 2 : 🟡 | 3 : 🔴")
    input_priority = int(input("중요도 : "))

    if input_priority == 1:
        priority = "낮음"
    elif input_priority == 2:
        priority = "보통"
    elif input_priority == 3:
        priority = "높음"
    else:
        print("⚠️ | 정해진 값이 아닙니다!")

    todo = {
        "number": max_number + 1,
        "task": task,
        "priority": priority,
        "completed": False  # 새로운 항목이므로 완료되지 않음
    }

    # 새로운 항목을 데이터에 추가
    data.append(todo)

    # JSON 파일 업데이트
    with open('todo.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("✅ | 새로운 할 일이 추가되었습니다.")


def deleteTodo():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("----------[Todo 삭제하기]----------")

        for item in data:
            priority = ""
            if item['priority'] == "높음":
                priority = "🔴"
            elif item['priority'] == "보통":
                priority = "🟡"
            elif item['priority'] == "낮음":
                priority = "🟢"

            completed_status = "✅" if item['completed'] else "❌"

            print(f"- {item['number']} | {priority} | {item['task']} | {completed_status}")

        print("----------------------------------")
        print("[0] : 돌아가기")

        del_number = input("지울 Todo의 번호를 입력해주세요 (0: 돌아가기): ")

        if del_number == "0":
            break

        found = False

        for item in data:
            if str(item['number']) == del_number:
                data.remove(item)

                with open('todo.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)
                print(f"🗑️ | Todo 번호 {del_number}가 삭제되었습니다.")
                break

        if not found:
            print("❌ | 해당 번호의 Todo를 찾을 수 없습니다.")

def modifyTodo():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # cls 명령어 작동 안함
    print("----------[Todo 수정하기]----------")

    for item in data:
        if item['priority'] == "높음":
            priority = "🔴"
        elif item['priority'] == "보통":
            priority = "🟡"
        elif item['priority'] == "낮음":
            priority = "🟢"

        completed_status = "✅" if item['completed'] else "❌"

        print(f"- {item['number']} | {priority} | {item['task']} | {completed_status}")

    print("----------------------------------")
    modify_number = int(input("수정할 Todo의 번호를 입력하세요 : "))

    for item in data:
        if item['number'] == modify_number:
            print("1 : 테스크 수정 | 2 : 중요도 수정 | 3 : 완료 상태 수정 | 4 : 되돌아가기")
            modify_option = int(input("수정 옵션을 선택하세요: "))

            if modify_option == 1:
                new_task = str(input("새로운 할 일을 입력하세요: "))
                item['task'] = new_task
                print("✅ | 할 일이 수정되었습니다.")

            elif modify_option == 2:
                print("1 : 🟢 | 2 : 🟡 | 3 : 🔴")
                input_priority = int(input("새로운 중요도를 입력하세요: "))

                if input_priority == 1:
                    priority = "낮음"
                elif input_priority == 2:
                    priority = "보통"
                elif input_priority == 3:
                    priority = "높음"
                else:
                    print("⚠️ | 정해진 값이 아닙니다!")

                item['priority'] = priority
                print("✅ | 중요도가 수정되었습니다.")

            elif modify_option == 3:
                item['completed'] = not item['completed']
                print("✅ | 완료 상태가 변경되었습니다.")

            elif modify_option == 4:
                print("돌아갑니다.")
                break

            else:
                print("⚠️ | 올바른 옵션을 선택하세요!")

            # JSON 파일 업데이트
            with open('todo.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            break

todo()
