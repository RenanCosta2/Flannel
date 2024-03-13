function visualizacaoAbaTermos(){
    
    let termosDeUso = document.getElementById('termos-de-uso')
    let opacidade = document.getElementById('opacidade')
    if (termosDeUso.style.display == 'block') {
        termosDeUso.style.display = 'none'
        opacidade.style.display = 'none'
    } else{
        termosDeUso.style.display = 'block'
        opacidade.style.display = 'block'
    }
}

function visualizacaoAbaPrivacidade(){
    
    let politicaPrivacidade = document.getElementById('politica-privacidade')
    let opacidade = document.getElementById('opacidade')
    if (politicaPrivacidade.style.display == 'block') {
        politicaPrivacidade.style.display = 'none'
        opacidade.style.display = 'none'
    } else{
        politicaPrivacidade.style.display = 'block'
        opacidade.style.display = 'block'
    }
}