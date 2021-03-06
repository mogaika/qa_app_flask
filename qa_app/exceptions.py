#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from flask import current_app, render_template


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', page="Not Found"), 404


@current_app.errorhandler(Exception)
def internal_error(e):
    return render_template('errors/500.html', page="Internal Server Error"), 500

