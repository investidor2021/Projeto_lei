
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
    for original, abreviado in substituicoes.items():
        if original in texto:
             texto = texto.replace(original, abreviado)
    return texto
