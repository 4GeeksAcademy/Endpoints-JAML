from flask import Blueprint, request, jsonify
from models import db, Vehicles

bp = Blueprint('vehicles_bp', __name__, url_prefix='/vehicles')

@bp.route('/', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicles.query.all()
    return jsonify([vehicle.serialize() for vehicle in vehicles]), 200

@bp.route('/<int:id_vehicle>', methods=['GET'])
def get_vehicle(id_vehicle):
    vehicle = Vehicles.query.get(id_vehicle)

    if not vehicle:
         return jsonify({"msg":"El vehiculo no fue localizado"}), 404
    
    return jsonify({"success": "El vehiculo fue localizado"}, vehicle.serialize()), 200

@bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.get_json()

    if not data.get('name_vehicle'):
        return jsonify({"error": "El campo name es ogligatorio"}), 400
    
    new_vehicle = Vehicles (
        name_vehicle = data.get('name_vehicle'),
        passengers = data.get('passengers')
    )

    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify({"success":"A new vehicle has been created","data": new_vehicle.serialize()}), 201

@bp.route('/<int:id_vehicle>', methods=['PUT'])
def update_vehicle(id_vehicle):
    vehicle = Vehicles.query.get(id_vehicle)

    if not vehicle:
        return jsonify({"msg": "El Vehiculo no fue localizado"}), 404
    
    data = request.get_json()

    if 'name_vehicle' in data:
        vehicle.name_vehicle = data['name_vehicle']
    if 'passengers' in data:
        vehicle.passengers = data['passengers']

    db.session.commit()
        
    return jsonify(vehicle.serialize()), 200


@bp.route('/<int:id_vehicle>', methods=['DELETE'])
def delete_vehicle(id_vehicle):
    vehicle = Vehicles.query.get(id_vehicle)

    if not vehicle:
        return jsonify({"msg":"El vehiculo no fue localizado"}), 404
    
    db.session.delete(vehicle)
    db.session.commit()
    
    return jsonify({"msg":"El vehiculo fue eliminado"}), 200