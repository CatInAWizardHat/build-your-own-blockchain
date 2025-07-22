# Build-your-own-blockchain

Initially followed this tutorial:
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
from the build-your-own-x repository, hence the name of the repo.

Been iterating on it in my spare time to add added functionality.

utilizes flask to create the endpoints needed to interact with the chain, run with
```bash
python blockchain.py
```

which will start the server on your machine, can be accessed through localhost.

Endpoints:
```
localhost:5000/mine
localhost:5000/transactions/new
localhost:5000/chain
localhost:5000/nodes/register
localhost:5000/nodes/resolve
```
