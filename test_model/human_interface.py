#!/usr/bin/env python3
from classifier_interface import Classifier
import json

cls = Classifier()

while True:
    user_review = input()
    dict_json = json.loads('{"text":"","grade":-2,"anonymous":false,"delivery":"DELIVERY","id":66197723,"authorInfo":{"grades":1,"uid":431595006},"shop":{"id":359037,"name":"BONCH.PRO"},"author":"Панарина Ольга","comments":[],"agree":0,"date":1477913239000,"shopId":359037,"reject":0,"problem":"UNRESOLVED","visibility":"NAME","region":2,"pro":""}')

    dict_json['text'] = user_review

    print(cls.predict_json(dict_json))




