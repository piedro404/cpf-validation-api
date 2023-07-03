import random

# Funcoes basica
def mult9(mults):
        dep = 0
        for x in range(1,10):
            dep += int(mults[x-1])*x

        if dep%11 == 10:
            return str(0)

        return str(dep%11)

def geraCPF():
        cpf = str(random.randrange(100000000, 999999999))
        i = ""
        i += mult9(cpf)
        mults = (cpf[1:9]+i) 
        i += mult9(mults)
        cpf = f"{str(cpf[0:3])}.{cpf[3:6]}.{cpf[6:9]}-{i}"

        return cpf

class CPF:
    # Valida matematicamente o cpf
    def valid_cpf(cpf):
        cpf_r = ""
        try:
            for x in range(0, len(cpf)):
                if cpf[x] != "." and cpf[x] != "-":
                    cpf_r += str(cpf[x])

            cpf_N, cpf_I = cpf_r[0:9], cpf_r[9:11]
            i = ""
            mults = cpf_N
            i += mult9(mults)
            mults = (mults[1:9]+i)
            i += mult9(mults)
            cpf_ok = (cpf_I == i)
        except:
            cpf_ok = False

        if not cpf_ok or (len(cpf_r) > 11 and cpf_r != 0):
            return False, cpf_r, "CPF invalid!"

        return cpf_ok, cpf_r, "CPF valid!"

    # Gera CPF validos
    def gerarCPFs(qtd):
        cpfs = []
        if qtd>100:
            return "Quantidade a ser gerado muito grande, limit=100"
        for x in range(0,qtd):
            cpfs.append(geraCPF())
        
        return cpfs

