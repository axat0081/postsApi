from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

posts = [{'posterName' : 'DevTeam',
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
	return jsonify({'posts' : posts})

@app.route('/lang', methods=['POST'])
def addOne():
	post = request.get_json()
	posts.append(post)
	return jsonify({'posts' : posts})

if __name__ == '__main__':
	app.run(threaded=True, port=5000) 
