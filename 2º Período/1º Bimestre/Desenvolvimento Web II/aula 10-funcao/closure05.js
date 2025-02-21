var botao = document.querySelectorAll("button");
function funcaoAuxiliar(j){
    return function(){
        alert ("Você clicou o botão " + j);        
    }
};
for (var i=0; i < botao.length; i++){
    botao[i].addEventListener('click', funcaoAuxiliar(i));
}