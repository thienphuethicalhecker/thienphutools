from easyarg import AGR



parser=AGR()
parser.add_agr('--say',action='store_true',)
parser.parse_agrs()


data_say=parser.get_value('--say')
print(data_say)
