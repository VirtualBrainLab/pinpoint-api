from pinpoint_api.models.transforms import qiu2018, dorr2018, dorr2018_ibl, default

transforms = [qiu2018, dorr2018, dorr2018_ibl, default]

for transform in transforms:
    with open(f'../models/{transform.name}.json', 'w') as file:
        file.write(transform.model_dump_json())