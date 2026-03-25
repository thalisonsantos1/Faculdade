async function connect() {
    if (global.connection
        && global.connection.state !== 'disconnected') 
        return global.connection;
    
    const mysql = require('mysql2/promise');
    const connection = await mysql.createConnection(
        {
            host: '54.91.193.137', user: 'libertas',
            password: '123456', database: 'libertas5per'

        }
    );
    console.log ("Conectou no MySQL!");
    global.connection = connection;
    return connection;
}

function validateEmail(email) {
    // Aceita qualquer string não vazia com pelo menos um caractere
    // Mais flexível para dados legados
    return email && email.trim().length > 0;
}

exports.get = async (req, res, next) => {
    //res.status(200).send('Rota GET!');
    const conn = await connect();
    const [rows] = await conn.query('SELECT idpessoa, nome, telefone, email FROM pessoa');
    res.status(200).json(rows);
}

exports.post = async(req, res, next) => {
    try {
        const conn = await connect();
        let {nome, telefone, email} = req.body;
        
        if (!nome || !telefone || !email) {
            return res.status(400).json({resultado: false, mensagem: 'Nome, telefone e email são obrigatórios'});
        }
        
        if (!validateEmail(email)) {
            return res.status(400).json({resultado: false, mensagem: 'Email inválido'});
        }
        
        const sql = 'INSERT INTO pessoa (nome, telefone, email) VALUES (?, ?, ?)';
        await conn.query(sql, [nome, telefone, email]);
        res.status(201).json({resultado: true, mensagem: 'Pessoa inserida com sucesso'});
    } catch (error) {
        res.status(500).json({resultado: false, mensagem: error.message});
    }
};

exports.put = async(req, res, next) => {
    try {
        const conn = await connect();
        let id = req.params.id;
        let {nome, telefone, email} = req.body;
        
        console.log("PUT recebido - ID:", id, "Nome:", nome, "Telefone:", telefone, "Email:", email);
        
        if (!nome || !telefone || !email) {
            console.log("Validação falhou - campos vazios");
            return res.status(400).json({resultado: false, mensagem: 'Nome, telefone e email são obrigatórios'});
        }
        
        if (!validateEmail(email)) {
            console.log("Email inválido:", email);
            return res.status(400).json({resultado: false, mensagem: 'Email inválido'});
        }
        
        const sql = 'UPDATE pessoa SET nome = ?, telefone = ?, email = ? WHERE idpessoa = ?';
        const [result] = await conn.query(sql, [nome, telefone, email, id]);
        
        console.log("Atualização executada - Linhas afetadas:", result.affectedRows);
        
        if (result.affectedRows === 0) {
            return res.status(404).json({resultado: false, mensagem: 'Pessoa não encontrada'});
        }
        
        res.status(200).json({resultado: true, mensagem: 'Pessoa atualizada com sucesso'});
    } catch (error) {
        console.error("Erro no PUT:", error);
        res.status(500).json({resultado: false, mensagem: error.message});
    }
};

exports.delete = async(req, res, next) => {
    try {
        const conn = await connect();
        let id = req.params.id;
        
        const sql = 'DELETE FROM pessoa WHERE idpessoa = ?';
        const [result] = await conn.query(sql, [id]);
        
        if (result.affectedRows === 0) {
            return res.status(404).json({resultado: false, mensagem: 'Pessoa não encontrada'});
        }
        
        res.status(200).json({resultado: true, mensagem: 'Pessoa deletada com sucesso'});
    } catch (error) {
        res.status(500).json({resultado: false, mensagem: error.message});
    }
};

exports.getById = async (req, res, next) => {
    try {
        let id = req.params.id;
        const conn = await connect();
        const [rows] = await conn.query ('SELECT idpessoa, nome, telefone, email FROM pessoa WHERE idpessoa = ?', [id]);
        if (rows.length > 0) {
            res.status(200).json(rows[0]);
        } else {
            res.status(404).json({resultado: false, mensagem: 'Pessoa não encontrada'});
        }
    } catch (error) {
        res.status(500).json({resultado: false, mensagem: error.message});
    }
};