console.log("HOLA")

const updateBtns = document.getElementsByClassName('update-cart')



for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        const productId = this.dataset.producto
        const action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        
        console.log('USER: ', user)
        if(user === 'AnonymousUser'){
            console.log('No logeado')
        }else{
            actualizarUserOrden(productId, action)
        }
    })
    
}


function actualizarUserOrden(productId, action){
    console.log('Usuario logeado, mandando data...')

    const url = '/actualizar_carro/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken

        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })

}




// Carrito para el invitado

//Funcion para añadir al carro como invitado
function addCookieItem(productId, action) {
    console.log('No estas logeado')

    if (action == 'add'){
        if(carro[productId] === undefined){
            carro[productId] = {'cantidad':1}

        }else{
            carro[productId]['cantidad'] += 1
        }
    }

    if(action == 'eliminar'){
        carro[productId]['cantidad'] - 1

        if(carro[productId]['cantidad'] <= 0){
            console.log('Producto eliminado del carrito')
            delete carro[productId]
        }
    }
    console.log('carro',carro)
    document.cookie = 'carro=' + JSON.stringify(carro) + ";domain=;path=/"

    
}
