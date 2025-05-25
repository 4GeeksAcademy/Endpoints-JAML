from flask import Blueprint, request, jsonify
from models import db, Peoples

bp = Blueprint('peoples_bp', __name__, url_prefix='/peoples')

@bp.route('/', methods=['GET'])
def get_all_peoples():
    peoples = Peoples.query.all()
    return jsonify([people.serialize() for people in peoples]), 200

@bp.route('/<int:id_people>', methods=['GET'])
def get_people(id_people):
    people = Peoples.query.get(id_people)

    if not people:
        return jsonify({"msg":"La persona no fue localizada"}), 400
    
    return jsonify({"success":"La persona fue localizada"}, people.serialize()), 200

@bp.route('/', methods=['POST'])
def create_people():
    data = request.get_json()
    new_people = Peoples(
        name_people =data["name_people"]
    )

    db.session.add(new_people)
    db.session.commit()

    return jsonify({"success":"A new people has been created", "data": new_people.serialize()}), 200

@bp.route('/<int:id_people>', methods=['PUT'])
def update_people(id_people):
    people = Peoples.query.get(id_people)
   
    if not people:
        return jsonify({"msg":"La persona no fue localizada"}), 404
   
    data = request.get_json()
   
    if 'name_people' in data:
       people.name_people = data['name_people']

    db.session.commit()

    return jsonify(people.serialize()), 200

@bp.route('/<int:id_people>', methods=['DELETE'])
def delete_people(id_people):
    people = Peoples.query.get(id_people)

    if not people:
        return jsonify({"msg":"La persona no fue localizada"}), 404

    db.session.delete(people)
    db.session.commit()

    return jsonify({"msg":"La persona fue eliminada"}), 200