
echo $1
git clone $1
cd $2
echo "COmmand"
grep -o -Ril $3 ./ 

echo "removing direct"
cd ..
rm -rf $2
