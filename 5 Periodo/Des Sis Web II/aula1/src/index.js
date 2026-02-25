const PessoaRoute = require('./PessoaRoute');
const PessoaController = require('./PessoaController');

module.exports = (app) => {
    PessoaRoute(app, PessoaController)
}