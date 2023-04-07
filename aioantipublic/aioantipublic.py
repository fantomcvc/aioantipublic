import asyncio
import aiohttp
from typing import Dict, List, Optional
import platform
from pydantic import validate_arguments, HttpUrl


if platform.system() == "Windows":
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AntiPublicError(Exception):
	pass


class AntiPublic:

	def __init__(self) -> None:
		self.path_bins_prefix = "https://bins.antipublic.cc/bins"
		self.path_api_prefix = "https://api.antipublic.cc/cards"

	@validate_arguments
	async def bin_info(
			self,
			bin: str
		) -> Dict:
			"""Получить информацию об одном бине
			Args: 
				bin (str): BIN или номер карты
			Returns:
				Dict: {
					"bin": "426684",
					"brand": "VISA",
					"country": "US",
					"country_name": "UNITED STATES",
					"country_flag": "🇺🇸",
					"country_currencies":
					[
						"USD",
						"USN",
						"USS"
					],
					"bank": "JPMORGAN CHASE BANK N.A.",
					"level": "CLASSIC",
					"type": "CREDIT"
				}
			"""

			method = "GET"
			url = self.path_bins_prefix + f"/{bin}"
			return await self._request(method, url)

	
	@validate_arguments
	async def bin_info_list(
			self,
			bins: list,
		) -> Dict:
			"""Получить информацию о нескольких бинах (до 100)
			Args: 
				bins (list): Список бинов или номеров карт
			Returns:
				Dict: [
					{
						"bin": "426684",
						"brand": "VISA",
						"country_name": "UNITED STATES",
						"country": "US",
						"country_flag": "🇺🇸",
						"country_currencies":
						[
							"USD",
							"USN",
							"USS"
						],
						"bank": "JPMORGAN CHASE BANK N.A.",
						"level": "CLASSIC",
						"type": "CREDIT"
					}
				]
			"""
			method = "POST"
			url = self.path_bins_prefix
			json = bins
			return await self._request(method, url, json)
	
	@validate_arguments
	async def check_public(
			self,
			cards: list,
		) -> Dict:
			"""Получить информацию об одной или нескольких картах (до 100)
			Args: 
				cards (list): Список номеров карт
			Returns:
				Dict: {
					"public":
					[
						"4242424242424242"
					],
					"private":
					[
						"4266845237252027"
					],
					"private_percentage": 50
				}
			"""
			method = "POST"
			url = self.path_api_prefix
			json = cards
			return await self._request(method, url, json)

	async def _request(self, method, url, json=None) -> Dict:

		headers = {
			"Content-Type": "application/json",
		}


		async with aiohttp.ClientSession() as session:
			async with session.request(
					method, url, headers=headers, json=json
				) as response:
				result = await response.json()
				if isinstance(result, dict) and 'detail' in result:
					raise AntiPublicError(result)
				else:
					return result
