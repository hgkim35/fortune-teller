#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("I am in the main handler")

class CountHandler(webapp2.RequestHandler):
    def get(self):
        count_template = JINJA_ENVIRONMENT.get_template("templates/number.html")
        users_fav_num = 27
        self.response.write(count_template.render({"user_number":users_fav_num}))

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortunes = ["You will be happy." "You will grow taller." "You will find"]
        user_name = "Grace"
        user_location = "Brooklyn"
        fortune_page = JINJA_ENVIRONMENT.get_template("templates/fortune.html")
        self.response.write(fortune_page.render({"name": user_name, "location": user_location}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune', FortuneHandler),
], debug=True)
