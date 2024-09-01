#run.py
import subprocess as sp
import sys
#Used https://www.geeksforgeeks.org/python-subprocess-module/?ref=gcse_ind to learn about the subprocess and get the syntax for the exception
file = open('/home/mgauna/cs3640/A1/output.txt', 'w+')
file.write('mgauna Maria Gauna')
file.write('\n')
file.write('\n')

if len(sys.argv)==2:
    ip = sys.argv[1]
    try:
        current_date = sp.run(['date'], capture_output=True, text=True)
        file.write('\n*****\n')
        file.write(f'Command: (Date) {current_date.stdout}')
    except:
        file.write(f'[Error]Command:(Date) failed with return code:{sp.CalledProcessError.returncode}')
        print(f'[Error]Command:(Date) failed with return code:{sp.CalledProcessError.returncode}')
    try:
        current_whoami= sp.run(['whoami'], capture_output=True, text=True)
        file.write('\n*****\n')
        file.write(f'Command: (whoami) {current_whoami.stdout}')
    except:
        file.write(f'[Error]Command:(whoami) failed with return code:{sp.CalledProcessError.returncode}')
        print(f'[Error]Command:(whoami) failed with return code:{sp.CalledProcessError.returncode}')
    try:
        current_ifconfig= sp.run(['ifconfig'], capture_output=True, text=True)
        file.write('\n*****\n')
        file.write(f'Command: (ifconfig) {current_ifconfig.stdout}')
    except:
        file.write(f'[Error] Command:(ifconfig) failed with return code:{sp.CalledProcessError.returncode}')
        print(f'[Error] Command:(ifconfig) failed with return code:{sp.CalledProcessError.returncode}')
    try:
        current_ping= sp.run(['ping' ,ip, '-c', '10'], capture_output=True, text=True)
        file.write('\n*****\n')
        file.write(f'Command: (ping {ip} -c 10) {current_ping.stdout}')
    except:
        file.write(f'[Error] Command:(ping {ip} -c 10) failed with return code:{sp.CalledProcessError.returncode}')
        print(f'[Error] Command:(ping {ip} -c 10) failed with return code:{sp.CalledProcessError.returncode}')
    try:
        current_traceroute= sp.run(['traceroute',ip, '-m', '10'], capture_output=True, text=True)
        file.write('\n*****\n')
        file.write(f'Command: (traceroute {ip} -m 10) {current_traceroute.stdout}')
    except:
        file.write(f'[Error] Command:(traceroute {ip} -m 10) failed with return code:{sp.CalledProcessError.returncode}')
        print(f'[Error] Command:(traceroute {ip} -m 10) failed with return code:{sp.CalledProcessError.returncode}')

elif len(sys.argv)==1:
    file.write(f'[Error] No IP address stated detected. Please try again.')
    print(f'[Error] No IP address stated detected. Please try again..')
elif len(sys.argv)> 2:
    file.write(f'[Error] To many arguments inputted. Please try again.')
    print(f'[Error] To many arguments inputted. Please try again.')
file.close()