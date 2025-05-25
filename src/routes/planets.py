from flask import Blueprint, request, jsonify
from models import db, Planets

bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@bp.route('/', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

@bp.route('/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "El planeta no fue localizado"}), 404
    
    return jsonify({"success": "El planeta fue localizado"}, planet.serialize()), 200

@bp.route('/', methods=['POST'])
def create_planet():
    data = request.get_json()

    if not data.get('name_planet'):
        return jsonify({"error": "El campo name es ogligatorio"}), 400
    if not data.get('diameter'):
        return jsonify({"error": "El campo diameter es ogligatorio"}), 400
    if not data.get('gravity'):
        return jsonify({"error": "El campo gravity es ogligatorio"}), 400

    new_planet = Planets(
            name_planet=data.get('name_planet'),
            diameter=data.get('diameter'),
            gravity=data.get('gravity')
    )

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"success": "A new planet has been created", "data": new_planet.serialize()}), 201

@bp.route('/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "El planeta no fue localizado"}), 404

    data = request.get_json()

    if 'name_planet' in data:
        planet.name_planet = data['name_planet']
    if 'diameter' in data:
        planet.diameter = data['diameter']
    if 'gravity' in data:
        planet.gravity = data['gravity']

    db.session.commit()

    return jsonify(planet.serialize()), 200


@bp.route('/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "El planeta no fue localizado"}), 404
    
    db.session.delete(planet)
    db.session.commit()

    return jsonify({"msg": "El planeta fue eliminado"}), 200