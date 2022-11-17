function get_cookie(cookie_name) {
    let name = cookie_name + "=";
    let decoded_cookie = decodeURIComponent(document.cookie);
    let ca = decoded_cookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function set_cookie(cookie_name, cookie_value, expire_days) {
    const d = new Date();
    d.setTime(d.getTime() + (expire_days*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cookie_name + "=" + cookie_value + ";" + expires + ";SameSite=lax;path=/";
}

function get_carrito() {
    let carrito = get_cookie("carrito");
    if (!carrito) {
        carrito = "{}";
        set_cookie("carrito", carrito, 30);
    }
    return JSON.parse(carrito);
}

function set_carrito(carrito) {
    set_cookie("carrito", JSON.stringify(carrito), 30);
    update_carrito(carrito);
    if (Object.entries(carrito).length == 0) {
        window.location.reload(true);
    }
}

function update_carrito(carrito) {
    let carrito_elem = document.getElementById('carrito');
    let subtotal_elem = document.getElementById('subtotal');
    if (Object.entries(carrito).length == 0) {
        carrito_elem.classList.add('d-none');
        if (subtotal_elem) {
            subtotal_elem.textContent = '$CLP 0.0';
        }
    } else {
        items = 0;
        subtotal = 0;
        Object.keys(carrito).forEach(item => {
            items += carrito[item]["quantity"];
            if (subtotal_elem){
                subtotal += parseInt(document.getElementById('subtotal' + item).value);
            }
        })
        carrito_elem.classList.remove('d-none');
        carrito_elem.textContent = items;
        if (subtotal_elem) {
            subtotal_elem.textContent = '$CLP ' + subtotal.toFixed(2);
        }
    }
}

function update_price(product, price, change=1) {
    let quantity = document.getElementById('quantity' + product);
    let subtotal = document.getElementById('subtotal' + product);
    quantity.value = parseInt(quantity.value) + change;
    subtotal.value = (parseInt(quantity.value) * price).toFixed(2);
}

function add_to_carrito(product, price=0) {
    let carrito = get_carrito()
    if (product in carrito) {
        carrito[product]["quantity"] += 1;
    } else {
        carrito[product] = {"quantity": 1};
    }
    if (price) {
        update_price(product, price)
    }
    set_carrito(carrito);
}

function remove_from_carrito(product, price=0) {
    let carrito = get_carrito()
    carrito[product]["quantity"] -= 1;
    if (!carrito[product]["quantity"]) {
        delete carrito[product];
        document.getElementById('item' + product).remove();
    } else if (price) {
        update_price(product, price, -1)
    }
    set_carrito(carrito);
}

function add_class(elem_id, elem_class) {
    document.getElementById(elem_id).classList.add(elem_class);
}

function remove_class(elem_id, elem_class) {
    document.getElementById(elem_id).classList.remove(elem_class);
}

function formatear_con_decimales(id){
    let el = document.getElementById(id);
    el.value = parseFloat(el.value).toFixed(2)
}

document.addEventListener("DOMContentLoaded", function(event) {
    update_carrito(get_carrito());
});
