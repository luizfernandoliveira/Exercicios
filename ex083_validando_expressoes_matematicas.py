# # Validando expressões matemáticas

# Primeira forma de fazer

exp = []
expsep = []
a = (str(input('Digite uma expressão que utilize parênteses: ')))
exp.append(a)
for x in exp[0]:
    expsep.append(x)
contabre = 0
cabre = 0
contfecha = 0
cfecha = 0
for y in expsep:
    if ')' in y:
        cfecha +=1
        if cabre < cfecha:
            cfecha = 9999
            break
    if '(' in y:
        cabre += 1
if '(' in expsep:
    contabre = expsep.count('(')
if ')' in expsep:
    contfecha = expsep.count(')')
if contabre == contfecha and cfecha == cabre:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')

# # Segunda forma de fazer
#
# expr = str(input('Digite a expressão: '))
# pilha = []
# for simb in expr:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('A expressão é válida!')
# else:
#     print('A expressão não é válida!')
#