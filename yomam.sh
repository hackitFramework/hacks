echo $1
git clone $1
cd $2
grep -o -Ril $3 ./ 
cd ..
rm -rf $2
