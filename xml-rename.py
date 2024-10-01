#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nome do arquivo: xml-rename
Autor: Wesley Crus
Data: 2024-10-01
Versão: 1.0
Descrição: Este script renomeia o arquivo xml com base na TAG <infNFE ID>
"""

import os
import xml.etree.ElementTree as ET

# Caminho para o diretório
diretorio = r'c:\temp\xml-rename'

# Percorre todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.xml'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Faz o parse do arquivo XML
        try:
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Define o namespace
            namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

            # Busca a tag <infNFe> com namespace
            inf_nfe = root.find('.//nfe:infNFe', namespaces)

            if inf_nfe is not None:
                # Obtém o atributo 'Id' da tag <infNFe>
                id_nfe = inf_nfe.attrib.get('Id')

                if id_nfe:
                    # Define o novo nome do arquivo
                    novo_nome = f"proc{id_nfe}.xml"
                    novo_caminho = os.path.join(diretorio, novo_nome)
                    
                    # Renomeia o arquivo
                    os.rename(caminho_arquivo, novo_caminho)
                    print(f'Renomeado: {nome_arquivo} -> {novo_nome}')
                else:
                    print(f'ID não encontrado em: {nome_arquivo}.')

            else:
                print(f'Tag <infNFe> não encontrada em: {nome_arquivo}.')

        except ET.ParseError:
            print(f'Erro ao parsear o arquivo: {nome_arquivo}.')
        except FileNotFoundError:
            print('Arquivo não encontrado.')
        except Exception as e:
            print(f'Ocorreu um erro com o arquivo {nome_arquivo}: {e}')
