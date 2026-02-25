const PessoaController = require('./PessoaController');

module.exports = (app, PessoaController) => {
    app.post('/pessoa', PessoaController.post);
    app.put('/pessoa', PessoaController.put);
    app.delete('/pessoa', PessoaController.delete);
    app.get('/pessoa', PessoaController.get);    
    app.get('/pessoa/:id', PessoaController.getById);
};