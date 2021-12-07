From ubuntu:20.04
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN apt-get update && \
    apt-get -y install gcc mono-mcs make && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install python3-pip
RUN apt-get update && apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /usr/src/app
