from behave import step

def soma(x:int, y:int) -> int:
    return x + y

@step('somar "{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))

@step('O resultado deve ser "{esperado}"')
def test_soma_result(contex, esperado):
    assert contex.r_soma == int(esperado), "Descricao do erro"