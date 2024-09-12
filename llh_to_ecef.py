# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km ...
#  Text explaining script usage
# Parameters:
#  lat_deg: description of argument 1
#  lon_deg: description of argument 2
#  hae_km: description of argument 3
#  ...
# Output:
#  A description of the script output
#
# Written by Ajay Seethana
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
e_E = 0.081819221456

# helper functions

## function description
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0 - ecc ** 2 * math.pow(math.sin(lat_rad), 2))

# initialize script arguments
lat_deg = '' # description of argument 1
lon_deg = '' # description of argument 2
hae_km = ''
#  parse script arguments
if len(sys.argv)==4:
  lat_deg = sys.argv[1]
  lon_deg = sys.argv[2]
  hae_km = sys.argv[3]
  ...
else:
  print(\
   'Usage: '\
   'python llh_to_ecef lat_deg lon_deg hae_km'\
  )
  exit()

# write script below this line

lat_rad = float(lat_deg) * math.pi / 180
lon_rad = float(lon_deg) * math.pi / 180
hae_km = float(hae_km)

denom = calc_denom(e_E, lat_rad)
C_E = R_E_KM / denom
S_E = (R_E_KM * (1-e_E**2))/denom
r_x = (C_E + hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y = (C_E + hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z = (S_E + hae_km)*math.sin(lat_rad)

print(r_x)
print(r_y)
print(r_z)


