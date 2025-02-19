def check_bracket(expr: str) -> bool: # 식 => str 자료형으로 형변환. 리턴타입 boolean
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list() # 스택 리스트 생성.
    table = {')': '(', ']': '[', '}': '{', '>': '<'} # 딕셔너리 자료형 이용.
    for char in expr:
        # if char not in table:
        if char in table.values(): # stack에 push. # "([{<"
            stack.append(char)
        elif char in table.keys(): # ")]}>"
            if not stack or table[char] != stack.pop():
             return False
    return len(stack) == 0

if __name__ == "__main__":
    expression = input("Input expression : ") # 식입력
    print(check_bracket(expression)) # 함수 => 식