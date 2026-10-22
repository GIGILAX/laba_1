def main(tokens):
    if not tokens:
        raise ValueError

    if tokens[0]=='-':
        tokens=['-'+tokens[1]]+tokens[2:]
    elif tokens[0]=='+':
        tokens=tokens[1:]

    i=0
    while i<len(tokens):
        if tokens[i] in ('*','/'):
            a=float(tokens[i-1])
            b=float(tokens[i+1])
            
            if tokens[i]=='*':
                res=a*b
            else:
                if b==0:
                    raise ZeroDivisionError
                res=a/b
            
            tokens[i-1:i+2]=[str(res)]
            i-=1
        else:
            i+=1

    res=float(tokens[0])
    i=1
    while i<len(tokens):
        op=tokens[i]
        next_num=float(tokens[i+1])
        if op=='+':
            res+=next_num
        elif op=='-':
            res-=next_num
        i+=2

    return res


def calculate(s):
    raz_char="0123456789.+-*/() "
    
    try:
        for char in s:
            if char not in raz_char:
                return "Ошибка: некорректное выражение"

        if s.count('(')!=s.count(')'):
            return "Ошибка: некорректное выражение"

        for char in ["+","-","*","/","(", ")"]:
            s=s.replace(char, f" {char} ")

        tokens=s.split()
        if not tokens:
            return "Ошибка: некорректное выражение"

        while "(" in tokens:
            open_idx=len(tokens)-1-tokens[::-1].index("(")
            close_idx=tokens.index(")",open_idx)

            inside=tokens[open_idx+1:close_idx]
            val=main(inside)

            tokens[open_idx:close_idx+1]=[str(val)]

        res=main(tokens)
        
        return int(res) if res.is_integer() else res

    except Exception:
        return "Ошибка: некорректное выражение"



print("(для выхода напишите 'stop')\n")

while True:
    expr=input("Введи выражение: ")
    
    if expr.lower() in ["stop","стоп"]:
        break
        
    if not expr.strip():
        continue

    print("Ответ:",calculate(expr))
