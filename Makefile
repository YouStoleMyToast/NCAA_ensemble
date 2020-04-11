mac:
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 5 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 9 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 8 -i 90
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 5 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 8 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 7 -i 120
	python3 fit_data.py -f data/train.csv -m bagging-tree -s k-fold -S random -F 6 -i 200
	make mac
