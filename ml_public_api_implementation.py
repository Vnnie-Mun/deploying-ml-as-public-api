# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:06:30 2022

@author: siddhardhan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:16:26 2022

@author: siddhardhan
"""

import json
import requests


url = 'https://32ff17e1971d.ngrok-free.app/diabetes_prediction'


input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

