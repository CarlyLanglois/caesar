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

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Rot13</title>
</head>
<body>
    <h1>Enter some text to encode</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

#rot13 function
def rot13(text):
    for i in text:
        print 

class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.rot13.com/
    """
    def get(self):
        # a form to encrypt text
        form = """
        <form method="post">
            <textarea name="text" style="height: 100px; width: 400px;"></textarea>
            <br>
            <input type="submit">
        </form>
        """
        #add the form to the body of the html document
        page_text = page_header + form + page_footer
        self.response.write(page_text)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
