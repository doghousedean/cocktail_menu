from flask import Flask, render_template, send_file
from cocktails import Cocktails
import urllib.parse
import sys, os
import json
import qrcode
import io

app = Flask(__name__)

with open(os.path.join(sys.path[0], "config.json"), "r") as cf:
    config = json.load(cf)


@app.route("/")
def root():
    """
        Default response
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    # print(json.dumps(data, indent=2))
    return render_template("showcocktail.html", data=drinks.getRandom(), heading=heading)


@app.route("/cocktail/<name>")
def cocktail_name(name):
    """
        Search for a cocktail
    :param name:
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    drink = drinks.search(name)
    if drink is not None:
        return render_template("showcocktail.html", data=drink, heading=heading)
    else:
        return render_template("showcocktail.html", data=drinks.search('none'), heading=heading)


@app.route("/cocktails")
def cocktails():
    """
        Show cocktail list
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    data = drinks.getAll()
    return render_template("listcocktails.html", data=data, heading=heading)


@app.route("/ingredients")
def ingredients():
    """
        A list of ingredients and quantities
    :return:
    """
    drinks = Cocktails()
    data = drinks.getIngredients()
    # sorted_dict = {k: disordered[k] for k in sorted(disordered)}
    # sorted_data = {k: data for k in sorted(data)}
    return render_template("listingredients.html", data=data, heading=config['heading'])

@app.route("/base")
def base():
    """
        A list of ingredients and quantities
    :return:
    """
    drinks = Cocktails()
    data = drinks.getByBase()
    # sorted_dict = {k: disordered[k] for k in sorted(disordered)}
    # sorted_data = {k: data for k in sorted(data)}
    return render_template("showbybase.html", data=data, heading=config['heading'])

# Route to generate the QR code image
@app.route("/qr/<path:data>")
def generate_qr(data):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a byte stream
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)

    # Return the image as a response
    return send_file(img_byte_arr, mimetype="image/png")

# Route to display the template with QR code
@app.route("/wifi")
def wifi():
    wifi_data = "WIFI:T:WPA;S:MooreHenHouse;P:merebrow;;"  # Example Wi-Fi data
    url = "http://192.168.2.243/"
    return render_template("help.html", wifi_qr_code=f"/qr/{wifi_data}", menu_qr_code=f"/qr/{url}")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
