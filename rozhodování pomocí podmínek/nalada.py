#Napište program, který přijme zadanou větu a zjistí, 
#zda má zadavatel spíše negativní nebo spíše pozitivní náladu. 
#Definujte si k tomu kolekci pozitivních slov a kolekci negativních slov.

spatna_nalada = ['spatne', 'nic moc', 'napicu']
dobra_nalda = ['dobry', 'skvely', 'nejlip']

nalada = input("zadejte jak se dneska mate :D")
if nalada in spatna_nalada:
    print("dneska je vam spatne ")
elif nalada in dobra_nalda:
    print("dneska je vam dobre")