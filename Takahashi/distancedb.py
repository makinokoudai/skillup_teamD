import sqlalchemy
from database import session
from tables import Stations
import sys

args = sys.argv
sta1 = args[1]
sta2 = args[2]

kilo1 = session.query(Stations.kilo).filter_by(name=sta1).first()
kilo2 = session.query(Stations.kilo).filter_by(name=sta2).first()

if kilo1[0] < kilo2[0]:
    d = (kilo1[0] - kilo2[0]) * -1
    print('{:.2f}'.format(d),end="")
else:
    d = kilo1[0] - kilo2[0]
    print('{:.2f}'.format(d),end="")

