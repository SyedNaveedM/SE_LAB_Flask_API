from flask import Flask, jsonify, request

app = Flask(__name__)

# Our database
products = {
    1: {"name": "Laptop", "price": 55000, "quantity": 10},
    2: {"name": "Phone", "price": 20000, "quantity": 25},
    3: {"name": "Headphones", "price": 2000, "quantity": 50}
}


# Gets all the products in the database
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products), 200


# Search for a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


# Add new products to our database
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid request. Provide name, price, and quantity"}), 400
    
    new_id = max(products.keys()) + 1 if products else 1
    products[new_id] = {
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"]
    }
    return jsonify({"message": "Product added successfully", "id": new_id}), 201



# Update a particular products details
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_details(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.get_json()
    product.update({k: v for k, v in data.items() if k in ["name", "price", "quantity"]})
    return jsonify({"message": "Product updated successfully", "product": product}), 200


# Delete a particular product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Deletes a product from the inventory using its ID.
    """
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404
    deleted = products.pop(product_id)
    return jsonify({"message": "Product deleted successfully", "deleted": deleted}), 200


if __name__ == '__main__':
    app.run(debug=True)
