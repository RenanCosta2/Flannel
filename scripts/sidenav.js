
function bordaNavegacao(){
    let nomePagina = window.location.pathname
    nomePagina = nomePagina.split('/')
    nomePagina = nomePagina.pop().replace('.html', '')

    let paginaAtual = document.getElementById(nomePagina)

    paginaAtual.style.borderLeft = '4px solid #96E40E'

}