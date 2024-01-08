#Nejlepší hráči

#Mějme seznam hráčů a jejich nahrané skóre ve hře:
#Vypište na obrazovku hráče v pořadí od nejlepšího po nejhoršího a jen ty nejlepší 3 (top-3).


hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]


sorted_players = sorted(hraci, key=lambda x: x[1], reverse=True)


top_3_players = sorted_players[:3]


for i, (player, score) in enumerate(top_3_players, start=1):
    print(f"{i}. {player}: {score} bodů")
