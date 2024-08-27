from kfp import local
from kfp import dsl
from kfp import compiler

local.init(runner=local.DockerRunner())

@dsl.component(base_image='python:3.11', packages_to_install=['google-cloud-speech'])
def add(a: int, b: int) -> int:
    return a + b


@dsl.pipeline
def math_pipeline(x: int, y: int, z: int) -> int:
    t1 = add(a=x, b=y)
    t2 = add(a=t1.output, b=z)
    return t2.output


pipeline_task = math_pipeline(x=1, y=2, z=3)

compiler.Compiler().compile(math_pipeline, package_path='pipeline.yaml')
