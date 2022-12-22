# E-commerce
- Um site e-commerce simples feito em python com framework django.

## Este projeto NÃO inclui
Abaixo uma lista de recursos que não adicionei:

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento

## Como usar windows ?
- git clone https://github.com/kauansr/E-commerce.git
- cd E-commerce
- python -m venv venv
- venv\Scripts\activate.bat
- python -m pip install --upgrade pip setuptools wheel --user
- python -m pip install django django-crispy-forms pillow
- python manage.py migrate
