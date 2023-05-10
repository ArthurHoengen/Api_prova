from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)

# listas
materials = []
quantity = []

@app.route('/materials', methods=['GET'])
def get_materials():
    materiais = []
    for id in range(0,len(materials)):
        materiais.append({'id' : id,'name': materials[id], 'qtde': quantity[id]})
    response = jsonify({'materiais' : materiais})
    return response, 200

@app.route('/materials', methods=['POST'])
def new_material():
    request_data = request.get_json()
    material_data = request_data['material']
    
    materials.append(material_data['name'])
    quantity.append(material_data['qtde'])

    return 'CREATED', 201

@app.route('/materials/<int:id>', methods=['GET'])
def get_material_by_id(id):
    if id >=0 and id < len(materials):
        return jsonify({'id' : id,'name': materials[id], 'qtde': quantity[id]})
    
    return 'NOT FOUND', 404

@app.route('/materials/<int:id>', methods=['PUT'])
def update_material_by_id(id):
    request_data = request.get_json()
    material_data = request_data['material']
    
    materials[id] = material_data['name']
    quantity[id] = material_data['qtde']
        
    return 'OK', 200

@app.route('/materials/<int:id>', methods=['DELETE'])
def delete_material_by_id(id):
    materials.pop(id)
    quantity.pop(id)
    
    materiais = []
    for id in range(0,len(materials)):
        materiais.append({'id' : id,'name': materials[id], 'qtde': quantity[id]})
    response = jsonify({'materiais' : materiais})
    return response, 200

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port="5000", debug=True)
