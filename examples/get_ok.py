import asyncio
import os
from py_clob_client_async.client import ClobClient


async def main():
    host = os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    client = ClobClient(host)

    result = await client.get_ok()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
