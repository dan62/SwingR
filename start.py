#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)


# this is how the json should look when the results of recommendations are returned to the E-commerce wensite
recommended = [
    {
        'id': 1,
        'user_id': 3,
        'product': u'quaadrocopter for children',
        'description': u'childrens toys, 9-10 years old, mothers ',
        'link': u'https://www.lazada.co.th/products/tello-drone-phantom-thailand-i223434133-s341325619.html?spm=a2o4m.searchlist.list.1.5f631286ESdyAo&search=1',
        'image':u'https://th-live.slatic.net/original/12ce6c5d0f8936b880758225aa3ef395.jpg',
    },
    {
        'id': 1,
        'user_id': 3,
        'product': u'quaadrocopter for children',
        'description': u'childrens toys, 9-10 years old, mothers ',
        'link': u'https://www.lazada.co.th/products/tello-drone-phantom-thailand-i223434133-s341325619.html?spm=a2o4m.searchlist.list.1.5f631286ESdyAo&search=1',
        'image': u'https://th-live.slatic.net/original/12ce6c5d0f8936b880758225aa3ef395.jpg',
    }
]

# on successfull feed
successful_feed = [
    {
        'id': "3454",
        'que_number': "3",
        'message': "Your feed has been sent"
    }]



# in future will check if theres available recommendations from training
def check_cloud():
    return 0


# in future will save data that was fed to api
def save_feed():
    return 0


# in future will create the neural network with appropriate parameters
def neural_create():
    return 0


# in future will be used for training the model
def nn_train():
    return 0


# declaration of API routes
@app.route('/suggest', methods=['GET'])
def get_recommendations():
    check_cloud()
    return jsonify({'recommended': recommended})


@app.route('/feed', methods=['GET'])
def feed_for_training():
    save_feed()
    return jsonify({'feed_response': successful_feed})


if __name__ == '__main__':
    app.run(debug=True)