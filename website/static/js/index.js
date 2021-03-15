function deleteProduct(productId) {
    fetch('/delete-product', {
        method: 'POST',
        body: JSON.stringify({ productId: productId }),
    }).then((_res) => {
        window.location.href = "/admin";
    });
}

function addToCart(productId){
    fetch('/add-to-cart',{
        method:'POST',
        body: JSON.stringify({ productId: productId }),
    }).then((_res) => {
        window.location.href = "/cart";
    });
}
