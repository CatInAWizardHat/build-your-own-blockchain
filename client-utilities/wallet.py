import json
from sys import argv
from ecdsa import SigningKey, VerifyingKey, NIST384p


def generate_keys():
    """
    Generate a key-pair to use with our blockchain.
    """
    sk = SigningKey.generate(NIST384p)
    vk = sk.verifying_key

    private_key_string = sk.to_string().hex()
    public_key_string = vk.to_string().hex()

    wallet_data = {
        "private_key": private_key_string,
        "public_key": public_key_string,
    }

    with open("wallet.json", "w") as f:
        json.dump(wallet_data, f, indent=4)

    print("Wallet keys generated, saved to wallet.json")


def sign(recipient, amount):
    """
    Create a signature for transactions using our private_key, the recipient and amount
    """

    with open("wallet.json", "r") as f:
        wallet_data = json.load(f)
        loaded_private_key = SigningKey.from_string(
            bytes.fromhex(wallet_data["private_key"]), curve=NIST384p
        )
        loaded_public_key = VerifyingKey.from_string(
            bytes.fromhex(wallet_data["public_key"])
        )

    signature = loaded_private_key.sign(
        "{recipient} {amount}".format(recipient, amount).encode()
    )

    assert loaded_public_key.verify(
        signature, "{recipient} {amount}".format(recipient, amount).encode()
    )


if __name__ == "__main__":
    if argv[1] == "generate":
        generate_keys()
    elif argv[1] == "sign":

