class ShoppingCart {
    constructor(id) {
        this.id = id;
        this.productList = [];
    }

    getId() {
        return this.id;
    }

    getProductList() {
        return this.productList;
    }

    addProduct(product) {
        for(let i = 0; i < this.productList.length; i++) {
            if (product === this.productList[i] || product.getId() === this.productList[i].getId()) {
                this.productList.push(product);
            }
        }

        return this;
    }

    addAjaxProduct(product) {
        $.ajax({
            url: "/shop/add-item-to-cart/",
            method: "POST",
            success: function (data) {
                console.log(data);
            }
        })
    }

    getProduct(productId) {
        for (let i = 0; i < this.productList.length; i++) {
            if (this.productList[i].getId() === parseInt(productId)) {
                return this.productList[i];
            }
        }

        return null;
    }
}

class Product {
    constructor(id) {
        this.id = id;
    }

    getId() {
        return this.id;
    }
}