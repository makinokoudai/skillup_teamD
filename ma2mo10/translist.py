import sys
from DB.database import session
from transport_table import Transport

args = sys.argv

filename = "../../output/" + args[1]

translist = session.query(Transport).all()

with open(filename, mode='w', encoding='utf-8') as f:
    for trans in translist:
        f.write(f'"{trans.date}","{trans.seq}","{trans.depature}","{trans.arrival}","{trans.via}","{trans.amount}"\n')
