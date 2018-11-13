[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# SwingR Open Source Cloud Recommender System
SwingR is a Machine Learning Cloud Based Recommender System API for real time E-commerce solutions. SwingR utilizes Neural Networks to predict what kind of products the user is looking to purchase. Based on his/her clicking habits we will train our model to predict what to recommend to the user.

## Goals For this Project ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

- Develop a user freindly API list of endpoints which e-commerce platforms can easily implement into their systems 
- Experiment with multiple neural network architectures for recommendation, the e-commerce platform should have the ability to choose the kind of neural network they would like to use
- Perform multiple data transformations and store procedures, to ensure a better recommendation each time a user utilizes the eccomerce website
- Deploy our model to Google Colab is
- Implement a REST API to transact data between e-commerce vendor and our platform
- Implement a Javascript cdn hotlink for web developers to utilize in their HTML scripts
- Implement multiple factor suggestions Descision Trees + Neural Networks 

## Prerequizits ![pre](https://img.shields.io/badge/prerequizits-optional-blue.svg)
- Knowllege about Tensorflow 
- Python Basics
- REST API implementation 
- JSON 
- Neural Networks 
- Google Cloud Services
- Mathematics (Calculus and Lineer Algebra)

## Getting Started (Development) ![David](https://img.shields.io/david/dev/expressjs/express.svg?style=popout-square)

There are multiple dependencies to install, please install the follwoing and then run ```python start.py```
- Tensorflow
- Numpy
- Flask
- sqllite3
- csv
- MongoDB

## API endpoints [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)
The following are some API endpoints that we are working to implement in near duture some have been iplmented already:

**http://yourdomain.com/feed/**   - This endpoint should be sent a POST request containing the following JSON:

```
{
    "user_id":"34sd",
    "user_sessison":"123w",
    "user_age":27,
    "date_submitted":"14 September 2018",
    "time_submitted":"8:30pm",
    "purchase_income_todate":"$234",
    "search_activities":[{
        "search_id":"23",
        "search_data":"toys for kids",
        "time_stamp":"7:50pm",
        "results_link":"https://www.lazada.co.th/catalog/?q=kids+toys&_keyori=ss&from=input&spm=a2o4m.home.search.go.1125719cRd99FD"
    },
    {
        "search_id":"25",
        "search_data":"Remote control car",
        "time_stamp":"8:11pm",
        "results_link":"https://www.lazada.co.th/catalog/?q=remote+control+car&_keyori=ss&from=input&spm=a2o4m.searchlist.search.go.27cf5478bpLNl6"
    },
    {
        "search_id":"29",
        "search_data":"pots and pans",
        "time_stamp":"9:30pm",
        "results_link":"https://www.lazada.co.th/catalog/?q=pots+and+pans&_keyori=ss&from=input&spm=a2o4m.searchlist.search.go.186f2ca0fKEpwi"
    }
]
}
```

**http://yourdomain.com/suggest/{user_id}**   - This endpoint should be sent a GET request with the user id such that the system can scan for available sugegstions for that user, before a suggestion is ready a user must have had at least 100 search entries registered in the system, after which this endpoint can be called after a specified number of minutes


## Authors ![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=popout-square&label=Stars)


This project what initially started by myself and @aakashsplinter, we have created this project with the intention of creating a community based open source project which we all can commit to and benifit from using and exandiing your skillset. 

## Contributing ![DUB](https://img.shields.io/dub/l/vibe-d.svg?style=popout-square)

Please feel free to create issues and push code to this respository as and when you like, we always like adding new ideas to this respository to ensure  a mix of ideas and functionality. Please ensure you make detailed commits so that we have an idea of what you where trying to achieve, before pushing to production Branch.

## Versioning 
Please utilize the versioning methodology found in this respositiory https://github.com/GitTools/GitVersion


