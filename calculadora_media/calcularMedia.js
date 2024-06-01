
function calcularMedia(){
    // Primeiro vamos obter as informações das notas
    let notas = document.querySelectorAll(".notas")
    let soma = 0
    let quantidade = notas.length
    
    (function calcularMedia(){
        notas.forEach(function(notas){
            let valor = parseFloat(notas.value)
            if (isNaN(valor)){
                soma += valor
            }
        });

        let media = soma / quantidade
    
        document.getElementById("").textContent = media
    })
}


