(function(){
    const btn_eliminacion = document.querySelectorAll(".btneliminacion");


btn_eliminacion.forEach(btn => {
    btn.addEventListener('click', (e)=>{

        const confirmacion  = confirm('seguro de eliminar el curso');


        if (!confirmacion){

         e.preventDefault();
        }



    });
})
})();