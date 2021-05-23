for i in {001..202}; do

python _create_contest_folder.py <<EOF
https://atcoder.jp/contests/abc`printf %03d $i`
EOF

done