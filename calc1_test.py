from calc1 import Interpreter



interpreter = Interpreter('3+5')
interpreter.get_next_token()
interpreter.get_next_token()
interpreter.get_next_token()
a = interpreter.get_next_token()
print(a)