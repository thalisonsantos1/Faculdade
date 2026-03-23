const PessoaRoute = require('./pessoaRoute');
const PessoaController = require('./pessoaController');

module.exports = (app) => {
    PessoaRoute(app, PessoaController)
}