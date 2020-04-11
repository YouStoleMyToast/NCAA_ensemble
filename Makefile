mac:
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 5 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 9 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 8 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 5 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 8 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 7 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 6 -i 200

	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 13 -i 109
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 9 -i 122
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 25 -i 80
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 25 -i 60
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 15 -i 110
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 7 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 10 -i 180


	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 5 -i 150
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 9 -i 150
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 11 -i 85
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 20 -i 130
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 15 -i 110
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 12 -i 150
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 9 -i 170

	make mac
