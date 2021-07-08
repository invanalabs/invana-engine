"""

"""

#  Copyright 2020 Invana
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http:www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

SCHEMA_SAMPLE_DATA = [
                  {
                      "label": "Student",
                      "properties": {
                          "name": "student {}".format(i),
                          "age": i,
                      }
                  } for i in range(12, 50)
              ] + [
                  {
                      "label": "Teacher",
                      "properties": {
                          "name": "teacher {}".format(i),
                          "age": i,
                          "subject": "xyz"
                      }
                  } for i in range(25, 35)
              ]
