from __future__ import annotations

from pathlib import Path
from typing import Any

import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as lambda_
from aws_cdk import Tags
from constructs import Construct


class SpringBootApp(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.DockerImageFunction(
            self,
            "spring_boot_fn",
            code=lambda_.DockerImageCode.from_image_asset(
                directory=str(Path.cwd()),
            ),
            timeout=cdk.Duration.seconds(25),
            memory_size=1024,
        )

        book_api = apigw.LambdaRestApi(
            self,
            "book_api",
            handler=fn,
            proxy=False,
        )

        # @GetMapping("/book/{isbn}")
        book_resource = book_api.root.add_resource("book")
        book_isbn = book_resource.add_resource("{isbn}")
        book_isbn.add_method("GET")


app = cdk.App()
sprint_boot_app = SpringBootApp(app, "SpringBootDemo")
Tags.of(sprint_boot_app).add("Project", "spring_boot_demo")
Tags.of(sprint_boot_app).add("Creator", "cdk")
app.synth()
