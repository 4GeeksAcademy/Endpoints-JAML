from flask import Blueprint, request, jsonify
from models import db, Species

bp = Blueprint('species_bp', __name__, url_prefix='/species')

@bp.route('/', methods=['GET'])
def get_all_Species():
    species = Species.query.all()
    return jsonify([specie.serialize() for specie in species]), 200

@bp.route('/<int:id_specie>', methods=['GET'])
def get_specie(id_specie):
    specie = Species.query.get(id_specie)

    if not specie:
        return jsonify({"msg": "La especie no fue localizada"}), 404
    
    return jsonify({"success": "La especie fue localizada"}, specie.serialize()), 200

@bp.route('/', methods=['POST'])
def create_specie():
    data = request.get_json()

    if not data.get('name_specie'):
        return jsonify({"error": "El campo name_specie es obligadorio"}), 400

    new_specie = Species(
        name_specie = data["name_specie"],
        language = data["language"]
    )
    db.session.add(new_specie)
    db.session.commit()

    return jsonify({"success": "A new specie has been created", "data": new_specie.serialize()}), 200 

@bp.route('/<int:id_specie>', methods=['PUT'])
def update_specie(id_specie):
    specie = Species.query.get(id_specie)

    if not specie:
        return jsonify({"error": "La especie no fue localizada"}), 400

    data = request.get_json()
    
    if 'name_specie' in data:
        specie.name_specie = data['name_specie']
    if 'language' in data:
        specie.language = data ['language']

        db.session.commit()

    return jsonify({"msg":"La especie fue actualizada", "data":specie.serialize()}), 200

@bp.route('/<int:id_specie>', methods=['DELETE'])
def delete_specie(id_specie):
    specie = Species.query.get(id_specie)

    if not specie:
        return jsonify({"error": "La especie no fue localizada"}), 400
    
    db.session.delete(specie)
    db.session.commit()

    return jsonify({"msg": "La especie fue eliminada"}), 200