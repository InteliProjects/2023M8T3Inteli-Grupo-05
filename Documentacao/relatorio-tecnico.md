# RELATÓRIO TÉCNICO
## Case Meta

### Grupo: 
Verse

### Integrantes:
- <a href="https://github.com/CFFricks">Carolina Fricks</a>
- <a href="https://github.com/emanuelcop3">Emanuel Costa</a>
- <a href="https://github.com/FelipeSaadi">Felipe Saadi</a>
- <a href="https://github.com/JuliaTogni">Julia Togni</a>
- <a href="https://github.com/liviabonotto">Livia Bonotto</a>
- <a href="https://github.com/marcelofeitoza">Marcelo Feitoza</a>
- <a href="https://github.com/MateusGCN">Mateus Neves</a>


### Business Drivers

Os Business Drivers para este projeto incluiem:

#### Eficiência Operacional:
- Automatização da categorização para reduzir tarefas manuais.
- Otimização dos processos relacionados à gestão de despesas.

#### Redução de Custos:
- Minimização de erros humanos resultando em economias operacionais.
- Eliminação de retrabalho associado a classificações incorretas.

#### Melhoria na Tomada de Decisões:
- Fornecimento de dados categorizados de forma precisa e eficiente.
- Capacidade aprimorada de análise para suporte a decisões estratégicas.

#### Vantagem Competitiva:
- Agilidade em ambientes de negócios competitivos.
- Adoção de tecnologias avançadas para se destacar no mercado.

#### Conformidade e Transparência:
- Garantia de conformidade com regulamentações.
- Transparência nas operações financeiras.

### Riscos e Oportunidades como Requisitos Não Funcionais

Identificar riscos e oportunidades e transformá-los em requisitos não funcionais (RNFs) é um passo crucial para assegurar que o sistema atenda às necessidades do negócio. Isso inclui garantir uma acurácia de classificação superior a 80%, lidar com um volume de até 3000 solicitações simultâneas, e implementar robustos mecanismos de segurança e autenticação.


### Seleção e Foco dos RNFs

A seleção dos RNFs foi orientada pelos principais desafios do processo e expectativas de negócios, concentrando-se em:
- **Acurácia na Categorização**: Melhorar a precisão na classificação de dados para mais de 80% (RNF2) e fornecer faixas de confiança da categorização (RNF3). 
- **Disponibilidade**: Capacidade de processar 3000 ordens de compra simultâneas, sendo 90% processadas em até 3 minutos (RNF1).
- **Segurança**: Fortalecimento dos protocolos de segurança, incluindo a implementação de JWT para autenticação (RNF4) um sistema de logs robusto para garantir o monitoramento do sistema (RNF5).

Para ver mais detalhadamente sobre os requisitos, veja a seção [Mapeamento dos requisitos do sistema novo](https://github.com/2023M8T3Inteli/Grupo-05/blob/main/Documentacao/Index.md#mapeamento-dos-requisitos) na documentação do projeto.


### Simulação do Sistema Atual

#### Simulação da precisão do Sistema Atual

Os elementos que foram utilizados para a realização da simulação atual foram:

-   Saída de categorização correta (65%).
-   Saída de categorização incorreta (35%).

A simulação foi baseada na premissa de que a assertividade do sistema não está dentro dos parâmetros aceitáveis da regra de negócios da empresa e que, com essa simulação, poderemos comprovar que existe o descumprimento de um dos requisitos não funcionais do sistema.

Taxa de acerto (65%)
![image](https://github.com/2023M8T3Inteli/Grupo-05/assets/54749257/feae54ac-5a35-4fdd-8d23-61400bde7730)

Taxa de erro (35%)
![image](https://github.com/2023M8T3Inteli/Grupo-05/assets/54749257/d9a2e87a-fbda-438e-8f8b-1e5972320d35)

Analisando os resultados da simulação do sistema atual, podemos observar que, nos cinco módulos da simulação, as taxas de assertividade se mantiveram constantes: 65% de assertividade e 35% de erro. Isso já era esperado, visto que uma das premissas da simulação era a baixa taxa de confiabilidade na assertividade do sistema.



#### Simulação da capacidade de processamento do Sistema Atual

Os elementos que foram utilizados para a realização da simulação atual foram:

-   Input de requisições que começa em 20 e aumenta constantemente até 40.
-   Um servidor responsável por todo o processamento do sistema, atendendo até 30 requisições por minuto.
  
A simulação foi baseada na premissa de que a assertividade do sistema não está dentro dos parâmetros aceitáveis da regra de negócios da empresa e que, com essa simulação, poderemos comprovar que existe o descumprimento de um dos requisitos não funcionais do sistema.

Capacidade de processamento(30)
![image](https://github.com/2023M8T3Inteli/Grupo-05/assets/54749257/cf910450-8827-495e-b47f-febe3ad1574c)

A simulação do sistema atual revelou limitações quanto à capacidade de processamento simultâneo (limitado a 30 requisições). Isso impactou negativamente na eficiência operacional do sistema.


### Decisões Arquiteturais e Simulação

Para identificar as melhores abordagens a serem implementadas efetuamos diversas simulações utilizando a ferramenta Java Modelling Tools (JMT), por meio dela atestamos que para chegar em um melhor resultado de disponibilidade e de performance seria necessário o desacoplamento do sistema em 3 serviços de processamento, que necessitariam de um sistema de fila para orquestramento das solicitações. Nas simulações, essa abordagem foi responsável pela capacidade de processar fluidamente 3000 invoices simultâneas, com base nesse estudo, investimos nas implementações necessárias para alcançar esse resultado. 

Foram implementadas estratégias de escalabilidade e processamento paralelo, juntamente com técnicas avançadas de machine learning com o Lhama para melhorar a acurácia na categorização. O uso de filas de processamento (RabbitMQ) e microserviços escaláveis foi crucial para aprimorar a disponibilidade e a performance do sistema, de forma que o sistema agora é capaz de funcionar de forma 100% assíncrona, lidando efetivamente com altas cargas de solicitações para serem processadas em background. 

Para chegar nesse resultado utilizamos uma fila em RabbitMQ implementada no servidor principal para receber as solicitações de invoices a serem processadas, 3 workers são responsáveis por receber as solicitações dessa fila e processá-las, garantindo uma maior performance para o servidor principal pela redução de sua carga. 

Para garantir a comunicação assíncrona entre a interface-cliente e as APIs, utilizamos da tecnologia de websocket, essa abordagem proporcionou a funcionalidade do usuário receber uma notificação quando as solicitações terminarem de serem processadas pelo nosso servidor de processamento. Para notificar o usuário, temos um worker de notificação que recebe a informação das Invoices que já foram processadas e notifica o usuário solicitante por meio do websocket.

Como adicional, implementamos alguns mecanismos de segurança para proteger o sistema de acessos indevidos. Para resolver minimamente esse problema implementamos a permissão de acesso apenas com as credenciais da Meta, assim como a tecnologia de JWT para autenticar usuários que possuem credênciais válidas, permitindo-os a acessarem o sistema.


### Medições Finais

As medições finais destacaram avanços substanciais em termos de desempenho, capacidade de processamento e precisão na categorização de dados. As melhorias alcançadas validam as decisões arquiteturais adotadas e destacam a eficácia do sistema aprimorado.

#### Principais Métricas:

#### *Tempo de Resposta Aprimorado:*
- Antes: Limitação no envio de invoices
- Depois: Implementação de sistema de fila
- **Melhorias observadas:** Anteriormente, o sistema enfrentava desafios devido à ausência de uma abordagem eficiente para lidar com solicitações simultâneas de invoices. A implementação de um sistema de fila proporcionou uma resposta mais ágil, eliminando gargalos e garantindo maior previsibilidade nos tempos de processamento. Os usuários agora experimentam uma interação mais rápida e eficiente com o sistema, resultando em uma experiência aprimorada.

#### *Capacidade de Processamento Otimizada:*
- Antes: Limitação de 30 invoices por minuto
- Depois: Capacidade de 3000 processamentos de invoices por minuto
- **Melhorias observadas:** Antes das mudanças arquiteturais, o sistema estava restrito a processar apenas 30 invoices por minuto, limitando sua escalabilidade. A reestruturação permitiu uma otimização significativa, capacitando o sistema para processar até 3000 invoices por minuto. Essa melhoria substancial na capacidade de processamento garante que o sistema seja capaz de lidar com cargas elevadas de maneira eficaz, atendendo às demandas crescentes de processamento de dados.

#### *Precisão na Categorização:*
- Antes: Acurácia de 65%
- Depois: Aumento na acurácia do sistema ao implementar nossa IA com o Llama (IA da Meta)
- **Melhorias observadas:** A acurácia anterior de 65% na categorização indicava uma margem considerável de categorizações incorretas. A introdução da IA com o Llama, uma tecnologia avançada da Meta, resultou em uma significativa melhoria na precisão da categorização. A IA aprimorada agora realiza análises mais sofisticadas, reduzindo consideravelmente os erros e proporcionando uma categorização mais precisa e confiável dos dados. Essa melhoria tem impacto direto na confiabilidade das informações geradas pelo sistema.


### Avaliação dos Resultados

As medições finais confirmam o impacto positivo das decisões arquiteturais e implementações realizadas. O sistema agora opera com maior eficiência, oferecendo respostas mais rápidas, aumentando a capacidade de processamento e elevando a precisão na categorização de dados. Esses resultados são reflexo do compromisso com a excelência arquitetural e inovação tecnológica, proporcionando uma solução mais robusta e alinhada às demandas do ambiente empresarial.

