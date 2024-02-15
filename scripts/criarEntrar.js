function temConta() {

    let titulo = document.getElementById('titulo')
    titulo.innerHTML = 'Entre com sua conta Flannel'
    let imagem = document.getElementById('img')
    imagem.src = '../images/homem-com-laptop.jpg'

    let botaoEntrar = document.getElementById('tem-conta')
    let botaoCriar = document.getElementById('criar-conta')
    botaoEntrar.style.borderBottomWidth = '4px'
    botaoCriar.style.borderBottomWidth = '1px'

    let telaEntrar = document.getElementById('entrar')
    telaEntrar.style.display = 'block'
    let telaCadastrar = document.getElementById('cadastrar')
    telaCadastrar.style.display = 'none'
}

function criarConta() {

    let titulo = document.getElementById('titulo')
    titulo.innerHTML = 'Crie sua conta Flannel'
    let imagem = document.getElementById('img')
    imagem.src = '../images/homem-apontando-para-cima.jpg'

    let botaoEntrar = document.getElementById('tem-conta')
    let botaoCriar = document.getElementById('criar-conta')
    botaoEntrar.style.borderBottomWidth = '1px'
    botaoCriar.style.borderBottomWidth = '4px'

    let telaEntrar = document.getElementById('entrar')
    telaEntrar.style.display = 'none'
    let telaCadastrar = document.getElementById('cadastrar')
    telaCadastrar.style.display = 'block'
}