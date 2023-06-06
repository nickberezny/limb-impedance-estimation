build:
	gcc test_model.c -ltensorflow -o run_test
	./run_test

install:
	FILENAME=libtensorflow-cpu-linux-x86_64-2.11.0.tar.gz
	wget https://storage.googleapis.com/tensorflow/libtensorflow/${FILENAME}
	sudo tar -C /usr/local -xzf ${FILENAME}
	sudo ldconfig /usr/local/lib