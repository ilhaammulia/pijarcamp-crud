from flask import Blueprint, redirect, url_for, request, render_template, jsonify
from models import Product

views = Blueprint('views', __name__, url_prefix='')

@views.route('/')
def index():
    return redirect(url_for('views.get_products'))

@views.route('/products', methods=['GET'])
def get_products():
    products = Product.find_all()
    return render_template('index.html', products=products)

@views.route('/products', methods=['POST'])
def insert_product():
    product = Product(nama_produk=request.form['nama_produk'], keterangan=request.form['keterangan'], harga=int(request.form['harga']), jumlah=int(request.form['jumlah']))
    product.save()
    return redirect(url_for('views.get_products'))

@views.route('/products/<int:produk_id>', methods=['GET'])
def get_product(produk_id):
    product = Product.find_one(produk_id)
    if product:
        return jsonify({
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock
        })
    return jsonify({})

@views.route('/products/<int:produk_id>', methods=['PUT', 'PATCH'])
def update_product(produk_id):
    product = Product.find_one(produk_id)
    if product:
        product.name = request.form['nama_produk']
        product.description = request.form['keterangan']
        product.price = int(request.form['harga'])
        product.stock = int(request.form['jumlah'])
        product.update()
    return jsonify({
        'error': None
    })

@views.route('/products/<int:produk_id>', methods=['DELETE'])
def delete_product(produk_id):
    product = Product.find_one(produk_id)
    if product:
        Product.delete(product.id)
    return jsonify({
        'error': None
    })