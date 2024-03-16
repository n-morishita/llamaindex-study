FROM python:3.11

RUN apt update && \
    apt install -y locales tzdata cmake && \
    pip install llama-index-llms-llama-cpp && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN locale-gen ja_JP.UTF-8
    
# 日本語に設定
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# 日本時間に設定
ENV TZ=Asia/Tokyo
