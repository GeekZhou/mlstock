./readkv.py sim_$1| ./cmd.py './split.py @1 ,'|grep [0-9]|./zfill.py| ./cmd.py './delta.py @1'
