echo "Gathering system information..."
systeminfo /s LOCALHOST >> output.txt
echo "Gathering port info..."
netstat -a -n -o >> output.txt
echo "Gathering running processes..."
tasklist >> output.txt