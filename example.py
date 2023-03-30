import asyncio
from aioantipublic import AntiPublic, AntiPublicError


async def main():
	antip = AntiPublic()

	try:
		bin_info = await antip.bin_check(bin='456647')
		print(bin_info)

		bins_check = await antip.bins_check(bins=['456647', '424242'])
		print(bins_check)

		antipublic_check = await antip.antipublic_check(cards=["4242424242424242", "4266845237252027"])
		print(antipublic_check)
	except AntiPublicError as e:
		print(e)

if __name__ == '__main__':
	asyncio.run(main())