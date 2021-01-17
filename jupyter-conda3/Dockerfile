FROM continuumio/anaconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet && mkdir /data

# Check your password hash code and replace
# python -c "from notebook.auth import passwd; print(passwd('your_password'))"

ENTRYPOINT ["jupyter", "notebook", "--notebook-dir=/data", "--ip='*'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.password='sha1:f09c06ac2c20:b4485c9257c56da96fa621d29ca1f713b088b23e'"]

# docker build -t nineking424/jupyter-conda3 .
# (test) docker run --rm -d -p 8888:8888 -v C:\docker\data\jupyter:/data nineking424/jupyter-conda3
# (prod) docker run --name jupyter -d --restart always -p 8888:8888 -v C:\docker\data\jupyter:/data nineking424/jupyter-conda3
