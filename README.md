## About
Returns apr of the pair [NEAR-WETH](https://vfat.tools/aurora/auroraswap/)
## How to use
```shell
git clone https://github.com/arssing/multifarm-test
cd multifarm-test/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Go to http://127.0.0.1:8000 (wait a bit)
Example response:
{"apr":45.41}

