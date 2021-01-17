FROM centos:7
ADD oracle-instantclient*.rpm /tmp/

# Oracle 설치
RUN yum -y install /tmp/oracle-instantclient*.rpm && \
rm -rf /var/cache/yum && \
rm -f /tmp/oracle-instantclient*.rpm && \
echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient12.2.conf && \
# GCC 설치
yum -y install gcc && \
ldconfig

# PATH 설정
ENV PATH=$PATH:/usr/lib/oracle/12.2/client64/bin

# docker build -t nineking424/base-server .
# docker run --rm -it nineking424/base-server bash
# docker push nineking424/base-server