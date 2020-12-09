from flask import Blueprint, request, abort

from PersonalBase.apps.Device import config
from PersonalBase.apps.Device.config import Config

Device_routes = Blueprint("Device_routes", __name__)


@Device_routes.route("/device/index")
def device_index():
    return ""


@Device_routes.route("/device/register", methods=['POST'])
def device_register():
    device_name = request.form.get("device_hostname") or request.form.get("device_name") or abort(400)
    device_platform = request.form.get("device_platform") or Config.DevicePlatform.Other
    if device_platform not in Config.DevicePlatform.PlatformList:
        device_platform = Config.DevicePlatform.Other
    device_power = request.form.get("device_power") or Config.DevicePower.Unknown
    if device_power not in Config.DevicePower.PowerList:
        device_power = Config.DevicePower.Unknown
    if device_power == Config.DevicePower.Battery:
        device_battery_level = request.form.get("device_battery_level") or -1
    device_token = ""  # return by db
    pass
# TODO complete this def

# device in section con json data set
#        hostname
#        platform
#        batteryLevel int or false or "" or -1
#        token
#        ...

# progress
#
