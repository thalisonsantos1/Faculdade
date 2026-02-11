const UsuarioRoute = require('./UsuarioRoute');
const UsuarioController = require('./UsuarioController');

module.exports = (app) => {
    UsuarioRoute(app, UsuarioController);
}