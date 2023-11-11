from flask import Flask, render_template, request   # Flask boilerplate by Purplexity 
import routes                                       # Remove comments after dev

config = {                                          # The config of the project
    'Title': 'Hello',                               # The title of the project
    'Host' : 'localhost',                           # The host of the server
    'Port' : 80,                                    # The port of the server
    'Dev'  : True,                                  # If it is in dev mode
    'App?' : True,                                  # If it is a GUI App
}

routing: dict[str, routes.FlaskRouteFunction] = {   # The routes of the project
    '/': routes.index,                              # Add routes in this format
} ; app = Flask(config['Title'])                    # '<url>': routes.<func>,

for url, func in routing.items(): app.add_url_rule(url, view_func=func)

if config['App?']: import webview ; webview.create_window(config['Title'], app) ; webview.start()
else: app.run(config['Host'], config['Port'], config['Dev'])