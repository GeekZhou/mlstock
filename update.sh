./sim.py output/matrix.csv 3  > output/neighour.csv 
cat output/neighour.csv | ./writekv.py
