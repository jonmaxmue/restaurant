# start from an official image
FROM python:3.9

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our two dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system


# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000


# install curl
RUN apt-get install -y curl
#RUN npm -g install yuglify

# ********   GDAL etc. for GeoDjango -> START   **********
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get install -y libproj-dev
# Existing binutils causes a dependency conflict, correct version will be installed when GDAL gets intalled
RUN apt-get remove -y binutils
RUN apt-get autoremove -y

RUN apt-get install -y libgdal-dev g++ --no-install-recommends
RUN apt-get install -y gdal-bin
# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV LC_ALL="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"

RUN apt-get install -y python3-gdal
RUN apt-get install binutils
RUN apt-get install libproj-dev
# ********   GDAL etc. for GeoDjango -> END   **********

COPY supervisord.conf /etc/
CMD ["supervisord"]
#CMD tail -f /dev/null