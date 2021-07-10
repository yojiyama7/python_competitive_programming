for num in `seq -f '%03g' 1 208`; do
    bash folder_rename.sh abc_$num abc$num
done
