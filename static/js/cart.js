const modify_cart = document.getElementsByClassName("modify-cart")

for (element of modify_cart) {

    element.addEventListener("click", function () {
        product_id = this.dataset.id
        action = this.dataset.action
        console.log("product_id", product_id, "action", action)
        console.log(user)

        if (user === "AnonymousUser") {
            addCookieItem(product_id, action)
        }
        else {
            update_item(product_id, action)
        }
    })
}


const update_item = (product_id, action) => {
    const url = '/update-items/'
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken


        },
        body: JSON.stringify({ "product_id": product_id, "action": action })

    }).then((response) => {

        return response.json()

    }).then((data) => {
        location.reload()
        console.log(data)
    })



}


function addCookieItem(product_id, action) {
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[product_id] == undefined) {
            cart[product_id] = { 'quantity': 1 }

        } else {
            cart[product_id]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[product_id]['quantity'] -= 1

        if (cart[product_id]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[product_id];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload()
}