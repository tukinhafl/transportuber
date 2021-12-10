from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required
from app.models.caminhao_model import CaminhaoModel
from werkzeug.exceptions import NotFound

@jwt_required()
def criar_caminhao(motorista_id: int):
  session = current_app.db.session
  data = request.get_json()

  data['marca'] = data['marca'].title()
  data['modelo'] = data['modelo'].title()
  data['motorista_id'] = motorista_id
  print(data)

  novo_caminhao = CaminhaoModel(**data)

  session.add(novo_caminhao)
  session.commit()

  return jsonify(novo_caminhao.serialize()), 201

@jwt_required()
def listar_caminhoes():
  caminhoes = (CaminhaoModel.query.all())

  lista_caminhoes = [caminhao.serialize() for caminhao in caminhoes]

  return jsonify(lista_caminhoes), 200

@jwt_required()
def atualizar_caminhao(caminhao_id: int):
  try:
    session = current_app.db.session
    caminhao = CaminhaoModel.query.get(caminhao_id)
    data = request.get_json()

    colunas_validas = ["capacidade_de_carga", "placa"]

    for k, v in data.items():
      if k in colunas_validas:
        setattr(caminhao, k, v)
      else:
        return {"error": f"Chave inválida: ({k})"}, 409

    session.add(caminhao)
    session.commit()

    return caminhao.serialize()
  except KeyError as e:
    return {"error": f"Chaves faltantes: {e.args}"}

@jwt_required()
def deletar_caminhao(caminhao_id):
  try:
    caminhao_deletado = CaminhaoModel.query.filter_by(
      id=caminhao_id).first_or_404(description="Caminhão não encontrado")

    current_app.db.session.delete(caminhao_deletado)
    current_app.db.session.commit()

    return "", 204
  except NotFound:
    return jsonify({"erro": "Caminhão não existe"}), 404  
      