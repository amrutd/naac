create_survey:
	poetry run python uniamous_voting.py

complete_survey:
	poetry run python voting.py -M3 -I${count} --no-log


