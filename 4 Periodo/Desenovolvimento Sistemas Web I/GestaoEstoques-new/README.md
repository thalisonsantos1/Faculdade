# SIS WEB I – Gestão de Estoques

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.105-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Desenvolvimento de Sistemas WEB I  
Atividade Prática II – Gestão de Estoques  
Prof. Alysson Naves, Ph.D.  
27 de setembro de 2025  

---

## Contexto

Partindo de um projeto FastAPI com Categoria e Produto funcionando, este trabalho foca na **gestão de estoques**.  
O objetivo é consolidar regras de negócio reais de estoque por meio de entradas e saídas registradas como movimentações.  

Projeto base: [SIS-WEB1-2025-2](https://github.com/alyssonnaves/SIS-WEB1-2025-2)

---

## Objetivos

- Registrar movimentações de estoque (ENTRADA/SAIDA).  
- Calcular saldo por produto e impedir saldo negativo.  
- Definir estoque mínimo e listar produtos abaixo do mínimo.  
- Disponibilizar operações compostas: venda, devolução e ajuste.  
- Fornecer relatórios simples: extrato e resumo de saldos.

---

## Etapas do Trabalho

### Etapa 1 — Modelagem e Rotas Básicas

**Modelos:**

- **Produto:** adicionar `estoque_minimo` (int ≥ 0) e `ativo` (bool).  
- **EstoqueMovimento:** `id`, `produto_id`, `tipo` (ENTRADA|SAIDA), `quantidade` > 0, `motivo`, `criado_em`.

**Rotas:**

- `POST /api/v1/estoque/movimentos` → criar movimento.  
- `GET /api/v1/estoque/saldo/{produto_id}` → saldo atual.

**Regras:** validar produto e quantidade; para SAIDA, preparar verificação de saldo na Etapa 2.

---

### Etapa 2 — Regras de Saldo e Estoque Mínimo

- **Cálculo:** `saldo = somatório(ENTRADA) − somatório(SAIDA)`  
- **Bloqueio de saldo negativo:** parâmetro global (`ALLOW_NEGATIVE_STOCK=false`)  
- **Alertas:** `GET /api/v1/produtos/abaixo-minimo`

---

### Etapa 3 — Operações Compostas

- `POST /api/v1/estoque/venda` → registra SAIDA (motivo: “venda”).  
- `POST /api/v1/estoque/devolucao` → registra ENTRADA (motivo: “devolucao”).  
- `POST /api/v1/estoque/ajuste` → ENTRADA/SAIDA com motivo obrigatório.

---

### Etapa 4 — Relatórios e Consultas

- `GET /api/v1/estoque/extrato/{produto_id}?limit&offset` → últimos movimentos.  
- `GET /api/v1/estoque/resumo` → `produto_id`, `nome`, `saldo`, `estoque_minimo`, `abaixo_minimo`.

---

## Schemas sugeridos

- **EstoqueMovimentoCreate:** `{produto_id, tipo, quantidade, motivo?}`  
- **EstoqueMovimentoOut:** `{id, produto_id, tipo, quantidade, motivo, criado_em}`  
- **SaldoOut:** `{produto_id, saldo}`  
- **ResumoEstoqueOut:** `{produto_id, nome, saldo, estoque_minimo, abaixo_minimo}`

---

## Boas práticas

- Calcular saldo sempre a partir das movimentações (não editar `saldo` diretamente).  
- Impedir saldo negativo (ou permitir via configuração documentada).  
- Usar `response_model` em todas as rotas e mensagens de erro objetivas.  
- No SQLite, garantir `PRAGMA foreign_keys=ON` na conexão.

---

## Como executar a aplicação

1. Criar um ambiente virtual:

```bash
python -m venv venv
