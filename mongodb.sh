shodan download search "mongodb"
gzip -d search.json.gz
python3 mongodb.py /root/mongodb.txt
echo "output file /root/mongodb.txt"