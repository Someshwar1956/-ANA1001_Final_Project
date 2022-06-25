#****************************************************************
#Name: Someshwar Baghel
#Student Number: A00254095
#ANA1001_final Project
#****************************************************************


from flask import Flask, render_template # from flash we are importing flask
import requests, json #importing json and requests
app = Flask('app')


@app.route('/')
def home():   #defining home
  return render_template("index.html") 


@app.route('/page1')
def page1():  #defining page1


  url = 'https://www.balldontlie.io/api/v1/games/1'  #calling api 

  
  r = requests.get(url).json() #storing API response in a json file

  
  filename = 'data2.json' #dump into a json File
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  
  filename = 'data2.json'   #load a json File
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  team_score = []
  #extract = ['Boston Celtics', 'Philadelphia 76ers']

  data = all_data['home_team_score']
  team_score.append(data)

  data = all_data['visitor_team_score']
  team_score.append(data)
    
  print(team_score)

  