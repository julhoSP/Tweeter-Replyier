import tweepy
import time


CONSUMER_KEY = '' #Use sua chave aqui 
CONSUMER_SECRET = '' #Use sua chave aqui 
ACCESS_KEY = '' #Use sua chave aqui 
ACCESS_SECRET = '' #Use sua chave aqui 

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILENAME = 'ultimo_id_visto.txt' 

#Função de leitura do arquivo aonde salvaremos o ultimo id
def retrive_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#Função aonde escreveremos o ultimo id
def store_last_seen_id(file_name,last_id):
    f_write = open(file_name,'w')
    f_write.write(str(last_id))
    f_write.close()
    return


def reply_mentions():
    last_seen_id = retrive_last_seen_id(FILENAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extend')

    for mention in reversed(mentions):
        print(str(mention.id) +' - '+mention.text)
        last_seen_id = mention.id
        store_last_seen_id(FILENAME,last_seen_id)
        if '#helloworld' in mention.text.lower():
            api.update_status('@' + mention.user.screen_name + '#HelloWorld pra tu rapa', mention.id)

#loop de resposta
while True:
    reply_mentions()
    time.sleep(20)
