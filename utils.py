
def abreviar_texto(texto):
    """Abrevia termos comuns para caber melhor no documento."""
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
        "01.02.01": "Gab. Prefeito Depend.",
        "01.02.02": "Procuradoria Jurídica",
        "01.02.03": "Depto. Adm.",
        "01.02.04": "Depto. Almox. e Patr.",
        "01.02.05": "Depto. Finanças",
        "01.02.06": "Depto. Licit. e Compras",
        "01.02.07": "Depto. Convênios",
        "01.02.08": "Depto. Planejamento",
        "01.02.09": "Depto. Desenv. Econ. e Trab.",
        "01.02.10": "Depto. Obras",
        "01.02.11": "Depto. Serv. Urb. e Rurais",
        "01.02.12": "Depto. Agric. e Meio Amb.",
        "01.02.13": "Depto. Seg. e Trânsito",
        "01.02.14": "Depto. Educ. Ens. Básico",
        "01.02.15": "Depto. Educ. FUNDEB Mag.",
        "01.02.16": "Depto. Educ. FUNDEB - Out. Desp.",
        "01.02.17": "Depto. Educ. - Merenda Escolar",
        "01.02.18": "Depto. Cultura e Turismo",
        "01.02.19": "Depto. Esp. e Lazer",
        "01.02.20": "Fundo Mun. Saúde",
        "01.02.21": "Depto. Ação Social",
        "01.02.22": "Encargos Gerais Munic.",
        "01.02.23": "Depto. Tec. Inf. e Inov.",
        "01.02.24": "Depto. Adm. Tributária",
        "01.02.99": "Reserva de Cont.",
        "02.01.01": "Câmara Mun.",
        "04.04.01": "Depto. Comercial",
        "04.04.02": "Depto. Obras e Serv.",
        "04.04.03": "Depto. Capt. e Trat. Água",
        "04.04.04": "Depto. Trat. Esgoto",
        "05.05.01": "Fundo Prev. Serv. Mun."
    }
    for original, abreviado in substituicoes.items():
        if original in texto:
             texto = texto.replace(original, abreviado)
    return texto
