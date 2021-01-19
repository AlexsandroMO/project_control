function marcarTodos(marcardesmarcar){
        $('.marcar').each(function () {
            this.checked = marcardesmarcar;
        });
    }




//document.getElementById('checkboxPrimary1').addEventListener('click', mostrar, false);

function status_checkbox(){
    bt_check = document.getElementById('checkboxPrimary1');
    bt_check.status.checked = true;
    //document.getElementById("imagem-binder").style.display = "none";
    console.log('Foi!')

    }



/* 
    ocultar()
    //mostrar()

    document.getElementById('checkboxPrimary1').addEventListener('click', mostrar, false);
    //document.getElementById('imagem-oculta').addEventListener('click', ocultar, false);

    function ocultar(evt) {
        //alert('foi ocultar!!!')
        document.getElementById("imagem-binder").style.display = "none";
        
    }

    function mostrar(evt) {
        //alert('foi mostrar!!!')
        document.getElementById("imagem-binder").style.display = "block";
        //ocultar(false)
        
    }
 */