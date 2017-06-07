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
import urllib2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("I am in the main handler")

class CountHandler(webapp2.RequestHandler):
    def get(self):
        count_welcome = JINJA_ENVIRONMENT.get_template("templates/number-start.html")
        self.response.write(count_welcome.render())

    def post(self):
        count_template = JINJA_ENVIRONMENT.get_template("templates/number.html")
        users_fav_num = self.request.get("my_num")
        self.response.write(count_template.render({"user_number":users_fav_num}))


class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortune_page = JINJA_ENVIRONMENT.get_template("templates/fortune-start.html")
        self.response.write(fortune_page.render())

    def post(self):
        fortune_template = JINJA_ENVIRONMENT.get_template("templates/fortune.html")
        user_name_is = self.request.get("my_name")
        user_location_is = self.request.get("my_location")
        fortunes = ["You will be happy.", "You will grow taller.", "You will find a puppy."]
        self.response.write(fortune_template.render({"name": user_name_is, "location": user_location_is, "fortune": fortunes[random.randrange(0,len(fortunes)-1)]}))

class GifHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/gif-form.html")
        self.response.write(template.render())

    def post(self):
        template = JINJA_ENVIRONMENT.get_template("templates/gif.html")
        query = self.request.get('user_query')
        url = "http://api.giphy.com/v1/gifs/search?q=" + query.replace(" ", "+") + "&api_key=dc6zaTOxFJmzC"
        data = urllib2.urlopen(url)
        giphy_json_content = data.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        image = parsed_giphy_dictionary['data'][0]['images']['fixed_height']['url']
        self.response.write(template.render({"gif": image}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune', FortuneHandler),
    ('/gif', GifHandler),
], debug=True)
