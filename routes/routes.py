import json
from utils.helper import *
from flask import request
from flask import Response
from . import routes

db = {}
priceDB = {}


@routes.route('/GetHtml/', methods=["POST"])
def postProduct():
    rawUrl = request.get_json().get('rawUrl', '')
    sku, obj, status = scrapeProduct(rawUrl, priceDB)
    if not status:
        response = Response(
            response="To many request for this Product. Please try later",
            status=429,
            mimetype='application/json'
        )
        return response
    if sku is None and obj is None:
        response = Response(
            response="Please check the URL",
            status=422,
            mimetype='application/json'
        )
        return response
    else:
        db[sku] = obj.__dict__
        currDT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if sku in priceDB:
            priceObj = Prices(currDT, obj.productPrice)
            priceDB[sku].append(priceObj.__dict__)
        else:
            priceObj = Prices(currDT, obj.productPrice)
            priceDB[sku] = [priceObj.__dict__]

        response = Response(
            response=json.dumps(obj.__dict__),
            status=200,
            mimetype='application/json'
        )
        return response


@routes.route('/GetAllProductDetails/', methods=["GET"])
def getAllProductDetails():
    if not db:
        response = Response(
            response="Database Empty",
            status=422,
            mimetype='application/json'
        )
        return response
    else:
        response = Response(
            response=json.dumps(db),
            status=200,
            mimetype='application/json'
        )
        return response


@routes.route('/GetProductDetails/', methods=["GET"])
def getProduct():
    rawUrl = request.get_json().get('rawUrl', '')
    sku, shortenURL = URL(rawUrl).urlShortening()
    if not sku:
        response = Response(
            response="Please check the URL",
            status=422,
            mimetype='application/json'
        )
        return response
    elif sku in db:
        result = db[sku]
        response = Response(
            response=json.dumps(result),
            status=201,
            mimetype='application/json'
        )
        return response
    else:
        response = Response(
            response="No Entry Found for this Product",
            status=404,
            mimetype='application/json'
        )
        return response


@routes.route('/GetPriceTrend/', methods=['GET'])
def getPriceTrend():
    rawUrl = request.get_json().get('rawUrl', '')
    sku, shortenURL = URL(rawUrl).urlShortening()
    if not sku:
        response = Response(
            response="Please check the URL",
            status=422,
            mimetype='application/json'
        )
        return response
    else:
        if sku in priceDB:
            price_obj = {"Prices": priceDB[sku]}
            response = Response(
                response=json.dumps(price_obj),
                status=201,
                mimetype='application/json'
            )
        else:
            response = Response(
                response="No entry found in Database",
                status=404,
                mimetype='application/json'
            )
        return response
