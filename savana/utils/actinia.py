###############################################################################
# Filename: actinia.py                                                         #
# Project: TomorrowNow                                                         #
# File Created: Monday March 14th 2022                                         #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Sun Mar 20 2022                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2022 TomorrowNow                                               #
#                                                                              #
# TomorrowNow is an open-source geospatial participartory modeling platform    #
# to enable stakeholder engagment in socio-environmental decision-makeing.     #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
#                                                                              #
###############################################################################


from django.conf import settings
from requests.auth import HTTPBasicAuth
import json
import os
from django.contrib.gis.gdal import DataSource

ACTINIA_SETTINGS = settings.ACTINIA

def print_as_json(data):
    return json.dumps(data)

def auth():
    print(ACTINIA_SETTINGS)
    auth = HTTPBasicAuth(ACTINIA_SETTINGS['ACTINIA_USER'], ACTINIA_SETTINGS['ACTINIA_PASSWORD'])
    return auth

def baseUrl():
    ACTINIA_URL = os.path.join('http://',ACTINIA_SETTINGS['ACTINIA_BASEURL'], 'api', ACTINIA_SETTINGS['ACTINIA_VERSION'])
    print(ACTINIA_URL)
    return ACTINIA_URL

def location():
    return ACTINIA_SETTINGS['ACTINIA_LOCATION']

def currentUser():
    return ACTINIA_SETTINGS['ACTINIA_USER']
