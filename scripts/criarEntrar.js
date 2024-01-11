function temConta() {

    var titulo = document.getElementById('titulo')
    titulo.innerHTML = 'Entre com sua conta na XXXX.'

    var botaoEntrar = document.getElementById('tem-conta')
    var botaoCriar = document.getElementById('criar-conta')
    botaoEntrar.style.borderBottomWidth = '4px'
    botaoCriar.style.borderBottomWidth = '1px'

    var telaEntrar = document.getElementById('entrar')
    telaEntrar.style.display = 'block'
    var telaCadastrar = document.getElementById('cadastrar')
    telaCadastrar.style.display = 'none'
}

function criarConta() {

    var titulo = document.getElementById('titulo')
    titulo.innerHTML = 'Crie sua conta na XXXX.'

    var botaoEntrar = document.getElementById('tem-conta')
    var botaoCriar = document.getElementById('criar-conta')
    botaoEntrar.style.borderBottomWidth = '1px'
    botaoCriar.style.borderBottomWidth = '4px'

    var telaEntrar = document.getElementById('entrar')
    telaEntrar.style.display = 'none'
    var telaCadastrar = document.getElementById('cadastrar')
    telaCadastrar.style.display = 'block'
}