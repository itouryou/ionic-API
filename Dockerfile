FROM python:3.8 as builder

ARG project_dir=/app/

COPY . $project_dir

ENV PYTHONPATH=${APPDIR}/src
ENV LANG="ja_JP.UTF-8"

WORKDIR $project_dir

RUN mkdir log

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 80

ENV PYTHONUNBUFFERED=TRUE

RUN chmod +x command.sh

RUN sed -i 's/\r//' *.sh

CMD ["./command.sh"]