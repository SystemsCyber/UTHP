#!/bin/bash

# Function to convert from BCD to Decimal
bcd2dec() {
  local input_string="$1"
  echo "${input_string#0x}"
}

# Function to set system time and date
set_system_datetime() {
  local datetime_str="$1"
  sudo date --set="$datetime_str"
  echo "Custom script: Date set system date to: $datetime_str" | sudo tee /dev/kmsg
}

# Read values from DS1307
seconds=$(i2cget -y 1 0x68 0x00)
minutes=$(i2cget -y 1 0x68 0x01)
hours=$(i2cget -y 1 0x68 0x02)
dayOfWeek=$(i2cget -y 1 0x68 0x03)
date=$(i2cget -y 1 0x68 0x04)
month=$(i2cget -y 1 0x68 0x05)
year=$(i2cget -y 1 0x68 0x06)

# Convert BCD to Decimal
seconds=$(bcd2dec $seconds)
minutes=$(bcd2dec $minutes)
hours=$(bcd2dec $hours)
dayOfWeek=$(bcd2dec $dayOfWeek)
date=$(bcd2dec $date)
month=$(bcd2dec $month)
year=$(bcd2dec $year)

# Call function to set system time
datetime_str=$(printf "20%02d-%02d-%02d %02d:%02d" $year $month $date $hours $minutes)
set_system_datetime "$datetime_str"
