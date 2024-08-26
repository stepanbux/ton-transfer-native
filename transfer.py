#------------------------------------------------#
#                                                #
# Full script here - https://t.me/hidden_coding  #
#                                                #
#------------------------------------------------#


mnemonic = ""
mnemonics_list = mnemonic.split(" ")


# Settings
#---------------------------------
SENDER_SEED_PHRASE = ''  # v4r2 only
SENDER_ADDRESS = ''  # v4r2 only
AMOUNT = [0.01, 0.3]  # ton
USE_API_KEY = True  # or False, but much more latency and possible overload of the non-key api,
# get api key from @tonapibot (mainnet only)
API_KEY = ''
# --------------------------------


global seqno


async def initialization_wallet():
    mnemonics = SENDER_SEED_PHRASE.split(' ')

    version = WalletVersionEnum.v4r2

    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=version, workchain=0)
    return wallet


async def send(session, wallet, recipient_address, seqnoo, post_url):
    amount = round(random.uniform(AMOUNT[0], AMOUNT[1]), 4)

    query = wallet.send_ton()

    boc = "https://t.me/hidden_coding"

    json = {
        "boc": str(boc)
    }
    async with session.post(post_url, json=json) as resp:
        if resp.status == 200:
            print(f'Successfully created transaction. Sending {amount} TON to {recipient_address}...')
            return True, amount
        else:
            return False, None


async def wait_for_seqno_change(session, get_url, seqno):
    return 0


async def get_wallet_info(session, get_url):
    async with session.get(get_url) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f'Error getting wallet info: {response.status}, {response.text}, {await response.json()}')
        return None


async def main():
    global seqno
    if USE_API_KEY is True and API_KEY != '':
        get_url = f''
        post_url = f''
    else:
        get_url = f''
        post_url = f''

    with open('wallet.txt', 'r') as f:
        recipient_addresses = [line.strip() for line in f.readlines()]

    wallet = await initialization_wallet()

    async with aiohttp.ClientSession() as session:
        info = await get_wallet_info(session, get_url)
        await asyncio.sleep(1)
        if info['status'] == 'uninit':
            seqno = 0
        else:
            seqno = info['seqno']

if __name__ == "__main__":
    asyncio.run(main())
