"""
Módulo para gerenciamento de códigos AUDESP (Tribunal de Contas do Estado de SP)
Estrutura: XX.XX.XX.XX.XXX.XXXX.XXXX
           Poder.Órgão.Depto.Função.Subfunção.Programa.Projeto/Atividade
"""

# ===============================
# DEPARTAMENTOS (fornecido pelo usuário)
# ===============================
DEPARTAMENTOS = {
    "01.02.01": "GABINETE PREFEITO DEPENDÊNCIAS",
    "01.02.02": "PROCURADORIA JURIDICA",
    "01.02.03": "DEPTO DE ADMINISTRACÃO",
    "01.02.04": "DEPTO DE ALMOXARIFADO E PATRIMONIO",
    "01.02.05": "DEPTO DE FINANÇAS",
    "01.02.06": "DEPTO DE LICITAÇÃO E COMPRAS",
    "01.02.07": "DEPTO DE CONVÊNIOS",
    "01.02.08": "DEPTO DE PLANEJAMENTO",
    "01.02.09": "DEPTO DE DESENV. ECONOM. E DO TRABALHO",
    "01.02.10": "DEPTO DE OBRAS",
    "01.02.11": "DEPTO DE SERVIÇOS URBANOS E RURAIS",
    "01.02.12": "DEPTO DA AGRICULTURA E MEIO AMBIENTE",
    "01.02.13": "DEPTO DE SEGURANÇA E TRÂNSITO",
    "01.02.14": "DEPTO DE EDUCAÇÃO - ENSINO BASICO",
    "01.02.15": "DEPTO DE EDUCAÇÃO FUNDEB MAGISTERIO",
    "01.02.16": "DEPTO DE EDUCAÇÃO FUNDEB - OTS DESPESAS",
    "01.02.17": "DEPTO DE EDUCAÇÃO - MERENDA ESCOLAR",
    "01.02.18": "DEPTO DE CULTURA E TURISMO",
    "01.02.19": "DEPTO DE ESPORTES E LAZER",
    "01.02.20": "FUNDO MUNICIPAL DE SAUDE",
    "01.02.21": "DEPTO DE AÇÃO SOCIAL",
    "01.02.22": "ENCARGOS GERAIS DO MUNICIPIO",
    "01.02.23": "DEPTO DE TECNOLOGIA DA INFORMAÇÃO E INOVAÇÃO",
    "01.02.24": "DEPTO DE ADMINISTRAÇÃO TRIBUTÁRIA",
    "01.02.99": "RESERVA DE CONTIGÊNCIA",
    "02.01.01": "CÂMARA MUNICIPAL",
    "04.04.01": "DEPARTAMENTO COMERCIAL",
    "04.04.02": "DEPARTAMENTO DE OBRAS E SERVIÇOS",
    "04.04.03": "DEPARTAMENTO DE CAPTAÇÃOO E TRATAMENTO DE AGUA",
    "04.04.04": "DEPARTAMENTO DE TRATAMENTO DE ESGOTO",
    "05.05.01": "FUNDO DE PREVIDÊNCIA DOS SERVIDORES MUNICIPAIS"
}

# ===============================
# FUNÇÕES DE GOVERNO (AUDESP - Padrão Nacional)
# ===============================
FUNCOES = {
    "01": "Legislativa",
    "02": "Judiciária",
    "03": "Essencial à Justiça",
    "04": "Administração",
    "05": "Defesa Nacional",
    "06": "Segurança Pública",
    "07": "Relações Exteriores",
    "08": "Assistência Social",
    "09": "Previdência Social",
    "10": "Saúde",
    "11": "Trabalho",
    "12": "Educação",
    "13": "Cultura",
    "14": "Direitos da Cidadania",
    "15": "Urbanismo",
    "16": "Habitação",
    "17": "Saneamento",
    "18": "Gestão Ambiental",
    "19": "Ciência e Tecnologia",
    "20": "Agricultura",
    "21": "Organização Agrária",
    "22": "Indústria",
    "23": "Comércio e Serviços",
    "24": "Comunicações",
    "25": "Energia",
    "26": "Transporte",
    "27": "Desporto e Lazer",
    "28": "Encargos Especiais",
    "99": "Reserva de Contingência"
}

# ===============================
# SUBFUNÇÕES DE GOVERNO (AUDESP - Principais)
# ===============================
SUBFUNCOES = {
    "031": "Ação Legislativa",
    "032": "Controle Externo",
    "061": "Ação Judiciária",
    "062": "Defesa do Interesse Público no Processo Judiciário",
    "091": "Defesa da Ordem Jurídica",
    "092": "Representação Judicial e Extrajudicial",
    "121": "Planejamento e Orçamento",
    "122": "Administração Geral",
    "123": "Administração Financeira",
    "124": "Controle Interno",
    "125": "Normatização e Fiscalização",
    "126": "Tecnologia da Informação",
    "127": "Ordenamento Territorial",
    "128": "Formação de Recursos Humanos",
    "129": "Administração de Receitas",
    "130": "Administração de Concessões",
    "131": "Comunicação Social",
    "151": "Defesa Territorial",
    "152": "Defesa Civil",
    "181": "Policiamento",
    "182": "Defesa Civil",
    "183": "Informação e Inteligência",
    "211": "Relações Diplomáticas",
    "212": "Cooperação Internacional",
    "241": "Assistência ao Idoso",
    "242": "Assistência ao Portador de Deficiência",
    "243": "Assistência à Criança e ao Adolescente",
    "244": "Assistência Comunitária",
    "271": "Previdência Básica",
    "272": "Previdência do Regime Estatutário",
    "273": "Previdência Complementar",
    "274": "Previdência Especial",
    "301": "Atenção Básica",
    "302": "Assistência Hospitalar e Ambulatorial",
    "303": "Suporte Profilático e Terapêutico",
    "304": "Vigilância Sanitária",
    "305": "Vigilância Epidemiológica",
    "306": "Alimentação e Nutrição",
    "331": "Proteção e Benefícios ao Trabalhador",
    "332": "Relações de Trabalho",
    "333": "Empregabilidade",
    "334": "Fomento ao Trabalho",
    "361": "Ensino Fundamental",
    "362": "Ensino Médio",
    "363": "Ensino Profissional",
    "364": "Ensino Superior",
    "365": "Educação Infantil",
    "366": "Educação de Jovens e Adultos",
    "367": "Educação Especial",
    "368": "Educação Básica",
    "391": "Patrimônio Histórico, Artístico e Arqueológico",
    "392": "Difusão Cultural",
    "421": "Custódia e Reintegração Social",
    "422": "Direitos Individuais, Coletivos e Difusos",
    "423": "Assistência aos Povos Indígenas",
    "451": "Infra-Estrutura Urbana",
    "452": "Serviços Urbanos",
    "453": "Transportes Coletivos Urbanos",
    "481": "Habitação Rural",
    "482": "Habitação Urbana",
    "511": "Saneamento Básico Rural",
    "512": "Saneamento Básico Urbano",
    "541": "Preservação e Conservação Ambiental",
    "542": "Controle Ambiental",
    "543": "Recuperação de Áreas Degradadas",
    "544": "Recursos Hídricos",
    "545": "Meteorologia",
    "571": "Desenvolvimento Científico",
    "572": "Desenvolvimento Tecnológico e Engenharia",
    "573": "Difusão do Conhecimento Científico e Tecnológico",
    "601": "Promoção da Produção Vegetal",
    "602": "Promoção da Produção Animal",
    "603": "Defesa Sanitária Vegetal",
    "604": "Defesa Sanitária Animal",
    "605": "Abastecimento",
    "606": "Extensão Rural",
    "607": "Irrigação",
    "631": "Reforma Agrária",
    "632": "Colonização",
    "661": "Promoção Industrial",
    "662": "Produção Industrial",
    "663": "Mineração",
    "664": "Propriedade Industrial",
    "665": "Normalização e Qualidade",
    "691": "Promoção Comercial",
    "692": "Comercialização",
    "693": "Comércio Exterior",
    "694": "Serviços Financeiros",
    "695": "Turismo",
    "721": "Comunicações Postais",
    "722": "Telecomunicações",
    "751": "Conservação de Energia",
    "752": "Energia Elétrica",
    "753": "Combustíveis Minerais",
    "754": "Biocombustíveis",
    "781": "Transporte Aéreo",
    "782": "Transporte Rodoviário",
    "783": "Transporte Ferroviário",
    "784": "Transporte Hidroviário",
    "785": "Transportes Especiais",
    "811": "Desporto de Rendimento",
    "812": "Desporto Comunitário",
    "813": "Lazer",
    "841": "Refinanciamento da Dívida Interna",
    "842": "Refinanciamento da Dívida Externa",
    "843": "Serviço da Dívida Interna",
    "844": "Serviço da Dívida Externa",
    "845": "Outras Transferências",
    "846": "Outros Encargos Especiais",
    "847": "Transferências para a Educação Básica",
    "999": "Reserva de Contingência"
}

# ===============================
# PROGRAMAS DE GOVERNO (fornecido pelo usuário)
# ===============================
PROGRAMAS = {
    "0001": "PROCESSO LEGISLATIVO",
    "0002": "COORDENAÇÃO SUPERIOR",
    "0003": "GESTÃO ADMINISTRATIVA/FINANCEIRA",
    "0004": "DESENVOLVIMENTO ECONOMICO",
    "0005": "DESENVOLVIMENTO E SERVIÇOS URBANOS",
    "0007": "DESENVOLVIMENTO AMBIENTAL",
    "0008": "TRANSITO MUNICIPAL",
    "0009": "GUARDA MUNICIPAL",
    "0010": "EDUCAÇÃO BÁSICA",
    "0012": "TRANSPORTE DE ALUNOS",
    "0014": "ALIMENTAÇÃO ESCOLAR",
    "0015": "CULTURA E TURISMO",
    "0016": "ESPORTE E LAZER",
    "0017": "GESTÃO DAS AÇÕES E SERV. DE SAUDE",
    "0018": "PROGRAMA DE ATENÇÃO BASICA",
    "0019": "PROGRAMA MEDIA ALTA COMPLEXIDADE",
    "0020": "PROGRAMA VIGILANCIA EM SAÚDE",
    "0021": "PROGRAMA ASSSITENCIA FARMACEUTICA",
    "0022": "PROGRAMA GESTÃO SUS",
    "0025": "ASSISTENCIA SOCIAL GERAL",
    "0030": "PROGRAMA AUXILIO TRANSPORTE DE ESTUDANTE",
    "0032": "TRANSPORTE COLETIVO URBANO",
    "0033": "SANEAMENTO GERAL",
    "0034": "RESERVA DE CONTINGENCIA",
    "0035": "FUNDO DE PREVIDENCIA - RPPS",
    "0036": "UNIFORME ESCOLAR"
}

# GRUPOS DE NATUREZA removidos - não são mais necessários

# ===============================
# CATEGORIAS ECONÔMICAS
# ===============================
CATEGORIAS_ECONOMICAS = {
    "3": "Despesas Correntes",
    "4": "Despesas de Capital"
}

# ===============================
# GRUPOS DE NATUREZA DA DESPESA
# ===============================
GRUPOS_DESPESA = {
    "1": "Pessoal e Encargos Sociais",
    "2": "Juros e Encargos da Dívida",
    "3": "Outras Despesas Correntes",
    "4": "Investimentos",
    "5": "Inversões Financeiras",
    "6": "Amortização da Dívida"
}

# ===============================
# MODALIDADES DE APLICAÇÃO
# ===============================
MODALIDADES_APLICACAO = {
    "20": "Transferências à União",
    "22": "Execução Orçamentária Delegada à União",
    "30": "Transferências a Estados e ao Distrito Federal",
    "31": "Transferências a Estados e ao Distrito Federal - Fundo a Fundo",
    "32": "Execução Orçamentária Delegada a Estados e ao Distrito Federal",
    "35": "Transferências Fundo a Fundo aos Estados e ao Distrito Federal à conta de recursos de que tratam os §§ 1º e 2º do art. 24 da Lei Complementar nº 141, de 2012",
    "36": "Transferências Fundo a Fundo aos Estados e ao Distrito Federal à conta de recursos de que trata o art. 25 da Lei Complementar nº 141, de 2012",
    "40": "Transferências a Municípios",
    "41": "Transferências a Municípios - Fundo a Fundo",
    "42": "Execução Orçamentária Delegada a Municípios",
    "45": "Transferências Fundo a Fundo aos Municípios à conta de recursos de que tratam os §§ 1º e 2º do art. 24 da Lei Complementar nº 141, de 2012",
    "46": "Transferências Fundo a Fundo aos Municípios à conta de recursos de que trata o art. 25 da Lei Complementar nº 141, de 2012",
    "50": "Transferências a Instituições Privadas sem Fins Lucrativos",
    "60": "Transferências a Instituições Privadas com Fins Lucrativos",
    "67": "Execução de Contrato de Parceria Público-Privada - PPP",
    "70": "Transferências a Instituições Multigovernamentais",
    "71": "Transferências a Consórcios Públicos mediante contrato de rateio",
    "72": "Execução Orçamentária Delegada a Consórcios Públicos",
    "73": "Transferências a Consórcios Públicos mediante contrato de rateio à conta de recursos de que tratam os §§ 1º e 2º do art. 24 da Lei Complementar nº 141, de 2012",
    "74": "Transferências a Consórcios Públicos mediante contrato de rateio à conta de recursos de que trata o art. 25 da Lei Complementar nº 141, de 2012",
    "75": "Transferências a Instituições Multigovernamentais à conta de recursos de que tratam os §§ 1º e 2º do art. 24 da Lei Complementar nº 141, de 2012",
    "76": "Transferências a Instituições Multigovernamentais à conta de recursos de que trata o art. 25 da Lei Complementar nº 141, de 2012",
    "80": "Transferências ao Exterior",
    "90": "Aplicações Diretas",
    "91": "Aplicação Direta Decorrente de Operação entre Órgãos, Fundos e Entidades Integrantes dos Orçamentos Fiscal e da Seguridade Social",
    "93": "Aplicação Direta Decorrente de Operação de Órgãos, Fundos e Entidades Integrantes dos Orçamentos Fiscal e da Seguridade Social com Consórcio Público do qual o Ente Participe",
    "94": "Aplicação Direta Decorrente de Operação de Órgãos, Fundos e Entidades Integrantes dos Orçamentos Fiscal e da Seguridade Social com Consórcio Público do qual o Ente Não Participe",
    "95": "Aplicação Direta à conta de recursos de que tratam os §§ 1º e 2º do art. 24 da Lei Complementar nº 141, de 2012",
    "96": "Aplicação Direta à conta de recursos de que trata o art. 25 da Lei Complementar nº 141, de 2012",
    "99": "A Definir"
}

# ===============================
# ELEMENTOS DE DESPESA SIMPLIFICADOS (Código Completo)
# Formato: Cat.Grupo.Modalidade.Elemento.Desdobramento
# ===============================
ELEMENTOS_DESPESA_SIMPLIFICADOS = {
    "3.1.90.04.00": "Contratação por Tempo Determinado",
    "3.1.90.11.00": "Vencimentos e Vantagens Fixas - Pessoal Civil",
    "3.1.90.13.00": "Obrigações Patronais",
    "3.1.91.13.00": "Obrigações Patronais",
    "3.1.90.16.00": "Outras Despesas Variáveis - Pessoal Civil",
    "3.1.71.70.00": "Rateio pela Participação em Consórcio Público",
    "3.2.90.21.00": "Juros sobre a Dívida por Contrato",
    "3.3.90.08.00": "Outros Benefícios Assistenciais do Servidor e do Militar",
    "3.3.90.14.00": "Diárias - Civil",
    "3.3.90.18.00": "Auxílio Financeiro a Estudante",
    "3.3.90.30.00": "Material de Consumo",
    "3.3.50.30.00": "Material de Consumo",
    "3.3.90.32.00": "Material, Bem ou Serviço para Distribuição Gratuita",
    "3.3.90.35.00": "Serviços de Consultoria",
    "3.3.90.36.00": "Outros Serviços de Terceiros - Pessoa Física",
    "3.3.90.39.00": "Outros Serviços de Terceiros - Pessoa Jurídica",
    "3.3.50.39.00": "Outros Serviços de Terceiros - Pessoa Jurídica",
    "3.3.90.40.00": "Serviços de Tecnologia da Informação e Comunicação - Pessoa Jurídica",
    "3.3.90.46.00": "Auxílio-Alimentação",
    "3.3.90.47.00": "Obrigações Tributárias e Contributivas",
    "3.3.90.91.00": "Sentenças Judiciais",
    "3.3.90.92.00": "Despesas de Exercícios Anteriores",
    "3.3.90.93.00": "Indenizações e Restituições",
    "3.3.71.70.00": "Rateio pela Participação em Consórcio Público",
    "4.4.90.51.00": "Obras e Instalações",
    "4.4.50.51.00": "Obras e Instalações",
    "4.4.90.52.00": "Equipamentos e Material Permanente",
    "4.4.50.52.00": "Equipamentos e Material Permanente",
    "4.4.90.61.00": "Aquisição de Imóveis",
    "4.4.90.93.00": "Indenizações e Restituições",
    "4.6.90.71.00": "Principal da Dívida Contratual Resgatado",
    "9.9.99.99.00": "Reserva de Contingência"
}

# ===============================
# ELEMENTOS DE DESPESA DETALHADOS (Apenas Elemento)
# Para uso no modo avançado
# ===============================
ELEMENTOS_DESPESA_DETALHADOS = {
    "04": "Contratação por Tempo Determinado",
    "08": "Outros Benefícios Assistenciais do Servidor e do Militar",
    "11": "Vencimentos e Vantagens Fixas - Pessoal Civil",
    "13": "Obrigações Patronais",
    "14": "Diárias - Civil",
    "16": "Outras Despesas Variáveis - Pessoal Civil",
    "18": "Auxílio Financeiro a Estudante",
    "21": "Juros sobre a Dívida por Contrato",
    "30": "Material de Consumo",
    "32": "Material, Bem ou Serviço para Distribuição Gratuita",
    "35": "Serviços de Consultoria",
    "36": "Outros Serviços de Terceiros - Pessoa Física",
    "39": "Outros Serviços de Terceiros - Pessoa Jurídica",
    "40": "Serviços de Tecnologia da Informação e Comunicação - Pessoa Jurídica",
    "46": "Auxílio-Alimentação",
    "47": "Obrigações Tributárias e Contributivas",
    "51": "Obras e Instalações",
    "52": "Equipamentos e Material Permanente",
    "61": "Aquisição de Imóveis",
    "70": "Rateio pela Participação em Consórcio Público",
    "71": "Principal da Dívida Contratual Resgatado",
    "91": "Sentenças Judiciais",
    "92": "Despesas de Exercícios Anteriores",
    "93": "Indenizações e Restituições",
    "99": "Reserva de Contingência"
}

# ===============================
# FONTES DE RECURSOS (Utilizadas pelo Município)
# ===============================
FONTES_RECURSOS = {
    "01": "Tesouro",
    "02": "Transferências e Convênios Estaduais - Vinculados",
    "03": "Recursos Próprios de Fundos Especiais de Despesa - Vinculados",
    "04": "Recursos Próprios da Administração Indireta",
    "05": "Transferências e Convênios Federais - Vinculados",
    "06": "Outras Fontes de Recursos",
    "07": "Operações de Crédito",
    "08": "Emendas Parlamentares Individuais - Legislativo Municipal",
    "19": "Recursos Extraorçamentários",
    "91": "Tesouro - Exercícios Anteriores",
    "92": "Transferências e Convênios Estaduais - Vinculados - Exercícios Anteriores",
    "93": "Recursos Próprios de Fundos Especiais de Despesa - Vinculados - Exercícios Anteriores",
    "94": "Recursos Próprios da Administração Indireta - Exercícios Anteriores",
    "95": "Transferências e Convênios Federais - Vinculados - Exercícios Anteriores",
    "96": "Outras Fontes de Recursos - Exercícios Anteriores",
    "97": "Operações de Crédito - Exercícios Anteriores",
    "98": "Emendas Parlamentares Individuais - Exercícios Anteriores"
}

# ===============================
# APLICAÇÕES (Códigos de Aplicação do Município)
# ===============================
APLICACOES = {
    # GERAL (100-199)
    "0100": "Geral Total",
    "0110": "Geral",
    "0111": "Remuneração de Aplicações Financeiras",
    "0112": "Recursos Lei Complementar nº 194/2022",
    "0113": "Cessão de Direitos Creditórios",
    "0120": "Alienação de Bens",
    "0121": "Remuneração de Aplicações Financeiras",
    "0130": "CIDE - Contribuição de Intervenção no Domínio Econômico",
    "0131": "Remuneração de Aplicações Financeiras",
    "0140": "Royalties da Exploração do Petróleo e Gás Natural",
    "0141": "Remuneração de Aplicações Financeiras",
    "0190": "Movimentações Extraorçamentárias Geral",
    
    # EDUCAÇÃO (200-299)
    "0200": "Educação",
    "0210": "Educação Infantil",
    "0212": "Educação Infantil - Creche",
    "0213": "Educação Infantil - Pré-Escola",
    "0220": "Ensino Fundamental",
    "0230": "Ensino Médio",
    "0240": "Educação Especial",
    "0260": "Educação - FUNDEB",
    "0261": "Educação - FUNDEB - Magistério/Profissionais da Educação",
    "0262": "Educação - FUNDEB - Outros",
    "0271": "Educação - FUNDEB - Magistério - Creche",
    "0272": "Educação - FUNDEB - Magistério - Pré-Escola",
    "0273": "Educação - FUNDEB - Outros - Creche",
    "0274": "Educação - FUNDEB - Outros - Pré-Escola",
    "0280": "Recursos do Salário Educação - Creche",
    "0281": "Recursos do Salário Educação - Pré-Escola",
    "0282": "Recursos do Salário Educação - Ensino Fundamental",
    "0283": "PNAE - Creche",
    "0284": "PNAE - Pré-Escola",
    "0285": "PNAE - Ensino Fundamental",
    "0286": "PNATE - Creche",
    "0287": "PNATE - Pré-Escola",
    "0288": "PNATE - Ensino Fundamental",
    "0291": "PDDE - Creche",
    "0292": "PDDE - Pré-Escola",
    "0293": "PDDE - Ensino Fundamental",
    
    # SAÚDE (300-399)
    "0300": "Saúde",
    "0301": "Atenção Básica",
    "0302": "Atenção de Média e Alta Complexidade",
    "0303": "Vigilância em Saúde",
    "0304": "Assistência Farmacêutica",
    "0305": "Gestão do SUS",
    "0307": "Outros Programas Financiados por Transferências Fundo a Fundo",
    "0308": "Convênios SUS",
    "0309": "Serviços de Saúde",
    "0310": "Saúde - Geral",
    "0312": "Recursos para Combate ao Coronavírus",
    "0313": "Transferências para ACS e ACE",
    "0350": "Bloco de Custeio das Ações e Serviços Públicos de Saúde",
    "0360": "Bloco de Investimentos na Rede de Serviços de Saúde",
    "0370": "Assistência Financeira Complementar - Piso Salarial da Enfermagem",
    
    # TRÂNSITO (400-499)
    "0400": "Trânsito",
    "0410": "Trânsito - Sinalização",
    "0420": "Trânsito - Engenharia de Trânsito",
    "0430": "Trânsito - Engenharia de Campo",
    "0440": "Trânsito - Policiamento",
    "0450": "Trânsito - Fiscalização",
    "0460": "Trânsito - Educação de Trânsito",
    "0470": "Trânsito - FUNSET",
    
    # ASSISTÊNCIA SOCIAL (500-599)
    "0500": "Assistência Social",
    "0510": "Assistência Social - Geral",
    
    # REGIME PRÓPRIO DE PREVIDÊNCIA (600-699)
    "0600": "Regime Próprio de Previdência Social",
    "0601": "RPPS - Plano Financeiro",
    "0602": "RPPS - Plano Previdenciário",
    "0603": "RPPS - Plano Previdenciário - Poder Executivo",
    "0604": "RPPS - Plano Previdenciário - Poder Legislativo",
    "0605": "RPPS - Plano Financeiro - Poder Executivo",
    "0606": "RPPS - Plano Financeiro - Poder Legislativo",
    "0690": "RPPS - Taxa Administração",

    # EMENDAS (800-899)
    "0800": "Emendas Parlamentares",
    "0801": "Emendas Parlamentares Estaduais",
    "0802": "Emendas Parlamentares Municipais"
}


# ===============================
# FUNÇÕES DE VALIDAÇÃO E COMPOSIÇÃO
# ===============================

def validar_departamento(codigo):
    """Valida se o código do departamento existe."""
    return codigo in DEPARTAMENTOS

def validar_funcao(codigo):
    """Valida se o código da função existe."""
    return codigo in FUNCOES

def validar_subfuncao(codigo):
    """Valida se o código da subfunção existe."""
    return codigo in SUBFUNCOES

def validar_programa(codigo):
    """Valida se o código do programa existe."""
    return codigo in PROGRAMAS

def compor_dotacao(depto, funcao, subfuncao, programa, projeto):
    """
    Compõe o código completo da dotação AUDESP.
    
    Args:
        depto: Código do departamento (ex: "01.02.20")
        funcao: Código da função (ex: "10")
        subfuncao: Código da subfunção (ex: "122")
        programa: Código do programa (ex: "0017")
        projeto: Código do projeto/atividade (ex: "2051")
    
    Returns:
        String com o código completo (ex: "01.02.20.10.122.0017.2051")
    """
    return f"{depto}.{funcao}.{subfuncao}.{programa}.{projeto}"

def decompor_dotacao(codigo_completo):
    """
    Decompõe um código de dotação em suas partes.
    
    Args:
        codigo_completo: String com código completo (ex: "01.02.20.10.122.0017.2051")
    
    Returns:
        Dict com as partes decompostas
    """
    partes = codigo_completo.split(".")
    if len(partes) != 7:
        return None
    
    return {
        "poder": partes[0],
        "orgao": partes[1],
        "departamento_num": partes[2],
        "departamento_completo": f"{partes[0]}.{partes[1]}.{partes[2]}",
        "funcao": partes[3],
        "subfuncao": partes[4],
        "programa": partes[5],
        "projeto": partes[6]
    }

def obter_descricao_completa(codigo_completo):
    """
    Retorna a descrição completa de uma dotação baseada no código.
    
    Args:
        codigo_completo: String com código completo
    
    Returns:
        String com descrição formatada
    """
    partes = decompor_dotacao(codigo_completo)
    if not partes:
        return "Código inválido"
    
    descricoes = []
    
    # Departamento
    depto_cod = partes["departamento_completo"]
    if depto_cod in DEPARTAMENTOS:
        descricoes.append(DEPARTAMENTOS[depto_cod])
    
    # Função
    if partes["funcao"] in FUNCOES:
        descricoes.append(f"Função: {FUNCOES[partes['funcao']]}")
    
    # Subfunção
    if partes["subfuncao"] in SUBFUNCOES:
        descricoes.append(f"Subfunção: {SUBFUNCOES[partes['subfuncao']]}")
    
    # Programa
    if partes["programa"] in PROGRAMAS:
        descricoes.append(f"Programa: {PROGRAMAS[partes['programa']]}")
    
    return " - ".join(descricoes)

def obter_opcoes_departamento():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(DEPARTAMENTOS.items())]

def obter_opcoes_funcao():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(FUNCOES.items())]

def obter_opcoes_subfuncao():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(SUBFUNCOES.items())]

def obter_opcoes_programa():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(PROGRAMAS.items())]

def obter_opcoes_grupo_natureza():
    """DEPRECATED - Grupos de natureza foram removidos."""
    return []

def obter_opcoes_categoria_economica():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(CATEGORIAS_ECONOMICAS.items())]

def obter_opcoes_grupo_despesa():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(GRUPOS_DESPESA.items())]

def obter_opcoes_modalidade():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(MODALIDADES_APLICACAO.items())]

def obter_opcoes_elemento_simplificado():
    """Retorna lista formatada de elementos SIMPLIFICADOS (código completo) para selectbox."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(ELEMENTOS_DESPESA_SIMPLIFICADOS.items())]

def obter_opcoes_elemento_detalhado():
    """Retorna lista formatada de elementos DETALHADOS (apenas elemento) para selectbox."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(ELEMENTOS_DESPESA_DETALHADOS.items())]

def obter_opcoes_elemento():
    """Compatibilidade: redireciona para elementos simplificados."""
    return obter_opcoes_elemento_simplificado()

def obter_opcoes_fonte():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(FONTES_RECURSOS.items())]

def obter_opcoes_aplicacao():
    """Retorna lista formatada para selectbox do Streamlit."""
    return [(cod, f"{cod} - {nome}") for cod, nome in sorted(APLICACOES.items())]

def compor_dotacao_completa(depto, funcao, subfuncao, programa, grupo_nat, num_projeto,
                            cat_econ, grupo_desp, modalidade, elemento, desdobramento,
                            fonte, aplicacao):
    """
    Compõe o código COMPLETO da dotação orçamentária AUDESP.
    
    Estrutura: XX.XX.XX.XX.XXX.XXXX.X.XXX.X.X.XX.XX.XX.XX.XX.XX.XX.XX.XXXX
    
    Args:
        depto: Departamento (ex: "01.02.16")
        funcao: Função (ex: "12")
        subfuncao: Subfunção (ex: "361")
        programa: Programa (ex: "0013")
        grupo_nat: Grupo de Natureza - Tipo (ex: "2" para Projeto, "3" para Atividade)
        num_projeto: Número do Projeto/Atividade (ex: "126")
        cat_econ: Categoria Econômica (ex: "3" para Corrente, "4" para Capital)
        grupo_desp: Grupo de Despesa (ex: "1" para Pessoal)
        modalidade: Modalidade de Aplicação (ex: "90" para Aplicações Diretas)
        elemento: Elemento de Despesa (ex: "11" para Vencimentos)
        desdobramento: Desdobramento (ex: "00" ou "00.00.00.00.00")
        fonte: Fonte de Recursos (ex: "02")
        aplicacao: Aplicação (ex: "0265")
    
    Returns:
        String com o código completo
        Ex: "01.02.16.12.361.0013.2126.3.1.90.11.00.00.00.00.00.02.0265"
    """
    # Compor o número completo do projeto/atividade (tipo + número)
    projeto_completo = f"{grupo_nat}{num_projeto}"
    
    # Garantir que desdobramento tenha o formato correto (5 partes de 2 dígitos)
    if not desdobramento or desdobramento == "00":
        desdobramento = "00.00.00.00.00"
    
    # Compor o código completo
    codigo = (f"{depto}.{funcao}.{subfuncao}.{programa}.{projeto_completo}."
             f"{cat_econ}.{grupo_desp}.{modalidade}.{elemento}.{desdobramento}."
             f"{fonte}.{aplicacao}")
    
    return codigo

def obter_descricao_completa_detalhada(codigo_completo):
    """
    Retorna descrição detalhada de uma dotação orçamentária completa.
    
    Args:
        codigo_completo: Código completo da dotação
    
    Returns:
        String com descrição formatada
    """
    partes = codigo_completo.split(".")
    if len(partes) < 7:
        return "Código incompleto"
    
    descricoes = []
    
    # Departamento (partes 0, 1, 2)
    if len(partes) >= 3:
        depto_cod = f"{partes[0]}.{partes[1]}.{partes[2]}"
        if depto_cod in DEPARTAMENTOS:
            descricoes.append(DEPARTAMENTOS[depto_cod])
    
    # Função (parte 3)
    if len(partes) >= 4 and partes[3] in FUNCOES:
        descricoes.append(f"Função: {FUNCOES[partes[3]]}")
    
    # Subfunção (parte 4)
    if len(partes) >= 5 and partes[4] in SUBFUNCOES:
        descricoes.append(f"Subfunção: {SUBFUNCOES[partes[4]]}")
    
    # Programa (parte 5)
    if len(partes) >= 6 and partes[5] in PROGRAMAS:
        descricoes.append(f"Programa: {PROGRAMAS[partes[5]]}")
    
    # Projeto/Atividade (parte 6) - grupos de natureza foram removidos
    # Elemento de Despesa (parte 10) - usar elementos simplificados
    
    # Fonte de Recursos (parte 17 ou penúltima)
    if len(partes) >= 18 and partes[17] in FONTES_RECURSOS:
        descricoes.append(f"Fonte: {FONTES_RECURSOS[partes[17]]}")
    
    return " - ".join(descricoes)
