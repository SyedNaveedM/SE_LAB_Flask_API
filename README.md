# Product Inventory REST API  

This project implements a simple **Product Inventory REST API** using **Flask**. It demonstrates REST principles by providing endpoints to **create, read, update, and delete (CRUD)** products in an inventory system.  

## Features
- **GET** → Retrieve all products or a single product by ID.  
- **POST** → Add a new product to the inventory.  
- **PUT** → Update details (name, price, quantity) of an existing product.  
- **DELETE** → Remove a product by ID.  
- Data is exchanged in **JSON format** for consistency.  

## Endpoints

| Method | Endpoint              | Description                       |
|--------|------------------------|-----------------------------------|
| GET    | `/products`            | Get all products                  |
| GET    | `/products/<id>`       | Get product by ID                 |
| POST   | `/products`            | Add a new product                 |
| PUT    | `/products/<id>`       | Update an existing product        |
| DELETE | `/products/<id>`       | Delete a product by ID            |
