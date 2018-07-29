# app.py

from flask import Flask, request, jsonify, make_response
from dbsetup import create_connection, select_all_items, insert_db, create_table
import json
    
app = Flask(__name__)
database = "./pythonsqlite.db"
    
# create a database connection
conn = create_connection(database)
    
# create items table
create_table(conn)
    
c = conn.cursor()
    
def main():
    global c
        
@app.route('/search', methods=['GET'])
def search():
    data = request.args.get("name")
    output = select_all_items(c, data)
    return json.dumps(output)
        
@app.route('/insert', methods=['POST'])
def insert():
    content = request.json
    name = content['name']
    body = content['body']
    insert_db(c, name, body)
    return "Successful"
        
if __name__ == '__main__':
    main()
    app.run(debug=True)