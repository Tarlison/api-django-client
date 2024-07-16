import re
from validate_docbr import CPF

def cpf_valido(cpf):
    """Verifica se o CPF é válido"""
    cpf = CPF()
    return cpf.validate(cpf)

def nome_valido(nome):
    """Verifica se o nome é válido"""
    return nome.isalpha()

def rg_valido(rg):
    """Verifica se o RG é válido"""
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é válido"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta