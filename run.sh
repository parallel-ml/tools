arr=( 32 64 128 256 512 )

for i in "${arr[@]}"
do
    python run_stand_alone.py $i 5 128 channel
    sleep 300
    python stop_stand_alone.py
done
