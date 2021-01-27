import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheet)

df = pd.read_csv('https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv')

app.layout = html.Div(children = [
    html.H1(children = "Hello World!"),

    html.Div(children = """
        Web page start!
    """),
])

if __name__ == '__main__':
    app.run_server(debug = True)