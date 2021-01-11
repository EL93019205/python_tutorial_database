"""
main
"""
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('mysql+pymysql:///test_mysql_database2')

Base = sqlalchemy.ext.declarative.declarative_base()


# pylint: disable=R0903
class Person(Base):
    """
    Person
    """
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# pylint: disable=E1101
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michael'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
