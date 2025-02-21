var botao = document.querySelectorAll("button");
var botaoClicado = function (){
    alert ("Você clicou o botão " + i);
};
for (var i=0; i < botao.length; i++){
    botao[i].addEventListener('click', botaoClicado);
}