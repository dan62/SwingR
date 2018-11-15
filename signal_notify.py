
welcome_message = ", please read the README document to learn how to alter the \nsettings for the recommender API, we are adding functions daily!"


def welcome_notification(username):
    print("-------------------------------------------------------------------------")
    print("hello " + username + welcome_message)
    print("-------------------------------------------------------------------------")
    print("")
    print("Founder: Daniel Goncalves 2018")
    print("Type of project: Open Source")


def post_recieved_success():
    print('Your post has been received, we are processing data')