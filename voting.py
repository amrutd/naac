import sys
from mpyc.runtime import mpc
from db import db_manager

async def main():

        m = len(mpc.parties)

        t = m//2

        voters = list(range(m))  # parties P[0],...,P[t]

        if mpc.pid in voters:
             question =db_manager().select()[0]
             answer=input('Survey Question: \n' + question + '\nYes/NO :')
             ##how=input('Do you require any specific accommodations for seating arrangements?')
             if answer.upper()=='YES':
               vote=0
             else: 
               vote=1
        else:
            vote = None 

        secbit = mpc.SecFld(9)  # secure bits over GF(2)

        await mpc.start()
        votes = mpc.input(secbit(vote), senders=voters)
        result= await mpc.output(mpc.all(votes), receivers=voters)
        await mpc.shutdown()


        if not result:
            print("""
                     \033[1mSurvery Results: Yes 

                     Message from instructor:

                     The instructor will discuss with the class to 
                     arrange seating accommodations. \033[0m
                     """)
        else:
            print(f'Survery Results: \nNo')


if __name__ == '__main__':
    mpc.run(main())








