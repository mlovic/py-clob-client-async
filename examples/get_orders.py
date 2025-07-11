import os

from py_clob_client_async.client import ClobClient
from py_clob_client_async.clob_types import ApiCreds, OpenOrderParams
from dotenv import load_dotenv
from py_clob_client_async.constants import AMOY

load_dotenv()


def main():
    host = os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    key = os.getenv("PK")
    creds = ApiCreds(
        api_key=os.getenv("CLOB_API_KEY"),
        api_secret=os.getenv("CLOB_SECRET"),
        api_passphrase=os.getenv("CLOB_PASS_PHRASE"),
    )
    chain_id = AMOY
    client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)

    resp = client.get_orders(
        OpenOrderParams(
            market="71321045679252212594626385532706912750332728571942532289631379312455583992563",
        )
    )
    print(resp)
    print("Done!")


main()
