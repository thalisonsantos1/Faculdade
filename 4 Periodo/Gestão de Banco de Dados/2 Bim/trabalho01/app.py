from flask import Flask, render_template, request, jsonify
from database import conectar
from datetime import datetime

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# ========== CLIENTES ==========
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cliente_id, nome, telefone, email FROM clientes ORDER BY nome")
            clientes = cursor.fetchall()
            resultado = []
            for cliente in clientes:
                resultado.append({
                    'id': cliente[0],
                    'nome': cliente[1],
                    'telefone': cliente[2],
                    'email': cliente[3]
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/clientes', methods=['POST'])
def add_cliente():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s) RETURNING cliente_id"
            cursor.execute(sql, (data['nome'], data['telefone'], data['email']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE clientes SET nome = %s, telefone = %s, email = %s WHERE cliente_id = %s"
            cursor.execute(sql, (data['nome'], data['telefone'], data['email'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE cliente_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== FUNCIONÁRIOS ==========
@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT funcionario_id, nome, cargo, salario FROM funcionarios ORDER BY nome")
            funcionarios = cursor.fetchall()
            resultado = []
            for func in funcionarios:
                resultado.append({
                    'id': func[0],
                    'nome': func[1],
                    'cargo': func[2],
                    'salario': float(func[3])
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/funcionarios', methods=['POST'])
def add_funcionario():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s) RETURNING funcionario_id"
            cursor.execute(sql, (data['nome'], data['cargo'], data['salario']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/funcionarios/<int:id>', methods=['PUT'])
def update_funcionario(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE funcionarios SET nome = %s, cargo = %s, salario = %s WHERE funcionario_id = %s"
            cursor.execute(sql, (data['nome'], data['cargo'], data['salario'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/funcionarios/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM funcionarios WHERE funcionario_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== SERVIÇOS ==========
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/api/servicos', methods=['GET'])
def get_servicos():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT servico_id, descricao, preco FROM servicos ORDER BY descricao")
            servicos = cursor.fetchall()
            resultado = []
            for servico in servicos:
                resultado.append({
                    'id': servico[0],
                    'descricao': servico[1],
                    'preco': float(servico[2])
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/servicos', methods=['POST'])
def add_servico():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO servicos (descricao, preco) VALUES (%s, %s) RETURNING servico_id"
            cursor.execute(sql, (data['descricao'], data['preco']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/servicos/<int:id>', methods=['PUT'])
def update_servico(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE servicos SET descricao = %s, preco = %s WHERE servico_id = %s"
            cursor.execute(sql, (data['descricao'], data['preco'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/servicos/<int:id>', methods=['DELETE'])
def delete_servico(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM servicos WHERE servico_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== PRODUTOS ==========
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT produto_id, nome, preco, estoque FROM produtos ORDER BY nome")
            produtos = cursor.fetchall()
            resultado = []
            for produto in produtos:
                resultado.append({
                    'id': produto[0],
                    'nome': produto[1],
                    'preco': float(produto[2]),
                    'estoque': produto[3]
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/produtos', methods=['POST'])
def add_produto():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s) RETURNING produto_id"
            cursor.execute(sql, (data['nome'], data['preco'], data['estoque']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE produtos SET nome = %s, preco = %s, estoque = %s WHERE produto_id = %s"
            cursor.execute(sql, (data['nome'], data['preco'], data['estoque'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM produtos WHERE produto_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== PETS ==========
@app.route('/pets')
def pets():
    return render_template('pets.html')

@app.route('/api/pets', methods=['GET'])
def get_pets():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT p.pet_id, p.nome, p.especie, p.raca, p.data_nascimento, p.cliente_id, c.nome as cliente_nome 
                FROM pets p 
                LEFT JOIN clientes c ON p.cliente_id = c.cliente_id 
                ORDER BY p.nome
            """)
            pets = cursor.fetchall()
            resultado = []
            for pet in pets:
                resultado.append({
                    'id': pet[0],
                    'nome': pet[1],
                    'especie': pet[2],
                    'raca': pet[3],
                    'data_nascimento': pet[4].strftime('%Y-%m-%d') if pet[4] else None,
                    'cliente_id': pet[5],
                    'cliente_nome': pet[6]
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/clientes/simples', methods=['GET'])
def get_clientes_simples():
    """Para usar no dropdown de pets"""
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cliente_id, nome FROM clientes ORDER BY nome")
            clientes = cursor.fetchall()
            resultado = [{'id': c[0], 'nome': c[1]} for c in clientes]
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/pets', methods=['POST'])
def add_pet():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO pets (nome, especie, raca, data_nascimento, cliente_id) VALUES (%s, %s, %s, %s, %s) RETURNING pet_id"
            cursor.execute(sql, (data['nome'], data['especie'], data['raca'], data['data_nascimento'], data['cliente_id']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE pets SET nome = %s, especie = %s, raca = %s, data_nascimento = %s, cliente_id = %s WHERE pet_id = %s"
            cursor.execute(sql, (data['nome'], data['especie'], data['raca'], data['data_nascimento'], data['cliente_id'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM pets WHERE pet_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== ATENDIMENTOS ==========
@app.route('/atendimentos')
def atendimentos():
    return render_template('atendimentos.html')

@app.route('/api/atendimentos', methods=['GET'])
def get_atendimentos():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT a.atendimento_id, a.data_atendimento, a.pet_id, a.funcionario_id, a.servico_id,
                       p.nome as pet_nome, f.nome as funcionario_nome, s.descricao as servico_descricao
                FROM atendimentos a
                LEFT JOIN pets p ON a.pet_id = p.pet_id
                LEFT JOIN funcionarios f ON a.funcionario_id = f.funcionario_id
                LEFT JOIN servicos s ON a.servico_id = s.servico_id
                ORDER BY a.data_atendimento DESC
            """)
            atendimentos = cursor.fetchall()
            resultado = []
            for atend in atendimentos:
                resultado.append({
                    'id': atend[0],
                    'data_atendimento': atend[1].strftime('%Y-%m-%d') if atend[1] else None,
                    'pet_id': atend[2],
                    'funcionario_id': atend[3],
                    'servico_id': atend[4],
                    'pet_nome': atend[5],
                    'funcionario_nome': atend[6],
                    'servico_descricao': atend[7]
                })
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/atendimentos', methods=['POST'])
def add_atendimento():
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO atendimentos (data_atendimento, pet_id, funcionario_id, servico_id) VALUES (%s, %s, %s, %s) RETURNING atendimento_id"
            cursor.execute(sql, (data['data_atendimento'], data['pet_id'], data['funcionario_id'], data['servico_id']))
            id_novo = cursor.fetchone()[0]
            conn.commit()
            return jsonify({'success': True, 'id': id_novo})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/atendimentos/<int:id>', methods=['PUT'])
def update_atendimento(id):
    data = request.json
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE atendimentos SET data_atendimento = %s, pet_id = %s, funcionario_id = %s, servico_id = %s WHERE atendimento_id = %s"
            cursor.execute(sql, (data['data_atendimento'], data['pet_id'], data['funcionario_id'], data['servico_id'], id))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/atendimentos/<int:id>', methods=['DELETE'])
def delete_atendimento(id):
    conn = conectar()
    if conn is None:
        return jsonify({'error': 'Erro de conexão'})
    
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM atendimentos WHERE atendimento_id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)})
    finally:
        conn.close()

# ========== DROPDOWNS PARA ATENDIMENTOS ==========
@app.route('/api/pets/simples', methods=['GET'])
def get_pets_simples():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT pet_id, nome FROM pets ORDER BY nome")
            pets = cursor.fetchall()
            resultado = [{'id': p[0], 'nome': p[1]} for p in pets]
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/funcionarios/simples', methods=['GET'])
def get_funcionarios_simples():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT funcionario_id, nome FROM funcionarios ORDER BY nome")
            funcionarios = cursor.fetchall()
            resultado = [{'id': f[0], 'nome': f[1]} for f in funcionarios]
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@app.route('/api/servicos/simples', methods=['GET'])
def get_servicos_simples():
    conn = conectar()
    if conn is None:
        return jsonify([])
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT servico_id, descricao FROM servicos ORDER BY descricao")
            servicos = cursor.fetchall()
            resultado = [{'id': s[0], 'descricao': s[1]} for s in servicos]
            return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)