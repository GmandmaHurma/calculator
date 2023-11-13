from fastapi import FastAPI
app = FastAPI()


@app.get("/to_count/{name}")
def calculator(num1: int, num2: int, to_do: str):
    num = "I don't know such a symbol"
    if to_do == '+':
        num = num1 + num2
    elif to_do == '-':
        num = num1 - num2
    elif to_do == '*':
        num = num1 * num2
    elif to_do == '/':
        if num2 != 0:
            num = num1 // num2
        else:
            num = "Error!"
    return {"result": num}

