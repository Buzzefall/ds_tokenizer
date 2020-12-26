FROM continuumio/miniconda:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV APP_PATH /var/www/app

ENV PATH $APP_PATH:$PATH
ENV PATH /opt/conda/bin:$PATH


COPY ../../.. $APP_PATH

RUN chmod +x $APP_PATH/scripts/*.sh
RUN conda env update -f $APP_PATH/environment.yml -n base

EXPOSE 7620/tcp


#CMD python ${APP_PATH}/app.py
#CMD python ${APP_PATH}/app.py
CMD [ "python", "/var/www/app/app.py" ]