var btn = document.querySelector('#calcular');
var res = document.querySelector('#resultado'); 

btn.addEventListener ("click", function(){
    var base = Number(document.querySelectorAll("input") [0].value)
    var altura = Number(document.querySelectorAll("input")[1].value)
    var perimetro = 2 * (base + altura);
    var area = base * altura
    res.innerHTML = `Perímetro: ${perimetro} <br> Área: ${area}`})