# build用のイメージ
FROM amazoncorretto:17 as build
WORKDIR /task
# 必要なリソースのコピー
COPY src src/
COPY gradle gradle/
COPY gradlew .
COPY build.gradle .
# gradleタスク実行
RUN chmod 775 gradlew
RUN ./gradlew bootJar

# Spring boot実行用イメージ
FROM amazoncorretto:17-alpine
WORKDIR /opt
# aws-lambda-web-adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter
# ポートの指定
EXPOSE 8080
# build用イメージから必要なアプリを抜き出す
COPY --from=build /task/build/libs/task-0.0.1-SNAPSHOT.jar /opt
# アプリ起動
ENTRYPOINT ["java", "-jar", "task-0.0.1-SNAPSHOT.jar"]