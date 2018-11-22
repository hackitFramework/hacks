sudo apt-get install httrack
pip install pygithub3
pip install requests
git clone https://github.com/hsamuelson/hacks
echo "PATH=$pwd/hacks/gitgrab" > ./hacks/gitgrab/gitgrab
mv ./hacks/gitgrab/gitgrab /bin
cd /bin
chmod +x gitgrab