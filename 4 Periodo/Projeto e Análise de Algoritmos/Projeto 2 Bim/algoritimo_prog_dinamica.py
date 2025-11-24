"""A ideia principal:

    - Vamos usar uma tabela DP onde dp[mask] guarda a menor penalidade para um subconjunto de tarefas

    - mask é um número binário que representa quais tarefas já foram consideradas

    - Exemplo: mask = 5 (binário 101) significa que consideramos as tarefas 1 e 3"""

def escalonamento_pd(tarefas):
    """
    Algoritmo de Programação Dinâmica para Escalonamento com Deadlines
    Encontra a solução ÓTIMA (sempre correta)
    
    IDEIA PRINCIPAL:
    - Usamos uma máscara binária para representar subconjuntos de tarefas
    - dp[mask] = menor penalidade para agendar o subconjunto 'mask'
    - Começamos com subconjuntos pequenos e vamos construindo soluções maiores
    """
    
    n = len(tarefas)
    
    # PASSO 1: Criar a tabela DP
    # total_mascaras = 2^n (cada tarefa pode estar incluída ou não)
    total_mascaras = 1 << n  
    dp = [float('inf')] * total_mascaras  # Inicializar com infinito
    
    # CASO BASE: conjunto vazio tem penalidade 0
    dp[0] = 0
    
    # PASSO 2: Preencher a tabela DP
    # Vamos de subconjuntos menores para maiores
    for mask in range(total_mascaras):
        
        # Se não alcançamos este estado, pulamos
        if dp[mask] == float('inf'):
            continue
        
        # Contar quantas tarefas já foram agendadas neste subconjunto
        # Isso nos diz em qual slot estamos (cada tarefa ocupa 1 slot)
        tempo_atual = 0
        for i in range(n):
            if mask & (1 << i):  # Se a tarefa i está no subconjunto
                tempo_atual += 1
        
        # Agora tentamos adicionar cada tarefa que ainda não está no subconjunto
        for i in range(n):
            if not (mask & (1 << i)):  # Se tarefa i NÃO está no subconjunto
                
                # Nova máscara incluindo a tarefa i
                nova_mask = mask | (1 << i)
                
                # Dados da tarefa que queremos adicionar
                nome, deadline, penalidade = tarefas[i]
                
                # Verificar se conseguimos agendar a tarefa i a tempo
                # deadline >= tempo_atual + 1 significa que cabe
                if deadline >= tempo_atual + 1:
                    # CONSEGUIMOS AGENDAR sem penalidade
                    if dp[mask] < dp[nova_mask]:
                        dp[nova_mask] = dp[mask]
                else:
                    # NÃO CONSEGUIMOS AGENDAR, pagamos a penalidade
                    if dp[mask] + penalidade < dp[nova_mask]:
                        dp[nova_mask] = dp[mask] + penalidade
    
    # PASSO 3: A resposta final está no estado com todas as tarefas
    mask_todas_tarefas = total_mascaras - 1
    penalidade_otima = dp[mask_todas_tarefas]
    
    return penalidade_otima, dp

# =============================================================================
# FUNÇÃO PARA MOSTRAR A TABELA DP (PARA ENTENDER MELHOR)
# =============================================================================

def mostrar_tabela_dp_completa(dp, tarefas):
    """
    Mostra a tabela DP completa de forma organizada
    Para ajudar a entender como a programação dinâmica funciona
    """
    n = len(tarefas)
    
    print("\n" + "="*50)
    print("TABELA DP COMPLETA")
    print("="*50)
    
    for mask in range(len(dp)):
        if dp[mask] != float('inf'):
            # Converter a máscara para conjunto de tarefas
            tarefas_no_conjunto = []
            for i in range(n):
                if mask & (1 << i):
                    tarefas_no_conjunto.append(tarefas[i][0])
            
            # Mostrar de forma organizada
            if not tarefas_no_conjunto:
                print(f"mask {bin(mask)[2:].zfill(n)} [ ] → penalidade: {dp[mask]}")
            else:
                print(f"mask {bin(mask)[2:].zfill(n)} {tarefas_no_conjunto} → penalidade: {dp[mask]}")

# =============================================================================
# CASOS DE TESTE ESPECÍFICOS PARA PD
# =============================================================================

def testar_pd():
    """Testa apenas a Programação Dinâmica com casos específicos"""
    
    print("TESTES - PROGRAMAÇÃO DINÂMICA")
    print("=" * 40)
    
    # CASO DE TESTE 1
    print("\n>>> CASO 1: Exemplo das imagens")
    tarefas1 = [
        ("T1", 2, 60),
        ("T2", 1, 100), 
        ("T3", 3, 20),
        ("T4", 2, 40)
    ]
    
    print("Tarefas:")
    for tarefa in tarefas1:
        print(f"  {tarefa[0]}: deadline={tarefa[1]}, penalidade={tarefa[2]}")
    
    penalidade_otima, tabela_dp = escalonamento_pd(tarefas1)
    print(f"\nPenalidade mínima (PD): {penalidade_otima}")
    
    # Mostrar apenas alguns estados importantes da tabela DP
    print("\n--- Estados Importantes da Tabela DP ---")
    n = len(tarefas1)
    masks_importantes = [0, (1 << n) - 1]  # Vazio e todas as tarefas
    
    for mask in masks_importantes:
        if tabela_dp[mask] != float('inf'):
            tarefas_no_conjunto = []
            for i in range(n):
                if mask & (1 << i):
                    tarefas_no_conjunto.append(tarefas1[i][0])
            
            if not tarefas_no_conjunto:
                print(f"Conjunto vazio → Penalidade: {tabela_dp[mask]}")
            else:
                print(f"Todas as tarefas {tarefas_no_conjunto} → Penalidade mínima: {tabela_dp[mask]}")
    
    print("\n" + "=" * 40)
    
    # CASO DE TESTE 2
    print("\n>>> CASO 2: Caso simples")
    tarefas2 = [
        ("A", 1, 10),
        ("B", 1, 20),
        ("C", 2, 5)
    ]
    
    print("Tarefas:")
    for tarefa in tarefas2:
        print(f"  {tarefa[0]}: deadline={tarefa[1]}, penalidade={tarefa[2]}")
    
    penalidade_otima2, tabela_dp2 = escalonamento_pd(tarefas2)
    print(f"\nPenalidade mínima (PD): {penalidade_otima2}")

# =============================================================================
# EXECUTAR OS TESTES
# =============================================================================

if __name__ == "__main__":
    testar_pd()
    
    # Para ver a tabela DP completa de um caso pequeno:
    print("\n" + "="*50)
    print("EXEMPLO DETALHADO - CASO PEQUENO")
    print("="*50)
    
    tarefas_pequenas = [
        ("T1", 1, 10),
        ("T2", 1, 20)
    ]
    
    print("Tarefas:")
    for tarefa in tarefas_pequenas:
        print(f"  {tarefa[0]}: deadline={tarefa[1]}, penalidade={tarefa[2]}")
    
    penalidade, dp = escalonamento_pd(tarefas_pequenas)
    mostrar_tabela_dp_completa(dp, tarefas_pequenas)
    print(f"\nPenalidade mínima final: {penalidade}")



    """    
    1 - dp[mask] - guarda a menor penalidade para cada subconjunto

    2 - Máscara binária - cada bit representa se uma tarefa está incluída

    3 - Preenchimento ordenado - vamos de subconjuntos menores para maiores

    4 - Verificação de deadline - deadline >= tempo_atual + 1

    5 - Resultado final - dp[total_mascaras - 1] tem a resposta ótima"""