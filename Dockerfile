# specifiy base image
FROM ubuntu:14.04

# Update the sources list
RUN apt-get update

# install useful system tools and libraries
RUN apt-get install -y libfreetype6-dev && \
    apt-get install -y libglib2.0-0 \
                       libxext6 \
                       libsm6 \
                       libxrender1 \
                       libblas-dev \
                       liblapack-dev \
                       gfortran \
                       libfontconfig1 --fix-missing

RUN apt-get install tar \
                    git \
                    curl \
                    nano \
                    wget \
                    dialog \
                    net-tools \
                    build-essential

# install Python and pip package manager
RUN apt-get install -y python \
                       python-dev \
                       python-distribute \
                       python-pip


# intall useful and/or required Python libraries to run your script
RUN pip install matplotlib \
                pandas \
                numpy \
                scipy \
                sklearn \
                argparse \
