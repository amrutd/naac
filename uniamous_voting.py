##from mpyc.runtime import mpc
import sys
from db import db_manager

class create_survey():

    def __init__(self) -> None:
       self.question=input("Enter your Survey question: \n")
       self.answer= input("Answer type ? True/False : \n ")
       self.number= input("Number of participants : \n")

       db=db_manager()
       db.insert_into_table((self.question, self.number, 'Pending'))
       db.commit()
       db.close()

       print("""
                    \033[1m Thank you for creating the Survey \033[0m

                     """)

if __name__ == '__main__':
    obj=create_survey()







