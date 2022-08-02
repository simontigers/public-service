FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN playwright install

EXPOSE 5000

RUN mkdir logs

CMD [ "python3", "-m","flask","run" ,"--host=0.0.0.0"]
