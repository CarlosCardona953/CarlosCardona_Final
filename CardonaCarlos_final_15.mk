CardonaCarlos_final_15.pdf: datos.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: Final.cpp
	g++ Final.cpp

clean:
	rm -rf a.out datos.dat CardonaCarlos_final_15.pdf *~