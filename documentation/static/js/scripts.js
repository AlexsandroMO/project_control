
console.log('OK!')



function MessagesCarga(){

    let confirmation = confirm('[Alerta!] - Deseja Realmente Carregar Planilhas?');
    let id_href = document.getElementById('call-pl')
    console.log(id_href)


    if (confirmation == true){
        alert("Atualização de carga será realizada.");
        setTimeout(function() {
        
            window.location.href = 'http://127.0.0.1:8000/CreatePL'
        }, 1000);

    }

    else{
        alert("Ok, as planilhas não serão caerregadas.");
    }

}




function MessagesCotation(){

    let confirmation = confirm('[Alerta!] - Deseja Realmente Carregar Cotação');
    let id_href = document.getElementsByTagName('radio')
    console.log(id_href)
    alert("-------", id_href);


    if (confirmation == true){
        alert("Atualização de carga será realizada.");
        setTimeout(function() {
        
            window.location.href = 'http://127.0.0.1:8000/CreateCota'
        }, 1000);

    }

    else{
        alert("Ok, A planilhas não serão caerregada.");
    }

}

document.getElementById('sidebar').style.display = 'none';

function Mudarestado(el) {
    
    let display = document.getElementById(el).style.display;

    if(display == "none")
        document.getElementById(el).style.display = 'block';
    else
        document.getElementById(el).style.display = 'none';
}



function SendListCheck() {

    //let checked = document.getElementById('selected')
    let checked = document.getElementsByName('_selected_action').value
    console.log(checked)


    for (i=0;i<length(checked);i++){
        alert(i)
    }

    /*    setTimeout(function() {
        
        window.location.href = `http://127.0.0.1:8000/createLD`
    }, 1000); */
    
    

}


function myFunction() {
    var questao = document.forms[0];
    var txt = "";
    var i;
    for (i = 0; i < questao.length; i++) {
        if (questao[i].checked) {
            txt = txt + questao[i].value + " ";
        }
    }
    document.getElementById("selected").value = txt ;
}
