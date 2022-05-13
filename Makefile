dual_usrp_logger.py: dual_usrp_logger.grc
	grcc dual_usrp_logger.grc

install: dual_usrp_logger.py
	cp dual_usrp_logger.py /usr/local/bin
	chmod 755 /usrl/local/bin/dual_usrp_logger.py
	cp logger_0.py /usr/local/bin
	cp lmst_wait.py /usr/local/bin
	chmod 755 /usr/local/bin/lmst_wait.py
