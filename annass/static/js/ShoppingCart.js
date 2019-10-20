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

class ProductCategory {
    constructor(name) {
        this.name = name;
        this.products = [];
    }

    addProduct(product) {
        let found = false;
        for (let i = 0; i < this.products.length; i++) {
            if (this.products[i].id === product.id) {
                found = true;
            }
        }

        if (!found) {
            this.products.push(product);
        }

        return this;
    }

    getProducts() {
        return this.products;
    }

    getProduct(productId) {
        for (let i = 0; i < this.products.length; i++) {
            if (this.products[i].id === parseInt(productId)) {
                return this.products[i];
            }
        }

        return null;
    }

    build() {
        let productList = "<div class='product-list' id='" + this.name + "'>";
        for (let i = 0; i < this.products.length; i++) {
            productList += this.products[i].build();
        }

        productList += "</div>";

        $('#products-view').html(productList);

        return this;
    }
}

class Product {
    constructor(id, name, price, description, imageUrl) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
        this.price = price;
    }

    getId() {
        return this.id;
    }

    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
        return this;
    }

    getDescription() {
        return this.description;
    }

    setDescription(description) {
        this.description = description;
        return this;
    }

    getImageUrl() {
        return this.imageUrl;
    }

    setImageUrl(imageUrl) {
        this.imageUrl = imageUrl;
        return this;
    }

    getPrice() {
        return this.price;
    }

    setPrice(price) {
        this.price = price;
        return this;
    }

    build() {
        return "" +
            "<div class='product card'>" +
            "   <div class='product-image'>" +
            "       <img src='" + this.imageUrl + "'>" +
            "   </div>" +
            "   <div class='product-title'>" +
            "       <h3>" + this.name + "</h3>" +
            "   </div>" +
            "   <div class='product-price'>" +
            "       <p>" + this.price + "</p>" +
            "   </div>" +
            "</div>"
    }
}