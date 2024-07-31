#!/bin/sh

# ANSI Color -- use these variables to easily have different color
#    and format output. Make sure to output the reset sequence after 
#    colors (f = foreground, b = background), and use the 'off'
#    feature for anything you turn on.
# Author: pfh
# Source: http://crunchbang.org/forums/viewtopic.php?pid=129265#p129265

# Add /sbin, /usr/sbin, and /usr/local/sbin to the PATH
export PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin

initializeANSI()
{
  esc=""

  blackf="${esc}[30m";   redf="${esc}[31m";    greenf="${esc}[32m"
  yellowf="${esc}[33m";  bluef="${esc}[34m";   purplef="${esc}[35m"
  cyanf="${esc}[36m";    whitef="${esc}[37m"
  
  blackfbright="${esc}[90m";   redfbright="${esc}[91m";    greenfbright="${esc}[92m"
  yellowfbright="${esc}[93m";  bluefbright="${esc}[94m";   purplefbright="${esc}[95m"
  cyanfbright="${esc}[96m";    whitefbright="${esc}[97m"
  
  blackb="${esc}[40m";   redb="${esc}[41m";    greenb="${esc}[42m"
  yellowb="${esc}[43m";  blueb="${esc}[44m";   purpleb="${esc}[45m"
  cyanb="${esc}[46m";    whiteb="${esc}[47m"

  boldon="${esc}[1m";    boldoff="${esc}[22m"
  italicson="${esc}[3m"; italicsoff="${esc}[23m"
  ulon="${esc}[4m";      uloff="${esc}[24m"
  invon="${esc}[7m";     invoff="${esc}[27m"

  reset="${esc}[0m"
}

initializeANSI

cat << EOF

${greenf}
                   ██████╗███████╗██╗   ██╗
                  ██╔════╝██╔════╝██║   ██║
                  ██║     ███████╗██║   ██║
                  ██║     ╚════██║██║   ██║
                  ╚██████╗███████║╚██████╔╝
                   ╚═════╝╚══════╝ ╚═════╝ 

                  _______________________________________________________
                  |                                                      |
             /    |                                                      |
            /---, |                                                      |
       -----# ==| |                TruckHackingOS v1.0.0                 |
       | :) # ==| |                                                      |
  -----'----#   | |______________________________________________________|
  |)___()  '#   |______====____   \___________________________________|
 [_/,-,\"--"------ //,-,  ,-,\\\   |/             //,-,  ,-,  ,-,\\ __#
   ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||
----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------
Welcome to the Ultimate Truck Hacking Platform

To find software included in this image, run 'sudo apt list', 'dpkg -l', or 'pip3 list'
${reset}

EOF
# Set the PS1 prompt
if [ "$EUID" -eq 0 ]; then
    export PS1="\[$greenf\]\h\[$reset\]:\[$greenfbright\]\w\[$reset\]# "
else
    export PS1="\[$greenf\]\h\[$reset\]:\[$greenfbright\]\w\[$reset\]\$ "
fi