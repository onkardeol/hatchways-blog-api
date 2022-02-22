import asyncio
from methodtools import lru_cache
import json
from sys import platform

import aiohttp

API_ENDPOINT = "https://api.hatchways.io/assessment/blog/posts?tag="


class HatchwaysFacade:

    # Using 16 as max size for proof of concept, can be changed a higher number
    # Set maxsize as 2**n for optimal caching (less resizing will occur)
    @lru_cache(maxsize=16)
    def fetch_blogs(self, tags):
        # Removing duplicate tags
        tags = set(tags.split(","))
        blog_set = {}

        # This line is required on machines running Windows to prevent Async Event Loop exception
        if platform.startswith("win"):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._get_blogs_parallel(blog_set, tags))
        loop.close()

        return blog_set

    async def _get_blogs_parallel(self, blogs, tags):
        async with aiohttp.ClientSession() as session:
            ret = await asyncio.gather(
                *[self._fetch_blogs_parallel(blogs, tag, tags, session) for tag in tags]
            )

    async def _fetch_blogs_parallel(self, blogs, tag, tags, session):
        async with session.get(url=API_ENDPOINT + tag) as response:
            resp = await response.read()
            json_data = json.loads(resp)

            for post in json_data["posts"]:
                blogs[post["id"]] = post
