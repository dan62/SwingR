#importing of libraries to be used
import csv
import json
import signal_notify

#Variables for testing purposes only for this file
jsoni: str = "{'name':'daniel', 'email':'dan'}"
set_locate: str = "C:/Users/danie/Documents/GitHub/SwingR/settings.json"

#function which calls welcome message
def display_welcome():
    signal_notify.welcome_notification("testUser")

#function that checks users settings and input data and sets up
#the modal to adjust to users prefferences
def check_settings(raw_json,settings):

    #reading of user settings.json file which contains all the setting that will be used
    save_settings = open(settings, "r")
    user_set = json.load(save_settings)
    username = user_set['username']
    platform_name = user_set['your_platform_name']
    data_extention_type = user_set['save_data_type']
    cloud = user_set['cloud_service']
    credentials = user_set['dropbox_credentials']

    #checking if the chosen cloud platform is dropbox
    if cloud=="dropbox":
     app_folder = credentials['app_folder_name']
     app_key = credentials['app_folder_name']
     secret = credentials['app_folder_name']

    #checking if chosen extention is csv
    if data_extention_type == ".csv":
        to_csv()


#Function that writes out a csv file of users post data that will eventually be sent to the cloud for storage
def to_csv():
      with open('ecommerce_users.csv', mode='w') as ecomerce_file:
        history_writer = csv.writer(ecomerce_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        history_writer.writerow(['345', '3343', '27', '14 September 2018', '8:30pm', '$234','23 toys for kids 7:50pm'])
        history_writer.writerow(['345', '3343', '27', '14 September 2018', '8:30pm', '$234', '23 toys for kids 7:50pm'])
        history_writer.writerow(['345', '3343', '27', '14 September 2018', '8:30pm', '$234', '23 toys for kids 7:50pm'])
        history_writer.writerow(['345', '3343', '27', '14 September 2018', '8:30pm', '$234', '23 toys for kids 7:50pm'])


#uncomment the following line if you would like to test this script seperatley
display_welcome()
message = check_settings(jsoni, set_locate);



#these functions to come soon, will allow server owner to store the data in multiple locations
"""
def to_txt():
    
 def to_dedicated_sql():


  def to_mongo():


   def google()
"""