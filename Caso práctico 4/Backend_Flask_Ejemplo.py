from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'tu_string_de_conexión_a_la_base_de_datos'
db = SQLAlchemy(app)

# Modelos de SQLAlchemy (User, Product, Order) aquí...
