import re

tokens = {
    'IDENTIFICADOR': 0,
    'ENTERO': 1,
    'REAL': 2,
    'TIPO': 4,
    'OPSUMA': 5,
    'OPMUL': 6,
    'OPRELAC': 7,
    'OPOR': 8,
    'OPAND': 9,
    'OPNOT': 10,
    'OPIGUALDAD': 11,
    'PUNTOYCOMA': 12,
    'COMA': 13,
    'PARENTESIS_IZQ': 14,
    'PARENTESIS_DER': 15,
    'LLAVE_IZQ': 16,
    'LLAVE_DER': 17,
    'ASIGNACION': 18,
    'IF': 19,
    'WHILE': 20,
    'RETURN': 21,
    'ELSE': 22,
    'EOF': 23
}

palabras_reservadas = {"if": 19, "while": 20, "return": 21, "else": 22, "int": 4, "float": 4}

patrones = [
    (r'\d+\.\d+', 'REAL'),
    (r'\d+', 'ENTERO'),
    (r'\+|\-', 'OPSUMA'),
    (r'\*|\/', 'OPMUL'),
    (r'<=|>=|<|>', 'OPRELAC'),
    (r'\|\|', 'OPOR'),
    (r'&&', 'OPAND'),
    (r'!', 'OPNOT'),
    (r'==|!=', 'OPIGUALDAD'),
    (r';', 'PUNTOYCOMA'),
    (r',', 'COMA'),
    (r'\(', 'PARENTESIS_IZQ'),
    (r'\)', 'PARENTESIS_DER'),
    (r'\{', 'LLAVE_IZQ'),
    (r'\}', 'LLAVE_DER'),
    (r'=', 'ASIGNACION'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENTIFICADOR')
]

def analizador_lexico(codigo):
    pos = 0
    tokens_encontrados = []
    
    while pos < len(codigo):
        match = None
        for patron, tipo in patrones:
            regex = re.compile(patron)
            match = regex.match(codigo, pos)
            if match:
                lexema = match.group(0)
                if tipo == 'IDENTIFICADOR' and lexema in palabras_reservadas:
                    tokens_encontrados.append((lexema, palabras_reservadas[lexema]))
                else:
                    tokens_encontrados.append((lexema, tokens[tipo]))
                pos = match.end()
                break
        if not match:
            if codigo[pos].isspace():
                pos += 1
            else:
                raise ValueError(f"Error lexico en: {codigo[pos]}")
    
    tokens_encontrados.append(('$', tokens['EOF']))
    return tokens_encontrados

# Ejemplo de uso
codigo_fuente = "if (a >= 10) { return b + 2; }"
tokens_extraidos = analizador_lexico(codigo_fuente)
for token in tokens_extraidos:
    print(token)
