"""
Análise de Dados de Coletas - LABFICOL
=======================================

Exemplo prático: Processamento e análise de dados CSV
Demonstra uso de listas, dicionários e funções

Autor: LABFICOL/UFSC
"""

import csv
from datetime import datetime

def criar_arquivo_exemplo():
    """Cria um arquivo CSV de exemplo com dados de coleta"""
    dados = [
        ['id', 'data', 'praia', 'especie', 'biomassa_g', 'temperatura_c', 'salinidade_psu', 'profundidade_m'],
        ['1', '15/01/2025', 'Ingleses', 'Ulva lactuca', '245.3', '24.5', '35.0', '3.2'],
        ['2', '15/01/2025', 'Ingleses', 'Gracilaria', '180.7', '24.5', '35.0', '5.1'],
        ['3', '15/01/2025', 'Barra da Lagoa', 'Sargassum', '310.2', '23.8', '34.8', '4.5'],
        ['4', '20/02/2025', 'Ingleses', 'Ulva lactuca', '198.5', '26.1', '34.5', '3.0'],
        ['5', '20/02/2025', 'Barra da Lagoa', 'Gracilaria', '220.4', '25.5', '34.7', '5.3'],
        ['6', '18/03/2025', 'Ingleses', 'Ulva lactuca', '302.1', '22.3', '35.2', '3.5'],
        ['7', '18/03/2025', 'Barra da Lagoa', 'Gracilaria', '195.8', '22.0', '35.1', '5.0'],
        ['8', '22/04/2025', 'Armação', 'Ulva lactuca', '275.4', '21.5', '35.3', '3.8'],
        ['9', '22/04/2025', 'Armação', 'Sargassum', '340.5', '21.2', '35.2', '4.2'],
        ['10', '17/05/2025', 'Ingleses', 'Ulva lactuca', '310.8', '19.8', '35.4', '3.6']
    ]
    
    with open('coletas.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)
    
    print("✅ Arquivo 'coletas.csv' criado com sucesso!")

def carregar_dados(nome_arquivo='coletas.csv'):
    """Carrega dados do arquivo CSV"""
    coletas = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            for linha in leitor:
                # Converter valores numéricos
                coleta = {
                    'id': int(linha['id']),
                    'data': linha['data'],
                    'praia': linha['praia'],
                    'especie': linha['especie'],
                    'biomassa_g': float(linha['biomassa_g']),
                    'temperatura_c': float(linha['temperatura_c']),
                    'salinidade_psu': float(linha['salinidade_psu']),
                    'profundidade_m': float(linha['profundidade_m'])
                }
                coletas.append(coleta)
        
        print(f"✅ {len(coletas)} coletas carregadas de '{nome_arquivo}'")
        return coletas
    
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
        print("💡 Criando arquivo de exemplo...")
        criar_arquivo_exemplo()
        return carregar_dados(nome_arquivo)
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")
        return []

def estatisticas_basicas(coletas):
    """Calcula estatísticas básicas dos dados"""
    if not coletas:
        print("⚠️ Nenhum dado para analisar.")
        return
    
    print("\n" + "="*70)
    print("📊 ESTATÍSTICAS BÁSICAS")
    print("="*70)
    
    # Biomassa
    biomassas = [c['biomassa_g'] for c in coletas]
    print(f"\n⚖️  BIOMASSA:")
    print(f"   Média: {sum(biomassas) / len(biomassas):.2f}g")
    print(f"   Mínima: {min(biomassas):.2f}g")
    print(f"   Máxima: {max(biomassas):.2f}g")
    print(f"   Total: {sum(biomassas):.2f}g")
    
    # Temperatura
    temperaturas = [c['temperatura_c'] for c in coletas]
    print(f"\n🌡️  TEMPERATURA:")
    print(f"   Média: {sum(temperaturas) / len(temperaturas):.2f}°C")
    print(f"   Mínima: {min(temperaturas):.2f}°C")
    print(f"   Máxima: {max(temperaturas):.2f}°C")
    
    # Salinidade
    salinidades = [c['salinidade_psu'] for c in coletas]
    print(f"\n🧂 SALINIDADE:")
    print(f"   Média: {sum(salinidades) / len(salinidades):.2f} PSU")
    print(f"   Mínima: {min(salinidades):.2f} PSU")
    print(f"   Máxima: {max(salinidades):.2f} PSU")
    
    # Profundidade
    profundidades = [c['profundidade_m'] for c in coletas]
    print(f"\n🌊 PROFUNDIDADE:")
    print(f"   Média: {sum(profundidades) / len(profundidades):.2f}m")
    print(f"   Mínima: {min(profundidades):.2f}m")
    print(f"   Máxima: {max(profundidades):.2f}m")

def analise_por_especie(coletas):
    """Analisa dados agrupados por espécie"""
    if not coletas:
        return
    
    print("\n" + "="*70)
    print("🌿 ANÁLISE POR ESPÉCIE")
    print("="*70)
    
    # Agrupar por espécie
    especies = {}
    for coleta in coletas:
        especie = coleta['especie']
        if especie not in especies:
            especies[especie] = []
        especies[especie].append(coleta)
    
    # Analisar cada espécie
    for especie, dados in especies.items():
        print(f"\n📌 {especie}")
        print("-" * 70)
        print(f"   Ocorrências: {len(dados)}")
        
        biomassas = [d['biomassa_g'] for d in dados]
        print(f"   Biomassa média: {sum(biomassas) / len(biomassas):.2f}g")
        
        temperaturas = [d['temperatura_c'] for d in dados]
        print(f"   Temperatura média: {sum(temperaturas) / len(temperaturas):.2f}°C")
        
        profundidades = [d['profundidade_m'] for d in dados]
        print(f"   Profundidade média: {sum(profundidades) / len(profundidades):.2f}m")
        
        # Praias onde foi encontrada
        praias = list(set(d['praia'] for d in dados))
        print(f"   Praias: {', '.join(praias)}")

def analise_por_praia(coletas):
    """Analisa dados agrupados por praia"""
    if not coletas:
        return
    
    print("\n" + "="*70)
    print("📍 ANÁLISE POR PRAIA")
    print("="*70)
    
    # Agrupar por praia
    praias = {}
    for coleta in coletas:
        praia = coleta['praia']
        if praia not in praias:
            praias[praia] = []
        praias[praia].append(coleta)
    
    # Analisar cada praia
    for praia, dados in praias.items():
        print(f"\n📌 {praia}")
        print("-" * 70)
        print(f"   Coletas realizadas: {len(dados)}")
        
        # Espécies encontradas
        especies_encontradas = list(set(d['especie'] for d in dados))
        print(f"   Espécies ({len(especies_encontradas)}): {', '.join(especies_encontradas)}")
        
        biomassas = [d['biomassa_g'] for d in dados]
        print(f"   Biomassa total: {sum(biomassas):.2f}g")
        print(f"   Biomassa média: {sum(biomassas) / len(biomassas):.2f}g")
        
        temperaturas = [d['temperatura_c'] for d in dados]
        print(f"   Temperatura média: {sum(temperaturas) / len(temperaturas):.2f}°C")

def filtrar_dados(coletas, criterio, valor):
    """Filtra coletas baseado em um critério"""
    if criterio == 'especie':
        resultado = [c for c in coletas if c['especie'].lower() == valor.lower()]
    elif criterio == 'praia':
        resultado = [c for c in coletas if c['praia'].lower() == valor.lower()]
    elif criterio == 'temperatura_min':
        resultado = [c for c in coletas if c['temperatura_c'] >= float(valor)]
    elif criterio == 'temperatura_max':
        resultado = [c for c in coletas if c['temperatura_c'] <= float(valor)]
    else:
        resultado = coletas
    
    return resultado

def exportar_relatorio(coletas, nome_arquivo='relatorio.txt'):
    """Exporta relatório para arquivo de texto"""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("="*70 + "\n")
        arquivo.write("RELATÓRIO DE ANÁLISE DE COLETAS - LABFICOL/UFSC\n")
        arquivo.write("="*70 + "\n\n")
        
        arquivo.write(f"Total de coletas analisadas: {len(coletas)}\n")
        arquivo.write(f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        
        # Estatísticas gerais
        arquivo.write("-"*70 + "\n")
        arquivo.write("ESTATÍSTICAS GERAIS\n")
        arquivo.write("-"*70 + "\n")
        
        biomassas = [c['biomassa_g'] for c in coletas]
        arquivo.write(f"Biomassa total: {sum(biomassas):.2f}g\n")
        arquivo.write(f"Biomassa média: {sum(biomassas) / len(biomassas):.2f}g\n\n")
        
        # Lista de coletas
        arquivo.write("-"*70 + "\n")
        arquivo.write("LISTA DE COLETAS\n")
        arquivo.write("-"*70 + "\n\n")
        
        for coleta in coletas:
            arquivo.write(f"ID: {coleta['id']} | {coleta['data']}\n")
            arquivo.write(f"Praia: {coleta['praia']}\n")
            arquivo.write(f"Espécie: {coleta['especie']}\n")
            arquivo.write(f"Biomassa: {coleta['biomassa_g']}g | Temp: {coleta['temperatura_c']}°C\n")
            arquivo.write("-"*70 + "\n")
    
    print(f"\n✅ Relatório exportado para '{nome_arquivo}'")

def main():
    """Função principal"""
    print("="*70)
    print("🌊 ANÁLISE DE DADOS DE COLETAS - LABFICOL")
    print("="*70)
    
    # Carregar dados
    coletas = carregar_dados()
    
    if not coletas:
        print("\n⚠️ Não foi possível carregar os dados.")
        return
    
    # Executar análises
    estatisticas_basicas(coletas)
    analise_por_especie(coletas)
    analise_por_praia(coletas)
    
    # Exemplo de filtro
    print("\n" + "="*70)
    print("🔍 EXEMPLO DE FILTRO: Ulva lactuca")
    print("="*70)
    ulva = filtrar_dados(coletas, 'especie', 'Ulva lactuca')
    print(f"\n✅ {len(ulva)} registros de Ulva lactuca encontrados")
    
    # Exportar relatório
    exportar_relatorio(coletas)
    
    print("\n" + "="*70)
    print("✅ ANÁLISE CONCLUÍDA!")
    print("="*70)

if __name__ == "__main__":
    main()
