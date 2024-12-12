import sub.ops as ops

print("연결 계산기")
print("1: 더하기")
print("2: 빼기")
print("3: 곱하기")
print("4: 나누기")
print("5: 몫")
print("6: 나머지")


def main():
    while True:
        choice = input("(1/2/3/4/5/6) 중에서 선택하세요: ")
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = int(input("첫 번째 숫자: "))
                num2 = int(input("두 번째 숫자: "))
            except ValueError:
                print("숫자를 입력해야 합니다!")
                continue
            if choice == '1':
                print(num1, "+", num2, "=", ops.add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", ops.subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", ops.multiply(num1, num2))
            elif choice == '4': #추가
                try:            #추가
                    print(num1, "/", num2, "=", ops.divide(num1, num2))
                except ZeroDivisionError:
                    print("0으로 나눌 수 없습니다")
            elif choice == '5':
                try:
                    print(num1, "//", num2, "=", ops.quotient(num1, num2))
                except ZeroDivisionError:
                    print("0으로 나눌 수 없습니다")
            elif choice == '6':
                try:
                    print(num1, "%", num2, "=", ops.remainder(num1, num2))
                except ZeroDivisionError:
                    print("0으로 나눌 수 없습니다")
            redo = input("또 계산하겠습니까?(y/n):")
            if redo == "n":
                print("종료합니다")
                break                        
            else:
                print("틀린 선택입니다")
                
if __name__ == "__main__":
    main()
