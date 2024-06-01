
function calcularMedia(button){

    let row = button.closet('tr')

    // Primeiro vamos obter as informações das notas
    let notas = row.querySelectorAll(".notas")
    let soma = 0
    let quantidade = notas.length
    
    (function calcularMedia(){
        notas.forEach(function(nota){
            let valor = parseFloat(nota.value)
            if (isNaN(valor)){
                soma += valor
            }
        });

        let media = soma / quantidade
    
        document.getElementById("resultado").textContent = media
    })
}


