import os

#senha = 'My password'
senha = 'My Password'

'''
Mapeamento dos Host
'''
host={'h1':'00:00:00:00:01:01',
      'h2':'00:00:00:00:01:02',
      'h3':'00:00:00:00:02:03',
      'h4':'00:00:00:00:02:04',
      'h5':'00:00:00:00:04:05',
      'h6':'00:00:00:00:04:06',
      'srv1':'00:00:00:00:03:11',
      'srv2':'00:00:00:00:03:12'}
'''
Mapeamento dos Swicth
'''
switch={'s1':['1','2','12','13','14'],
        's2':['1','2','11','13','14'],
        's3':['1', '2','11','12','14'],
        's4':['1','2','11','12','13']}

'''
Mapeamento das Conexoes
'''
conexoes={'h1':['s1',1],
          'h2': ['s1',2],
          'h3': ['s2',1],
          'h4': ['s2',2],
          'h5': ['s4',1],
          'h6': ['s4',2],
          'srv1':['s3',1],
          'srv2':['s3',2]}
'''
Mapeamento dos links principais
'''
linkPrincipal={'s1':[13],
                's2':[13],
                's4':[13],
                's3':[11,12,14]

}
def executaComandosOVS(comando):
    text = os.popen("echo %s | sudo -S %s" % (senha, comando))
'''
Define regras de saida dos hosts nos switchs
'''


listaConexoes = []

for i in conexoes:
    listaConexoes.append(i)
for i in listaConexoes:
    comando = 'ovs-ofctl add-flow ' + conexoes[i][0] + ' dl_dst=' + host[i] + ',actions=output:' +str(conexoes[i][1])
    executaComandosOVS(comando)


'''
Define as outras regras de saida
'''


listaSwitches = []
listaHosts = []
for i in switch:
    listaSwitches.append(i)
for i in host:
    listaHosts.append(i)

for i in listaSwitches:
    #print('Switch '+i)
    if(len(linkPrincipal[i]) == 1):
        for j in listaConexoes:
            if(conexoes[j][0] != i): #Somente para fora do switch
                comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',actions=output:'+str(linkPrincipal[i][0])
                executaComandosOVS(comando)
    else:
        for j in listaConexoes:
            if(conexoes[j][0] != i): #Somente para fora do switch
                #Verificar para qual suite ele vai
                lista = host[j].split(':')
                lista = lista[4]
                switch_alvo = 's'+lista[1]
                if(switch_alvo == 's1'):
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',actions=output:11'
                    executaComandosOVS(comando)
                elif(switch_alvo == 's2'):
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',actions=output:12'
                    executaComandosOVS(comando)
                else:
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',actions=output:14'
                    executaComandosOVS(comando)



'''
listaConexoes = []

for i in conexoes:
    listaConexoes.append(i)
for i in listaConexoes:
    comando = 'ovs-ofctl add-flow ' + conexoes[i][0] + ' dl_dst=' + host[i] +',nw_proto=1'+ ',actions=output:' +str(conexoes[i][1])
    executaComandosOVS(comando)

listaSwitches = []
listaHosts = []
for i in switch:
    listaSwitches.append(i)
for i in host:
    listaHosts.append(i)

for i in listaSwitches:
    #print('Switch '+i)
    if(len(linkPrincipal[i]) == 1):
        for j in listaConexoes:
            if(conexoes[j][0] != i): #Somente para fora do switch
                comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',nw_proto=1'+',actions=output:'+str(linkPrincipal[i][0])
                executaComandosOVS(comando)
    else:
        for j in listaConexoes:
            if(conexoes[j][0] != i): #Somente para fora do switch
                #Verificar para qual suite ele vai
                lista = host[j].split(':')
                lista = lista[4]
                switch_alvo = 's'+lista[1]
                if(switch_alvo == 's1'):
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',nw_proto=1'+',actions=output:11'
                    executaComandosOVS(comando)
                elif(switch_alvo == 's2'):
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',nw_proto=1'+',actions=output:12'
                    executaComandosOVS(comando)
                else:
                    comando = 'ovs-ofctl add-flow ' + i + ' dl_dst='+ host[j]+',nw_proto=1'+',actions=output:14'
                    executaComandosOVS(comando)
'''
