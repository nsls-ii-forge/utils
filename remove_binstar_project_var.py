# This removes the project variable "BINSTAR_TOKEN" as it somehow interferes
# with the same-named variable from the group variables.

import glob

from conda_smithy.azure_ci_utils import build_client, get_default_build_definition
from conda_smithy.azure_ci_utils import default_config as config
from vsts.build.v4_1.models import BuildDefinitionVariable


bclient = build_client()

feedstocks = sorted(glob.glob('*-feedstock'))
# feedstocks = ['databroker-pack-feedstock']

for project in feedstocks:
    print(f'Project name: {project}')
    existing_definitions = bclient.get_definitions(
        project=config.project_name, name=project
    )
    ed = existing_definitions[0]
    ed = bclient.get_definition(ed.id, project=config.project_name)
    variables = {}
    build_definition = get_default_build_definition(
        'nsls-ii-forge',
        project,
        config=config,
        variables=variables,
        id=ed.id,
        revision=ed.revision,
    )
    bclient.update_definition(
        definition=build_definition,
        definition_id=ed.id,
        project=ed.project.name,
    )
