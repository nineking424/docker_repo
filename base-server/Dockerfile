FROM centos:7
ADD oracle-instantclient*.rpm /tmp/

# Oracle 설치
RUN yum -y install /tmp/oracle-instantclient*.rpm && \
rm -rf /var/cache/yum && \
rm -f /tmp/oracle-instantclient*.rpm && \
echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient12.2.conf && \
# GCC 설치
yum -y install gcc && \
yum -y install gcc-c++ && \
ldconfig

# PATH 설정
ENV PATH=$PATH:/usr/lib/oracle/12.2/client64/bin

# SSH 설치
RUN yum  -y install openssh-server openssh-clients && \
systemctl enable sshd

# FTP
RUN yum -y install vsftpd ftp && \
echo 'anonymous_enable=NO' > /etc/vsftpd/vsftpd.conf && \
echo 'local_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'write_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'local_umask=022' >> /etc/vsftpd/vsftpd.conf && \
echo 'dirmessage_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'xferlog_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'connect_from_port_20=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'xferlog_file=/var/log/xferlog' >> /etc/vsftpd/vsftpd.conf && \
echo 'xferlog_std_format=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'listen=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'pam_service_name=vsftpd' >> /etc/vsftpd/vsftpd.conf && \
echo 'userlist_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'tcp_wrappers=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'use_localtime=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'pasv_enable=YES' >> /etc/vsftpd/vsftpd.conf && \
echo 'pasv_min_port=50000' >> /etc/vsftpd/vsftpd.conf && \
echo 'pasv_max_port=50099' >> /etc/vsftpd/vsftpd.conf && \
systemctl enable vsftpd

EXPOSE 20 21 22

ENTRYPOINT ["/usr/sbin/init"]

# docker build -t nineking424/base-server:latest .
# docker run --name myserver -d -p 20-22:20-22 -p 50000-50099:50000-50099 --privileged nineking424/base-server:latest
# docker exec -it myserver bash
# docker stop myserver && docker rm myserver
# docker push nineking424/base-server:latest