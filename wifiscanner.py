import subprocess

# Define the shell command to get a list of available Wi-Fi networks
command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'

# Execute the shell command and capture the output
output = subprocess.check_output(command, shell=True).decode()

# Split the output by newlines to get a list of networks
networks = output.strip().split('\n')[1:]

# Print the list of networks
print('Available Wi-Fi Networks:')
for network in networks:
    print(network)




