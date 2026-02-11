module.exports = (app, UsuarioController) => {
    app.get('/usuario', UsuarioController.get);    
};