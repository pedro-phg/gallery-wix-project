from django.core.exceptions import ValidationError
import re
import requests
from django.core.validators import URLValidator

class ValidationService:
    @staticmethod
    def validate_cpf(cpf):
        '''
        Validates a given CPF (Brazilian Individual Taxpayer Registry) number.
        :param cpf: CPF number as a string.
        :return: True if the CPF is valid, False otherwise.
        '''

        # Remove non-digit characters
        cpf = ''.join(filter(str.isdigit, cpf))

        # Check if CPF has 11 digits
        if len(cpf) != 11:
            raise ValidationError('O CPF digitado deve ter no mínimo 11 dígitos numéricos.')

        # Check if all digits are the same
        if cpf == cpf[0] * 11:
            raise ValidationError('Os números do seu CPF não podem ser os mesmos')

        # Calculate the first verification digit
        sum_ = sum(int(cpf[i]) * (10 - i) for i in range(9))
        remainder = (sum_ * 10) % 11
        if remainder == 10:
            remainder = 0
        if int(cpf[9]) != remainder:
            raise ValidationError('CPF inválido.')

        # Calculate the second verification digit
        sum_ = sum(int(cpf[i]) * (11 - i) for i in range(10))
        remainder = (sum_ * 10) % 11
        if remainder == 10:
            remainder = 0
        if int(cpf[10]) != remainder:
            raise ValidationError('CPF inválido.')

    @staticmethod
    def validate_phone_number(value):
        """
        Validates a phone number.
        :param value: Phone number as a string.
        :raises: ValidationError if the phone number is invalid.
        """

        telefone = re.sub(r'[^0-9]', '', value)

        if len(telefone) not in [10, 11]:
            raise ValidationError('Número de Telefone Inválido')

        ddd = telefone[:2]
        valid_ddds = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33',
                      '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55',
                      '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82',
                      '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']

        if ddd not in valid_ddds:
            raise ValidationError('O Número de Telefone digitado é inválido.')

    @staticmethod
    def validate_image_url(value):
        """
        Validates an image URL.
        :param value: Image URL as a string.
        :raises: ValidationError if the image URL is invalid or inaccessible.
        """

        url_validator = URLValidator()
        try:
            url_validator(value)
        except ValidationError:
            raise ValidationError('URL da imagem é inválida')

        try:
            response = requests.head(value)
            if response.status_code != 200 or not response.headers.get('content-type', '').startswith('image/'):
                raise ValidationError('A URL não aponta pra uma imagem acessível')
        except requests.exceptions.RequestException:
            raise ValidationError('Não foi possível acessar a imagem')
