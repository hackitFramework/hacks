echo "Gathering system information..."

git clone ""
cd reponame

systeminfo /s LOCALHOST >> output.txt
echo "Gathering port info..."
netstat -a -n -o >> output.txt
echo "Gathering running processes..."
tasklist >> output.txt

git stage *
git commit -m "Adding Person Info"
git push origin ""
