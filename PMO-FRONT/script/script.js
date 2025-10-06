const hour = () =>{
            const date = new Date();
            let hora = date.getHours()
            let minuto = date.getMinutes()
            let segundo = date.getSeconds()
            document.getElementById("hour").innerHTML=`${hora}:${minuto}:${segundo}`
        }
        setInterval(hour,1000)


/*FUNÇÃO FAZER APARECER INPUT */
function botaodep(){
    document.getElementById("hidden").classList.remove("hidden")
}

//ABRIR MODAL
function abrirModal() {
    document.getElementById("modalProjeto").style.display = "flex";
}

function fecharModal() {
    document.getElementById("modalProjeto").style.display = "none";
}

// Fechar ao clicar fora da modal
window.onclick = function(event) {
    const modal = document.getElementById("modalProjeto");
    if (event.target === modal) {
        modal.style.display = "none";
    }
}


