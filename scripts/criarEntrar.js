function telasContas() {

    let titulo = document.getElementById('titulo')
    let imagem = document.getElementById('img')

    let botaoEntrar = document.getElementById('tem-conta')
    let botaoCriar = document.getElementById('criar-conta')

    let telaEntrar = document.getElementById('entrar')
    let telaCadastrar = document.getElementById('cadastrar')

    if (telaEntrar.style.display == 'none') {
        
        titulo.innerHTML = 'Entre com sua conta Flannel'
        imagem.src = '../images/pessoas/homem-com-laptop.svg'
        botaoEntrar.style.borderBottomWidth = '4px'
        botaoCriar.style.borderBottomWidth = '1px'
        telaEntrar.style.display = 'block'
        telaCadastrar.style.display = 'none'
    } else{
        titulo.innerHTML = 'Crie sua conta Flannel'
        imagem.src = '../images/pessoas/homem-apontando-para-cima.svg'
        botaoEntrar.style.borderBottomWidth = '1px'
        botaoCriar.style.borderBottomWidth = '4px'
        telaEntrar.style.display = 'none'
        telaCadastrar.style.display = 'block'
    }
}

function visualizacaoAbaNovaSenha(){
    
    let divNovaSenha = document.getElementById('nova-senha')
    
    let opacidade = document.getElementById('opacidade')
    
    if (divNovaSenha.style.display == 'flex') {
        divNovaSenha.style.display = 'none'
        opacidade.style.display = 'none'
    }else{
        divNovaSenha.style.display = 'flex'
        opacidade.style.display = 'block'
    }
}

function visualizacaoSenha(idInput, olhoOff, olhoOn){

    console.log(idInput)
    let input = document.getElementById(idInput)
    let olho_on = document.getElementById(olhoOn)
    let olho_off = document.getElementById(olhoOff)
    if (input.type === "password") {
        input.type = "text"
        olho_on.style.display = 'block'
        olho_off.style.display = 'none'
    } else{
        input.type = "password"
        olho_on.style.display = 'none'
        olho_off.style.display = 'block'
    }

}