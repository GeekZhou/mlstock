cat output/name.csv | ./cmd.py './delta.py @1' |awk -F',' '{print "rat_"$1":"$2","$3}' |./writekv.py
