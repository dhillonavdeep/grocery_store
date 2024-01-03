from flask_restful import Resource,Api,reqparse,fields, marshal_with
from .models import Product,db

api=Api(prefix='/api')


parser=reqparse.RequestParser()
parser.add_argument('name', type=str, help='Please provide a valid string for the name.',required=True)
parser.add_argument('description', type=str, help='Please provide a valid string for the description.',required=True)
parser.add_argument('section', type=str, help='Please provide a valid string for the section.')
parser.add_argument('quantity', type=int, help='Please provide a valid integer for the quantity.',required=True)
parser.add_argument('amount', type=int, help='Please provide a valid integer for the amount.',required=True)

product_details_fields = {
    'id':   fields.String,
    'name':   fields.String,
    'description':  fields.String,
    'section':  fields.String,
    'amount': fields.Integer,
    'quantity':fields.Integer
}

class ProductDetails(Resource):
    def get(self):
        return { "message":"Hello from api"}
    def post(self):
        args=parser.parse_args()
        Product_detail=Product(**args)
        db.session.add(Product_detail)
        db.session.commit()
        return { "message":"Product Created"}
    

api.add_resource(ProductDetails,'/product_details')