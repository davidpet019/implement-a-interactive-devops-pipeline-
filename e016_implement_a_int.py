import os
import yaml
from jinja2 import Template

class PipelineGenerator:
    def __init__(self):
        self.pipeline_template = """
pipeline:
  stages:
    - {{ stage }}
  {{ stage }}:
    stage: {{ stage }}
    script:
      - echo "Running {{ stage }} stage"
    only:
      - main
"""

    def generate_pipeline(self, stages):
        template = Template(self.pipeline_template)
        pipeline_yaml = ""
        for stage in stages:
            pipeline_yaml += template.render(stage=stage)
        return pipeline_yaml

def main():
    generator = PipelineGenerator()
    stages = input("Enter stages separated by comma (e.g. build, test, deploy): ").split(', ')
    pipeline_yaml = generator.generate_pipeline(stages)
    print("Generated pipeline YAML:")
    print(pipeline_yaml)
    with open('pipeline.yml', 'w') as f:
        f.write(pipeline_yaml)

if __name__ == "__main__":
    main()