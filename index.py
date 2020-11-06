from flask import Flask, request,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/ecosol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    precio = db.Column(db.String(100))
    oferta = db.Column(db.String(100))
    imagen = db.Column(db.String(100))
    id_categoria = db.Column(db.String(100))

    categoria=id_categoria

    def __init__(self,nombre,precio,imagen,categoria,oferta):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.categoria = categoria
        self.oferta = oferta

# db.create_all()
class pdSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','precio','imagen','categoria','oferta')

task_schema = pdSchema()
tasks_schema = pdSchema(many=True)

@app.route('/products',methods=['GET'])
def get_tasks():
    all_tasks = productos.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
