FROM homeassistant/armhf-base:latest
COPY run.py /
RUN apk add --update --no-cache \
	python \
	python-dev \
	py-pip

RUN chmod a+x /run.py
RUN pip install pif
RUN pip install godaddypy
CMD ["python","run.py" ]