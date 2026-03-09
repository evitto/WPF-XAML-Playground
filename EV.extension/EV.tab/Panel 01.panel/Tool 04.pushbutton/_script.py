# -*- coding: utf-8 -*-

import os
from pyrevit import script

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------

log_folder = r'C:\Users\e.vitto\Documents\DAE REVIT LOG'
log_file = os.path.join(log_folder, 'button_click_log.txt')

# Get button name automatically from pyRevit
button_name = script.get_info().name

# -------------------------------------------------------
# CREATE FOLDER IF NOT EXISTS
# -------------------------------------------------------

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# -------------------------------------------------------
# CREATE FILE IF NOT EXISTS
# -------------------------------------------------------

if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        f.write('')

# -------------------------------------------------------
# READ EXISTING DATA
# -------------------------------------------------------

data = {}

with open(log_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    if ':' in line:
        name, value = line.split(':')
        data[name.strip()] = int(value.strip())

# -------------------------------------------------------
# UPDATE CLICK COUNT
# -------------------------------------------------------

if button_name in data:
    data[button_name] += 1
else:
    data[button_name] = 1

# -------------------------------------------------------
# WRITE UPDATED DATA
# -------------------------------------------------------

with open(log_file, 'w') as f:
    for key in sorted(data):
        f.write('{} : {}\n'.format(key, data[key]))

# -------------------------------------------------------
# OPTIONAL PRINT
# -------------------------------------------------------

print('{} clicked {} times'.format(button_name, data[button_name]))