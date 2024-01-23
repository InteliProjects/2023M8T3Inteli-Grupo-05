# Grupo-05

# Inteli - Instituto de Tecnologia e liderança

<p align="center">
  <img src="https://i.imgur.com/aIfBsxk.png" alt="Inteli logo" border="0" width="312px">
</p>

# Proposta de Arquitetura de Software

## Grupo 5 - MetaVerse

### 🚀 Integrantes
- <a href="https://github.com/CFFricks">Carolina Fricks</a>
- <a href="https://github.com/emanuelcop3">Emanuel Costa</a>
- <a href="https://github.com/FelipeSaadi">Felipe Saadi</a>
- <a href="https://github.com/JuliaTogni">Julia Togni</a>
- <a href="https://github.com/liviabonotto">Livia Bonotto</a>
- <a href="https://github.com/marcelofeitoza">Marcelo Feitoza</a>
- <a href="https://github.com/MateusGCN">Mateus Neves</a>

## 🔍 Sumário

* [Descrição](#descrição)
* [Estrutura de pastas](#-estrutura-de-pastas)
* [Documentação do sistema](#-documentação-do-sistema)
* [Instalação](#-instalação)
  * [Tecnologias](#tecnologias)
  * [Implementações](#implementações)
  * [Demo](#demo)
* [Histórico de lançamentos](#-histórico-de-lançamentos)
* [Licença/License](#-licençalicense)
* [Referências](#-referências)


## 📜Descrição

O setor de Supply Chain da META enfrenta o desafio de melhorar a precisão na classificação de dados de compras, atualmente em 65%. Este baixo índice de precisão afeta negativamente a análise de padrões de gastos, aumentando custos e impactando as relações com fornecedores, além de gerar problemas de conformidade e auditoria. A solução proposta envolve o aprimoramento da Inteligência Artificial utilizada para classificar as compras e fornecer dados mais precisos para análises detalhadas. O objetivo é redesenhar a arquitetura atual para aumentar a qualidade do software e do processo, elevando assim a taxa de precisão na classificação de dados.

**Principais melhorias da arquitetura:**

- **Acurácia do modelo:** implementação ainda não finalizada.

- **Disponibilidade:** o sistema foi aprimorado para lidar com um volume maior de solicitações simultâneas, passando de 30 para 3000 requisições simultâneas. Isso foi alcançado através da implementação de um sistema de fila com RabbitMQ e com técnicas de balanceamento de carga e escalonamento automático. Também foi implementado o uso de microserviços para desacoplar o sistema principal do componente de processamento de ordens de compra, aumentando a resiliência e a capacidade de recuperação do sistema. Essas melhorias foram essenciais para garantir um serviço contínuo e confiável, mesmo durante picos de demanda.
  
- **Segurança:** a arquitetura atualizada do sistema introduziu melhorias que incluem a implementação de JSON Web Tokens (JWT) para autenticação e controle de acesso. Esse mecanismo ajuda a garantir que apenas usuários autorizados possam acessar o sistema. Além disso, o sistema de logs foi reforçado para monitorar e registrar todas as atividades do sistema em tempo real, sendo crucial para detectar e responder a atividades suspeitas ou tentativas de acesso não autorizado, fortalecendo a proteção dos dados sensíveis.

TODO COMPLETAR MELHORIAS

## 📁 Estrutura de pastas
- 📂 __Projeto5M8__
   - 📄 [README.md](README.md)
   - 📂 __[Atual](Atual/)__
      - <a href="https://github.com/2022M2T3/Projeto4/blob/main/documentos/WAD%20-%20Yamaha%20Planning%20System.pdf"><img src="https://user-images.githubusercontent.com/99209356/174968401-abc5cae1-7a1e-4f06-aca6-c859c993c038.svg" width="18px" height="18px"></a> src
   - 📁 __[Documentação](Documentacao/)__
   - 📁 __[Novo](Novo/)__
   - 📁 __[Simulação](Simulacao/)__
   - 📂 __[src](src/)__
      - 📂 controllers
      - 📁 models
      - 📁 services
      - 📁 tests
      - 📁 utils
      - 📁 utils
      - 📂 uploads


Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>Atual</b>: Esta pasta abriga todos os arquivos que simulam o sistema/arquitetura atual da Meta.

- <b>Documentacao</b>: Esta pasta engloba toda a documentação desenvolvida neste projeto.

- <b>Novo</b>: Aqui encontram-se todos os arquivos que simulam o sistema/arquitetura que estamos desenvolvendo para a Meta.

- <b>Simulação</b>: Esta pasta contém todos os arquivos que simulam os requisitos inicialmente elencados no projeto.

- <b>src</b>: Este diretório contém todo o código-fonte criado para o desenvolvimento do projeto, incluindo backend e frontend, se aplicável.

- <b>README.md</b>:  Arquivo que atua como guia e fornece uma explicação abrangente sobre o projeto.

## 📄 Documentação do sistema
  - <a href="https://github.com/2023M8T3Inteli/Grupo-05/blob/main/Documentacao/Index.md"><img src="https://user-images.githubusercontent.com/99209356/174968401-abc5cae1-7a1e-4f06-aca6-c859c993c038.svg" width="18px" height="18px"> index.md</a> 

## 🔧 Instalação

Para a instalação desse projeto, é necessário ter alguns recursos instalados na máquina que irá executar. Nota-se que além das instalações necessárias, também destaca-se que é relevante a versão de cada uma dessas tecnologias, haja vista que podem ocorrer falhas na execução, devido a configuração do projeto.

### Tecnologias
- Python 3.12.1
- Rabbit MQ 3.10.0
- Docker 23.0.3
- Type Script ^5.3.2
- Node 14.17.6


### Implementações
- Passo a Passo de como inicicializar o sistema localmente (Docker).

```bash
  git clone https://github.com/2023M8T3Inteli/Grupo-05.git
  cd Grupo-05
```

```bash
  # Abra o Docker
```

```bash
  cd Novo/src/app
```

```bash
  # Execute o comando, para rodar o docker
  docker-compose up
```

```bash
  # Para testar os workers, acesse:
  http://localhost:5000/create-job/msg
```

```bash
  # Para testar a aplicação, acesse:
  http://localhost:3000
```

## 🗃 Histórico de lançamentos

**1.0 — 27/10/2023 (Sprint I)**

* Arquitetura do Sistema Atual - Visão Negócio (versão 1) (Visão Arquitetural - ISO 10746)

* Arquitetura do Sistema Novo - Especificação de Requisitos (Versão 1).

* Arquitetura do Sistema Novo (Versão 1.5) - Visão Modelo Comportamental (Simulação)


**2.0 — 10/11/2023 (Sprint II)**

* Arquitetura do Sistema Atual (Versão 2.0) - Avaliação dos mecanismos de engenharia e de tecnologia utilizados no sistema atual (ATAM - Architecture Tradeoff Analysis Method).

* Arquitetura do Sistema Novo (Versão 2.0). Especificação da solução técnica do novo

* Arquitetura do Sistema Novo (Versão 2.5). Simulação do Novo, incluindo as táticas e os componentes.


**3.0 — 24/11/2023 (Sprint III)**

* Implementação dos Mecanismos Arquiteturais.

* Testes automatizados, não funcionais

* Revisão do Modelo de Simulação do Novo


**4.0 — 08/12/2023 (Sprint IV)**

* Ajustes de implementação.

* Evidencias de testes não funcionais.

* Medir o novo sistema

* Identificar os tradeoffs arquiteturais
  

**5.0 — 21/12/2023 (Sprint V)**

* Revisão do Repositório Github

* Arquitetura do Sistema Novo (Versão 3.0) com as atualizações, incluindo o Storytelling de dados (Antes x Depois; Atual x Novo)


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="#">Metaverse</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="#">Inteli, Carolina Fricks, Emanuel Costa, Felipe Saadi, Julia Togni, Livia Bonotto, Marcelo Feitoza, Mateus Neves</a> is 
licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências
ADZLANI, Nasri. RabbitMQ on Docker and python. Disponível em: <https://nasriadzlani.medium.com/rabbitmq-on-docker-and-python-300e449fcc8c>. Acesso em: Nov. 2023.

ISO 25010. Disponível em: <https://iso25000.com/index.php/en/iso-25000-standards/iso-25010.> Acesso em: Out. 2023.

JAVA MODELLING TOOLS (JMT). Politecnico di Milano e Imperial College London. Disponível em: <https://jmt.sourceforge.net/.> Acesso em: Nov. 2023.

NODE.JS. Documentação da API mais recente. Disponível em: <https://nodejs.org/docs/latest/api/.> Acesso em: Out. 2023.

BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. Software Architecture in Practice. United States of America: Pearson Addison Wesley, 2021. 438p. : il. ISBN 9780136886099. Capítulos 3.3, 3.4, 3.5 e 3.7. Acesso em: Nov. 2023.


Para referenciar a apresentação "Decisões arquiteturais para micro serviços: tradeoffs, granularidade e fronteiras" de Jessilyneh, no estilo ABNT, a citação seria:

JESSILYNEH. Decisões arquiteturais para micro serviços: tradeoffs, granularidade e fronteiras. Apresentada no TDC de Porto Alegre, dezembro de 2023. Disponível em: <https://speakerdeck.com/jessilyneh/decisoes-arquiteturais-para-micro-servicos-tradeoffs-granularidade-e-fronteiras.> Acesso em: Dez. 2023.


_Alguns textos foram baseados em pesquisas no ChatGPT._ Disponível em: <https://chat.openai.com/>.

<p align="center">
  <img src="https://i.imgur.com/aIfBsxk.png" alt="Inteli logo" border="0" width="312px">
</p>

<br>
