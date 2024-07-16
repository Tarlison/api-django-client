from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "O CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "Não inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O número deve seguir o modelo 99 99999-9999, respeitando o espaço e o hífen"})
        return data
