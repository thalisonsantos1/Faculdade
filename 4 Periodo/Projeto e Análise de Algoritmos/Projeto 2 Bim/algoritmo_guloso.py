"""Primeiro, pensei na lógica:

    1 - Ordenar as tarefas pela penalidade (maior primeiro)

    2 - Para cada tarefa, tentar colocar no último slot livre antes do deadline

    3 - Se não conseguir slot, paga a penalidade"""


def escalonamento_guloso(tarefas):
    """
    Algoritmo Guloso para Escalonamento com Deadlines
    Decisão gananciosa: escolher sempre a tarefa com MAIOR penalidade primeiro
    """
    
    # PASSO 1: Ordenar tarefas por penalidade decrescente (decisão gananciosa!)
    # Quanto maior a penalidade, mais importante agendar essa tarefa
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x[2], reverse=True) #essa é a decisão gananciosa, pois estamos sempre escolhendo a tarefa com maior penalidade primeiro
    # isso se torna ganancioso porque não pensa nas consequências futuras, somente no ganho imediato.
    
    # Achar o máximo deadline para saber quantos slots precisamos
    max_deadline = max(tarefa[1] for tarefa in tarefas)
    
    # Criar array de slots (0 = livre, 1 = ocupado)
    slots = [0] * (max_deadline + 1)
    slots[0] = -1  # slot 0 não usado (deadlines começam em 1)
    
    # Listas para guardar resultados
    agendadas = []
    penalidade_total = 0
    
    # PASSO 2: Para cada tarefa, tentar agendar no último slot disponível
    for tarefa in tarefas_ordenadas:
        nome, deadline, penalidade = tarefa
        agendou = False
        
        # Tentar colocar no último slot possível (do deadline pra trás)
        for slot in range(deadline, 0, -1):
            if slots[slot] == 0:  # Slot livre!
                slots[slot] = 1
                agendadas.append((nome, slot))
                agendou = True
                break
        
        # Se não conseguiu agendar, paga penalidade
        if not agendou:
            penalidade_total += penalidade
            agendadas.append((nome, "Não agendada"))
    
    return agendadas, penalidade_total

# CASOS DE TESTE (comentados para entender)

print("=== CASO DE TESTE 1 ===")
# Tarefas: (nome, deadline, penalidade)
tarefas1 = [
    ("T1", 2, 60),
    ("T2", 1, 100), 
    ("T3", 3, 20),
    ("T4", 2, 40)
]

print("Tarefas originais:")
for tarefa in tarefas1:
    print(f"  {tarefa[0]}: deadline={tarefa[1]}, penalidade={tarefa[2]}")

agendadas, penalidade = escalonamento_guloso(tarefas1)

print("\nResultado do agendamento guloso:")
for nome, slot in agendadas:
    print(f"  {nome} → slot {slot}")

print(f"Penalidade total: {penalidade}")
print("Esperado: T2(slot1), T1(slot2), T3(slot3), T4(não agendada), Penalidade=40")

print("\n" + "="*50)

print("=== CASO DE TESTE 2 ===")
# Outro exemplo para testar
tarefas2 = [
    ("A", 1, 10),
    ("B", 1, 20),  # B tem penalidade maior que A
    ("C", 2, 5)
]

print("Tarefas originais:")
for tarefa in tarefas2:
    print(f"  {tarefa[0]}: deadline={tarefa[1]}, penalidade={tarefa[2]}")

agendadas2, penalidade2 = escalonamento_guloso(tarefas2)

print("\nResultado do agendamento guloso:")
for nome, slot in agendadas2:
    print(f"  {nome} → slot {slot}")

print(f"Penalidade total: {penalidade2}")
print("Esperado: B(slot1), C(slot2), A(não agendada), Penalidade=10")