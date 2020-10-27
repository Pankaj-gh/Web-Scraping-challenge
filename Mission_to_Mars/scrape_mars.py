from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


app = Flask(__name__)

def scrape():
