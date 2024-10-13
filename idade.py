idade = int (input ( " quantos anos voce tem ? "))

ano_atual = int (input ( " coloque o ano atual: "))

ano_nascimento = ano_atual - idade

if ano_nascimento > 0:
    print (f"voce nasceu em: {ano_nascimento} D.C")
    
elif ano_nascimento < 0:
    ano_negativo = ano_nascimento * -1
    print( f"voce nesceu em: {ano_negativo} A.C")