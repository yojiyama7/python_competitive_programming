# echo $1 $2

python reset_contest_folder.py <<EOF
$1
EOF
python _create_contest_folder.py <<EOF
https://atcoder.jp/contests/$2
EOF
