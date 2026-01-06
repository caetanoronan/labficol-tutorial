"""
Sistema de Cadastro de Coletas - LABFICOL
==========================================

Exemplo prático do módulo 1-Python-Essencial
Sistema simples para cadastrar coletas de macroalgas

Autor: LABFICOL/UFSC
"""

# Lista para armazenar coletas
coletas = []

def menu_principal():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("🌊 SISTEMA DE CADASTRO DE COLETAS - LABFICOL")
    print("="*50)
    print("1. Cadastrar nova coleta")
    print("2. Listar todas as coletas")
    print("3. Buscar por espécie")
    print("4. Estatísticas")
    print("5. Sair")
    print("="*50)

def cadastrar_coleta():
    """Cadastra uma nova coleta"""
    print("\n📝 CADASTRAR NOVA COLETA")
    print("-" * 40)
    
    # Coletar informações
    id_coleta = len(coletas) + 1
    data = input("Data (DD/MM/AAAA): ")
    praia = input("Praia: ")
    especie = input("Espécie: ")
    
    # Validar entrada numérica
    while True:
        try:
            biomassa = float(input("Biomassa (gramas): "))
            temperatura = float(input("Temperatura (°C): "))
            salinidade = float(input("Salinidade (PSU): "))
            profundidade = float(input("Profundidade (metros): "))
            break
        except ValueError:
            print("❌ Erro! Digite apenas números para os valores numéricos.")
    
    # Criar dicionário da coleta
    coleta = {
        'id': id_coleta,
        'data': data,
        'praia': praia,
        'especie': especie,
        'biomassa_g': biomassa,
        'temperatura_c': temperatura,
        'salinidade_psu': salinidade,
        'profundidade_m': profundidade
    }
    
    # Adicionar à lista
    coletas.append(coleta)
    
    print(f"\n✅ Coleta #{id_coleta} cadastrada com sucesso!")

def listar_coletas():
    """Lista todas as coletas cadastradas"""
    if not coletas:
        print("\n⚠️ Nenhuma coleta cadastrada ainda.")
        return
    
    print(f"\n📊 TOTAL DE COLETAS: {len(coletas)}")
    print("="*80)
    
    for coleta in coletas:
        print(f"\n🔹 Coleta #{coleta['id']}")
        print(f"   Data: {coleta['data']}")
        print(f"   Praia: {coleta['praia']}")
        print(f"   Espécie: {coleta['especie']}")
        print(f"   Biomassa: {coleta['biomassa_g']}g")
        print(f"   Temperatura: {coleta['temperatura_c']}°C")
        print(f"   Salinidade: {coleta['salinidade_psu']} PSU")
        print(f"   Profundidade: {coleta['profundidade_m']}m")
        print("-" * 80)

def buscar_por_especie():
    """Busca coletas por espécie"""
    if not coletas:
        print("\n⚠️ Nenhuma coleta cadastrada ainda.")
        return
    
    especie_busca = input("\n🔍 Digite o nome da espécie: ")
    
    resultados = [c for c in coletas if especie_busca.lower() in c['especie'].lower()]
    
    if not resultados:
        print(f"\n❌ Nenhuma coleta encontrada para '{especie_busca}'")
        return
    
    print(f"\n✅ {len(resultados)} coleta(s) encontrada(s):")
    print("="*80)
    
    for coleta in resultados:
        print(f"\n🔹 Coleta #{coleta['id']} - {coleta['data']}")
        print(f"   Praia: {coleta['praia']}")
        print(f"   Biomassa: {coleta['biomassa_g']}g")
        print(f"   Temperatura: {coleta['temperatura_c']}°C")

def calcular_estatisticas():
    """Calcula estatísticas das coletas"""
    if not coletas:
        print("\n⚠️ Nenhuma coleta cadastrada ainda.")
        return
    
    # Calcular médias
    biomassa_total = sum(c['biomassa_g'] for c in coletas)
    biomassa_media = biomassa_total / len(coletas)
    
    temp_media = sum(c['temperatura_c'] for c in coletas) / len(coletas)
    sal_media = sum(c['salinidade_psu'] for c in coletas) / len(coletas)
    prof_media = sum(c['profundidade_m'] for c in coletas) / len(coletas)
    
    # Contar espécies
    especies = {}
    praias = {}
    
    for coleta in coletas:
        # Contar espécies
        if coleta['especie'] in especies:
            especies[coleta['especie']] += 1
        else:
            especies[coleta['especie']] = 1
        
        # Contar praias
        if coleta['praia'] in praias:
            praias[coleta['praia']] += 1
        else:
            praias[coleta['praia']] = 1
    
    # Exibir estatísticas
    print("\n" + "="*60)
    print("📈 ESTATÍSTICAS GERAIS")
    print("="*60)
    print(f"\n📊 Total de coletas: {len(coletas)}")
    print(f"🌿 Espécies diferentes: {len(especies)}")
    print(f"📍 Praias monitoradas: {len(praias)}")
    
    print("\n" + "-"*60)
    print("⚖️  MÉDIAS")
    print("-"*60)
    print(f"Biomassa média: {biomassa_media:.2f}g (Total: {biomassa_total:.2f}g)")
    print(f"Temperatura média: {temp_media:.2f}°C")
    print(f"Salinidade média: {sal_media:.2f} PSU")
    print(f"Profundidade média: {prof_media:.2f}m")
    
    print("\n" + "-"*60)
    print("🌿 RANKING DE ESPÉCIES")
    print("-"*60)
    especies_ordenadas = sorted(especies.items(), key=lambda x: x[1], reverse=True)
    for especie, count in especies_ordenadas:
        porcentagem = (count / len(coletas)) * 100
        print(f"{especie}: {count} coletas ({porcentagem:.1f}%)")
    
    print("\n" + "-"*60)
    print("📍 RANKING DE PRAIAS")
    print("-"*60)
    praias_ordenadas = sorted(praias.items(), key=lambda x: x[1], reverse=True)
    for praia, count in praias_ordenadas:
        porcentagem = (count / len(coletas)) * 100
        print(f"{praia}: {count} coletas ({porcentagem:.1f}%)")

def executar_sistema():
    """Loop principal do sistema"""
    print("\n✨ Bem-vindo ao Sistema de Cadastro de Coletas!")
    
    while True:
        menu_principal()
        
        try:
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                cadastrar_coleta()
            elif opcao == '2':
                listar_coletas()
            elif opcao == '3':
                buscar_por_especie()
            elif opcao == '4':
                calcular_estatisticas()
            elif opcao == '5':
                print("\n👋 Obrigado por usar o sistema!")
                print("🌊 LABFICOL/UFSC\n")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")

# Executar o sistema
if __name__ == "__main__":
    executar_sistema()
