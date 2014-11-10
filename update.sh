./sim.py output/deltamatrix.csv 10  > output/deltaneighour.csv 
cat output/deltaneighour.csv | awk -F ':' '{print "sim_"$1":"$2}'| ./writekv.py
