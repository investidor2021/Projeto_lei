import re
from audesp_codes import DEPARTAMENTOS

def abreviar_texto(texto, cod_depto=None):
    """
    Abrevia termos comuns para caber melhor no documento.
    Se cod_depto for validado, retorna o nome abreviado diretamente mapeado.
    """
    # 1. Prioridade: Busca direta pelo código
    if cod_depto:
         cod_limpo = str(cod_depto).strip()
         if cod_limpo in DEPARTAMENTOS:
             return DEPARTAMENTOS[cod_limpo]

    # 2. Tentar encontrar o código do departamento no texto (ex: 01.02.01)
    # O código geralmente está no início ou faz parte da string de dotação
    if not cod_depto:
        match_depto = re.search(r'\b(\d{2}\.\d{2}\.\d{2})\b', texto)
        if match_depto:
            codigo = match_depto.group(1)
            if codigo in DEPARTAMENTOS:
                 return DEPARTAMENTOS[codigo]

    substituicoes = {
        "MATERIAL DE CONSUMO":"Mat. Cons.",
        "OUTROS BENEFÍCIOS ASSISTENCIAIS DO SERVIDOR E DO MILITAR":"Outros Ben. Assist. Serv. e Mil.",
        "VENCIMENTOS E VANTAGENS FIXAS - PESSOAL CIVIL":"Venc. e Vant. - P Civil",
        "OUTRAS DESPESAS VARIÁVEIS - PESSOAL CIVIL":"Outras Desp. Var. - P Civil",
        "OUTROS SERVIÇOS DE TERCEIROS - PESSOA FÍSICA":"Outros Serv. Terc. - PF",
        "OUTROS SERVIÇOS DE TERCEIROS - PESSOA JURÍDICA":"Outros Serv. Terc. - PJ",
        "SERVIÇOS DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO - PESSOA JURÍDICA":"Serv. T.I. e Com. - PJ",
        "EQUIPAMENTOS E MATERIAL PERMANENTE":"Eq. e Mat. Perm.",
        "MATERIAL, BEM OU SERVIÇO PARA DISTRIBUIÇÃO GRATUITA":"Mat., Bem ou Serv. para Dist. Grat.",
        "PRINCIPAL DA DÍVIDA CONTRATUAL RESGATADO":"Princ. da Dívida Contr. Resg.",
        "JUROS SOBRE A DÍVIDA POR CONTRATO":"Juros s/ a Dívida por Contr.",
        
        # Mapeamento Reverso (Nome Completo -> Abreviação)
        # Importante: O texto de entrada deve conter esses nomes exatos para a substituição funcionar.
        "GABINETE PREFEITO DEPENDÊNCIAS": "Gab. Prefeito Depend.",
        "PROCURADORIA JURIDICA": "Procuradoria Jurídica",
        "DEPTO DE ADMINISTRACÃO": "Depto. Adm.",
        "DEPTO DE ALMOXARIFADO E PATRIMONIO": "Depto. Almox. e Patr.",
        "DEPTO DE FINANÇAS": "Depto. Finanças",
        "DEPTO DE LICITAÇÃO E COMPRAS": "Depto. Licit. e Compras",
        "DEPTO DE CONVÊNIOS": "Depto. Convênios",
        "DEPTO DE PLANEJAMENTO": "Depto. Planejamento",
        "DEPTO DE DESENV. ECONOM. E DO TRABALHO": "Depto. Desenv. Econ. e Trab.",
        "DEPTO DE OBRAS": "Depto. Obras",
        "DEPTO DE SERVIÇOS URBANOS E RURAIS": "Depto. Serv. Urb. e Rurais",
        "DEPTO DA AGRICULTURA E MEIO AMBIENTE": "Depto. Agric. e Meio Amb.",
        "DEPTO DE SEGURANÇA E TRÂNSITO": "Depto. Seg. e Trânsito",
        "DEPTO DE EDUCAÇÃO - ENSINO BASICO": "Depto. Educ. Ens. Básico",
        "DEPTO DE EDUCAÇÃO FUNDEB MAGISTERIO": "Depto. Educ. FUNDEB Mag.",
        "DEPTO DE EDUCAÇÃO FUNDEB - OTS DESPESAS": "Depto. Educ. FUNDEB - Out. Desp.",
        "DEPTO DE EDUCAÇÃO - MERENDA ESCOLAR": "Depto. Educ. - Merenda Escolar",
        "DEPTO DE CULTURA E TURISMO": "Depto. Cultura e Turismo",
        "DEPTO DE ESPORTES E LAZER": "Depto. Esp. e Lazer",
        "FUNDO MUNICIPAL DE SAUDE": "Fundo Mun. Saúde",
        "DEPTO DE AÇÃO SOCIAL": "Depto. Ação Social",
        "ENCARGOS GERAIS DO MUNICIPIO": "Encargos Gerais Munic.",
        "DEPTO DE TECNOLOGIA DA INFORMAÇÃO E INOVAÇÃO": "Depto. Tec. Inf. e Inov.",
        "DEPTO DE ADMINISTRAÇÃO TRIBUTÁRIA": "Depto. Adm. Tributária",
        "RESERVA DE CONTIGÊNCIA": "Reserva de Cont.",
        "CÂMARA MUNICIPAL": "Câmara Mun.",
        "DEPARTAMENTO COMERCIAL": "Depto. Comercial",
        "DEPARTAMENTO DE OBRAS E SERVIÇOS": "Depto. Obras e Serv.",
        "DEPARTAMENTO DE CAPTAÇÃOO E TRATAMENTO DE AGUA": "Depto. Capt. e Trat. Água",
        "DEPARTAMENTO DE TRATAMENTO DE ESGOTO": "Depto. Trat. Esgoto",
        "FUNDO DE PREVIDÊNCIA DOS SERVIDORES MUNICIPAIS": "Fundo Prev. Serv. Mun."
    }

    # Adicionar lógica de substituição extra baseada no código, se o texto contiver o código
    if match_depto:
        codigo = match_depto.group(1)
        if codigo in DEPARTAMENTOS:
             # Aqui temos um problema: como substituir o nome antigo pelo novo se não sabemos EXATAMENTE como o nome antigo está escrito?
             # O usuário diz: "o sistema tem que extrair o codigo do departamento para conseguir ajustar o nome"
             # Se o texto for "01.02.20 - MATERIAL DE CONSUMO - FUNDO MUNICIPAL DE SAUDE"
             # E a gente sabe que 01.02.20 é "Fundo Mun. Saúde"
             # A gente poderia tentar remover o nome antigo usando regex ou similar, mas é arriscado.
             
             # Melhor abordagem: Se a gente tem a lista de nomes que mapeiam para este código, a gente tenta substituir todos.
             # Mas não temos essa lista invertida aqui.
             pass

    for original, abreviado in substituicoes.items():
        if original in texto:
             texto = texto.replace(original, abreviado)
             
    # TENTATIVA FINAL DE RESGATE PELA SINTAXE DO CÓDIGO
    # Se o texto contém o código (ex: 01.02.20), e depois das substituições ainda NÃO contém o nome abreviado,
    # significa que a substituição falhou (provavelmente grafia diferente).
    # Nesse caso, podemos tentar forçar um append ou replace se identificarmos o padrão.
    
    return texto
