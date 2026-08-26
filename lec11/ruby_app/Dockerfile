FROM ruby:3.2.3-slim

RUN apt update && apt install -y build-essential 

WORKDIR /app/

COPY Gemfile .

RUN bundle install

COPY app.rb  .

EXPOSE 4567

ENTRYPOINT ["bundle","exec","ruby","app.rb","-o","0.0.0.0"]