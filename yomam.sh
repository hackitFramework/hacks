git clone $1 &> /dev/null
cd $2
if grep -o -Ril $3 ./
then
	echo "^" $2 "^" 
fi
cd ..
rm -rf $2
