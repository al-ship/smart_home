string id
string text
# 0-info, 1-warn, 2-alert:
uint8 level
#one or several: log,audio(voice),display,sms,mail:
string destination
#client device ID or mail or number or something alse:
string recipient
# image or sound data:
uint8[] data
