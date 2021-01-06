from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'posterName' : 'DevTeam',
              'creationDate' : '12.09.13',
              'message' : 'Hello'}, 
              {'posterName' : 'DevTeam',
              'creationDate' : '12.10.13',
              'message' : 'We hope you like our app'}, 
              {'posterName' : 'DevTeam',
              'creationDate' : '12.09.14',
              'message' : 'Yahallo!!'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang', methods=['POST'])
def addOne():
	language = request.get_json()
	languages.append(language)
	return jsonify({'languages' : languages})


if __name__ == '__main__':
	app.run() #run app on port 8080 in debug mode