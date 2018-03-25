from flask import Flask
app = Flask(__name__)


from py2neo import authenticate, Graph
import os

url = 'localhost:7474'
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

# set up authentication parameters
authenticate(url, username, password)

# connect to authenticated graph database
graph = Graph("http://localhost:7474/db/data/")


@app.route('/')
def hello_world():
  query = """
  MATCH (d:Drug) RETURN d.drug_name
  LIMIT 5
  """

  d = graph.run(query)

  #return 'Hello, world!'
  return d

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80)
