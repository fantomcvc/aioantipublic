# Aioantipublic
Async API wrapper for antipublic.cc

## Quickstart
1. Copy `aioantipublic/` folder into your project
2. Install dependencies `pip install -r aioantipublic/requirements.txt/`
3. See examples
4. Read the [documentation](https://docs.antipublic.cc/)

## Usage
1. `from aioantipublic import AntiPublic, AntiPublicError`
2. `antip = AntiPublic()`
3. See example
```
bin_info = await antip.bin_check(bin='456647')
print(bin_info)

antipublic_check = await antip.antipublic_check(cards=["4242424242424242", "4266845237252027"])
print(antipublic_check)
```
## Exception handling

```
from aioantipublic import AntiPublic, AntiPublicError

antip = AntiPublic()
try:
	bin_info = await antip.bin_check(bin='456647')
	print(bin_info)
except AntiPublicError as e:
	print(e)
```
`> {'detail': 'BIN "111111" not found.'`
