#!/usr/bin/env python3
from classifier_interface import Classifier
import json

user_review = input()
dict_json = {}

dict_json['text'] = user_review


cls = Classifier()

print(cls.predict_json(dict_json))
