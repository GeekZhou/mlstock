./readkv.py $1| ./cmd.py './split.py @1 ,'|grep [0-9]|./zfill.py| ./cmd.py './readkv.py rat_@1'
