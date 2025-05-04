"""
Key Mutation — утилита для анализа истории публичных ключей по Bitcoin-адресу.
"""

import requests
import sys

def fetch_transactions(address):
    url = f"https://blockstream.info/api/address/{address}/txs"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def extract_pubkeys(tx_list, address):
    pubkeys = set()
    for tx in tx_list:
        for vin in tx.get("vin", []):
            scriptsig = vin.get("scriptsig_asm", "")
            if address in scriptsig or "OP_CHECKSIG" in scriptsig:
                parts = scriptsig.split(" ")
                for part in parts:
                    if part.startswith("02") or part.startswith("03") or part.startswith("04"):
                        if len(part) in (66, 130):  # compressed / uncompressed pubkey
                            pubkeys.add(part)
    return pubkeys

def main(address):
    print(f"🔍 Анализ адреса: {address}")
    txs = fetch_transactions(address)
    pubkeys = extract_pubkeys(txs, address)

    if not pubkeys:
        print("⚠️ Не удалось извлечь публичные ключи. Возможно, адрес ещё не тратил средства.")
    elif len(pubkeys) == 1:
        print("✅ Публичный ключ неизменен. Безопасно.")
    else:
        print(f"⚠️ Обнаружено {len(pubkeys)} различных публичных ключей!")
        for pk in pubkeys:
            print(f" - {pk[:16]}...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python key_mutation.py <bitcoin_address>")
        sys.exit(1)
    main(sys.argv[1])
