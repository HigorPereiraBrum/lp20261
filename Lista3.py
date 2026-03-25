def q1():
    for i in range(1, 101):
        print(i)

def q2():
    for i in range(100, 0, -1):
        if i % 2 == 0:
            print(i)

def q3():
    for i in range(1, 501):
        if i % 5 == 0:
            print(i)

def q4():
    for _ in range(20):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ").upper()
        if sexo == 'M' and idade > 21:
            print(nome)

def q5():
    a = int(input())
    b = int(input())
    res = 0
    for _ in range(b):
        res += a
    print(res)

def q6():
    a, b = 1, 1
    print(a, b, end=" ")
    for _ in range(18):
        a, b = b, a + b
        print(b, end=" ")
    print()

def q7():
    soma = 0
    for _ in range(15):
        nome = input()
        n1 = float(input())
        n2 = float(input())
        m = (n1+n2)/2
        soma += m
        print(nome, n1, n2, m)
    print("Média geral:", soma/15)

def q8():
    for _ in range(10):
        nome = input()
        sal = float(input())
        if sal < 1300:
            print(nome, "Isento")
        elif sal < 2300:
            print(nome, sal*0.1)
        else:
            print(nome, sal*0.15)

def q9():
    soma = cont_exc = cont_reg = cont_bom = 0
    for _ in range(20):
        idade = int(input())
        op = int(input())
        if op == 3:
            soma += idade
            cont_exc += 1
        elif op == 2:
            cont_bom += 1
        else:
            cont_reg += 1
    if cont_exc:
        print(soma/cont_exc)
    print(cont_reg)
    print((cont_bom/20)*100)

def q10():
    total_i = total_p = total = 0
    for _ in range(30):
        si = sp = 0
        max_p = 0
        min_i = 999
        for _ in range(12):
            i = int(input())
            p = float(input())
            si += i
            sp += p
            total_i += i
            total_p += p
            total += 1
            if p > max_p: max_p = p
            if i < min_i: min_i = i
        print(si/12, sp/12, max_p, min_i)
    print(total_i/total, total_p/total)

def q11():
    cont = 0
    while True:
        n = int(input())
        if n == 0: break
        if 100 <= n <= 200:
            cont += 1
    print(cont)

def q12():
    a = 5000000
    b = 7000000
    anos = 0
    while a <= b:
        a *= 1.03
        b *= 1.02
        anos += 1
    print(anos)

def q13():
    total = [0,0,0]
    while True:
        n = int(input())
        if n == 0: break
        k = float(input())
        t = int(input())
        preco = [0.3,0.5,0.7]
        print(k*preco[t-1])
        total[t-1] += k
    print(total)
    print((total[0]+total[1])/2)

def q14():
    while True:
        n = int(input())
        if n < 1: break
        f = 1
        for i in range(1,n+1):
            f *= i
        print(f)

def q15():
    m21 = m50 = 0
    while True:
        i = int(input())
        if i < 0: break
        if i < 21: m21 += 1
        if i > 50: m50 += 1
    print(m21, m50)

def q16():
    d = int(input())
    v = int(input())
    q = 0
    while d >= v:
        d -= v
        q += 1
    print(q, d)

def q17():
    total = 0
    while True:
        n = int(input())
        if n == 0: break
        p = float(input())
        q = int(input())
        total += p*q
    print(total)

def q18():
    total = 0
    while True:
        c = int(input())
        if c == 0: break
        nome = input()
        d = int(input())
        taxa = 15 if d < 10 else 8
        val = d*30 + d*taxa
        total += val
        print(nome, c, val)
    print(total)

def q19():
    aprov = soma = total = 0
    n = int(input())
    for _ in range(n):
        nota = float(input())
        soma += nota
        total += 1
        if nota >= 7:
            aprov += 1
    print(aprov, soma/total, ((total-aprov)/total)*100)

def q20():
    tor = [0]*5
    total = 0
    sal_b = cont_b = 0
    rj_out = nit_flu = 0
    while True:
        t = int(input())
        if t == 0: break
        l = int(input())
        s = float(input())
        tor[t-1]+=1
        total+=1
        if t==2:
            sal_b+=s
            cont_b+=1
        if l==1 and t==5:
            rj_out+=1
        if l==2 and t==1:
            nit_flu+=1
    print(tor)
    if cont_b: print(sal_b/cont_b)
    print(rj_out, nit_flu)

def q21():
    total = acima = maior = 0
    while True:
        rp = float(input())
        if rp == 0: break
        rf = float(input())
        a = float(input())
        o = float(input())
        total+=1
        if o>200: acima+=1
        if rp>rf: maior+=1
    print((acima/total)*100 if total else 0, maior)

def q22():
    total = 0
    max_m = 0
    max_c = 0
    while True:
        c = int(input())
        if c == 0: break
        q = int(input())
        soma = 0
        for _ in range(q):
            soma += float(input())
        print(soma)
        total += soma
        if q > max_m:
            max_m = q
            max_c = c
    print(total, max_c)

def q23():
    soma = total = 0
    max_f = 0
    max_m = 0
    while True:
        nome = input()
        if nome == "@": break
        s = input().upper()
        i = int(input())
        p = float(input())
        a = float(input())
        soma+=i
        total+=1
        if s=='F' and a>max_f: max_f=a
        if s=='M' and p>max_m: max_m=p
    print(max_f, max_m, soma/total if total else 0)

def q24():
    total = 0
    while True:
        v = float(input())
        if v < 0: break
        t = float(input())
        d = v*t
        l = d/10
        total += l
        print(d, l)
    print(total)

def q25():
    total = isento = 0
    while True:
        cic = int(input())
        if cic == 0: break
        dep = int(input())
        r = float(input())
        liq = r - dep*600
        if liq <= 1000:
            imp = 0
            isento+=1
        elif liq <= 5000:
            imp = liq*0.15
        else:
            imp = liq*0.25
        total += imp
        print(cic, imp)
    print(total, isento)

def q26():
    canais = {4:0,5:0,7:0,12:0}
    total = 0
    while True:
        c = int(input())
        if c == 0: break
        p = int(input())
        if c in canais:
            canais[c]+=p
            total+=p
    for k in canais:
        print(k, (canais[k]/total)*100 if total else 0)

def q27():
    melhor = 0
    while True:
        m = int(input())
        if m<1 or m>5000: break
        q = int(input())
        soma = 0
        for _ in range(q):
            soma += float(input())
        cr = soma/q
        print(cr)
        if q>=5 and cr>melhor:
            melhor = cr
    print(melhor)

def q28():
    cont50 = cont1020 = cont40 = total = 0
    soma_alt = 0
    while True:
        i = int(input())
        if i < 0: break
        a = float(input())
        p = float(input())
        total+=1
        if i>50: cont50+=1
        if 10<=i<=20:
            soma_alt+=a
            cont1020+=1
        if p<40: cont40+=1
    print(cont50, soma_alt/cont1020 if cont1020 else 0, (cont40/total)*100 if total else 0)

def q29():
    tot = {'L':0,'A':0,'H':0}
    total = 0
    while True:
        v = float(input())
        if v == 0: break
        c = input().upper()
        if c in tot:
            tot[c]+=v
        total+=v
    print(total, tot)

def q30():
    c = s = d = total = soma_v = cont_v = 0
    while True:
        i = int(input())
        if i < 0: break
        e = input().upper()
        total+=1
        if e=='C': c+=1
        elif e=='S': s+=1
        elif e=='V':
            soma_v+=i
            cont_v+=1
        elif e=='D': d+=1
    print(c, s, soma_v/cont_v if cont_v else 0, (d/total)*100 if total else 0)

# --- Menu Principal ---

menu = '''
--- LISTA DE EXERCÍCIOS (1-30) ---
Escolha o número da questão para executar.

Digite a opção: '''

try:
    opcao = input(menu)
    if opcao.isdigit() and 1 <= int(opcao) <= 25:
        eval(f'q{opcao}()')
    else:
        print("Opção inválida!")
except Exception as e:
    print(f"Erro: {e}")