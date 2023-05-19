from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# app.app_context().push()
# db.create_all()


class AnimalModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(40), nullable=False)
    race = db.Column(db.String(40), nullable=False)
    years_old = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Animal(name= {self.name}, years_old = {self.years_old}, type = {self.type}, race= {self.race}) "


animal_put_args = reqparse.RequestParser()
animal_put_args.add_argument("name", type=str, help="Name of animal", required=True)
animal_put_args.add_argument("type", type=str, help="Type of animal", required=True)
animal_put_args.add_argument("race", type=str, help="Race of animal", required=True)
animal_put_args.add_argument("age", type=int, help="Animal age", required=True)

animal_update_args = reqparse.RequestParser()
animal_update_args.add_argument("name", type=str, help="Name of animal")
animal_update_args.add_argument("type", type=str, help="Type of animal")
animal_update_args.add_argument("race", type=str, help="Race of animal")
animal_update_args.add_argument("age", type=int, help="Animal age")

animals = {}
resource_fields = {
    "name": fields.String,
    "type": fields.String,
    "race": fields.String,
    "age": fields.Integer
}


class Animals(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = AnimalModel.query.all()
        print(result)
        return result


class Animal(Resource):
    @marshal_with(resource_fields)
    def get(self, animal_id):
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if not result:
            abort(404, message=f"Could not find animal with id: {animal_id}")
        return result

    @marshal_with(resource_fields)
    def post(self, animal_id):
        args = animal_put_args.parse_args()
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if result:
            abort(409, message="Animal id taken")
        animal = AnimalModel(id=animal_id, name=args['name'], type=args['type'], race=args['race'],
                             years_old=args['years_old'])
        db.session.add(animal)
        db.session.commit()

    @marshal_with(resource_fields)
    def patch(self, animal_id):
        result = AnimalModel.query.filter_by(id=animal_id).first()
        args = animal_update_args.parse_args()
        if not result:
            abort(404, message=f"Could not find animal with id: {animal_id}")
        if args['name']:
            result.name = args['name']
        if args['type']:
            result.type = args['type']
        if args['race']:
            result.race = args['race']
        if args['years_old']:
            result.years_old = args['years_old']
        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, animal_id):
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if not result:
            abort(404, message=f"Could not find animal with id: {animal_id}")
        del animals[animal_id]
        return 202


api.add_resource(Animal, "/animal/<int:animal_id>")
api.add_resource(Animals, "/animals")

if __name__ == "__main__":
    app.run(debug=True)
