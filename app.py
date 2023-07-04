from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akljdfjlkajsd'

boggle_game = Boggle()
