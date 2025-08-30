# Organizador de Arquivos

## Sobre o projeto
Este projeto foi desenvolvido como um estudo prático em Python.  
O objetivo principal foi criar uma aplicação simples para **organizar arquivos em pastas baseadas em suas extensões**, utilizando a biblioteca **CustomTkinter** para fornecer uma interface gráfica moderna.

Além da funcionalidade em si, a ideia do projeto foi exercitar boas práticas de programação e estruturação de código, buscando deixá-lo o mais **profissional e organizado** possível.  
Foram aplicados conceitos como:
- Separação clara entre lógica de negócio e interface gráfica.
- Uso de `pathlib` para manipulação de caminhos.
- Garantia de nomes únicos para evitar sobrescrita de arquivos.
- Tipagem com *type hints* para maior clareza e manutenção.
- Organização do código em classes e funções bem definidas.

## Funcionalidades
- Seleção de uma pasta através de interface gráfica.
- Organização automática de arquivos em subpastas nomeadas pela extensão.
- Arquivos sem extensão são movidos para a pasta `OUTROS`.
- Tratamento de arquivos duplicados com renomeação incremental.
- Exibição de mensagens de erro, alerta e conclusão via interface gráfica.

## Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Módulos padrão do Python: `pathlib`, `shutil`, `tkinter`
