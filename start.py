#!flask/bin/python
import requests
from flask import Flask, jsonify, request

import signal_notify
import write_feed

app = Flask(__name__)

# this is how the json should look when the results of recommendations are returned to the E-commerce wensite
recommended = [
    {
        'id': 1,
        'user_id': 3,
        'product': u'quaadrocopter for children',
        'description': u'childrens toys, 9-10 years old, mothers ',
        'link': u'https://www.lazada.co.th/products/tello-drone-phantom-thailand-i223434133-s341325619.html?spm=a2o4m.searchlist.list.1.5f631286ESdyAo&search=1',
        'image': u'https://th-live.slatic.net/original/12ce6c5d0f8936b880758225aa3ef395.jpg',
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
def search_cloud(id):
    return 0


# Performs formatting of the data and eventually saving to the cloud
def save_feed(s):
    settings_location = "C:/Users/danie/Documents/GitHub/SwingR/settings.json"
    stream_feed = s
    write_feed.display_welcome()
    if not s == "":
      signal_notify.post_recieved_success()
      write_feed.check_settings(stream_feed, settings_location)
    return 0


# in future will create the neural network with appropriate parameters
def neural_create():
    return 0


# in future will be used for training the model
def nn_train():
    return 0


# Recommendations Endpoint
@app.route('/suggest/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    search_cloud(user_id)
    return jsonify({'recommended': recommended})


# Training data feed endpoint
@app.route('/feed/', methods=['GET', 'POST'])
def feed_for_training():
    stream_data = request.get_json(force=True)

    #uncomment this line if you do not want to post real JSON for testing
    #stream_data="test"

    if not stream_data == "":
        save_feed(stream_data)
    return jsonify({'feed_response': successful_feed})


if __name__ == '__main__':
    app.run(debug=True)
