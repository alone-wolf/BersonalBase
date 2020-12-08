from flask import Blueprint

Device_routes = Blueprint("Device_routes", __name__)


@Device_routes.route("/device/index")
def device_index():
    return ""

# device in section con json data set
#        hostname
#        platform
#        batteryLevel int or false or "" or -1
#        token
#        ...

# progress
#
