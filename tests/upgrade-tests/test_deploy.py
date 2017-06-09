import pytest
from utils import temporary_model, wait_for_ready
from validation import validate_all

test_cases = [
    # bundle                 # channel
    ('kubernetes-core',      'edge'),
    ('canonical-kubernetes', 'edge'),
]


@pytest.mark.asyncio
@pytest.mark.parametrize('bundle,channel', test_cases)
async def test_deploy(bundle, channel):
    async with temporary_model() as model:
        await model.deploy(bundle, channel=channel)
        await wait_for_ready(model)
        await validate_all(model)