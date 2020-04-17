FROM oraclelinux:7-slim
# Create app directory
WORKDIR /usr/src/app
# Copy the .py files from your host machine into the new app directory
ADD app/ ./
# Update Oracle Linux
# Install cx_Oracle, library for python 
# Install the Oracle Instant Client
RUN yum update -y && \
  yum install -y oracle-release-el7 && \
  yum install -y oracle-epel-release-el7 && \
  yum install -y python3 && \
  yum -y install oraclelinux-developer-release-el7 && \
  yum -y install python-pip && \
  pip install -U pip && \
  python -m pip install cx_Oracle && \
  python -m pip install flask &&\
  yum install -y oracle-instantclient19.3-basic.x86_64 && \
  yum clean all && \
  echo Installed
EXPOSE 3000
CMD ["python", "oracle.py"]