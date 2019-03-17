setup:
	#python3 -m venv ~/.py4ds
	#source ~/.py4ds/bin/activate

makesite:
	jupyter-book create ../TEMPLATE/py4ds

buildsite:
	jupyter-book build ../TEMPLATE/py4ds
	cp -R ../TEMPLATE/py4ds/* ../
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
