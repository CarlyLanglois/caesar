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
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
    <h1>Enter some text to encode</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.caesar.com/
    """
    def get(self):


        # a form to encrypt text
        my_form = """
        <form method="post">
            <label>
                Rotate by: <input type="number" name="rotate-number"/>
            </label>
            <textarea name="text" style="height: 100px; width: 400px;"></textarea>
            <br>
            <input type="submit">
        </form>
        """
        #add the form to the body of the html document
        page_text = page_header + my_form + page_footer
        self.response.write(page_text)

    def post(self):
        # look inside the request to figure out what the user typed
        rotate_number = self.request.get("rotate-number")
        text_to_encrypt = self.request.get("text")

        # use caesar to encrypt the text in the box but the rotate number
        encrypted_text = encrypt(text_to_encrypt, 4)

        #build the page content
        response = page_header + my_form + page_footer
        self.response.write(response)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
