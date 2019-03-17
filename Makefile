setup:
	#python3 -m venv ~/.py4ds
	#source ~/.py4ds/bin/activate

makesite:
	jupyter-book create py4ds

buildsite:
	jupyter-book build py4ds

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
