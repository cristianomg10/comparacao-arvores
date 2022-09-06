from RedBlackTree import RedBlackTree
from AVLTree import AVLTree
from time import time
import numpy as np
import pandas as pd
import random

num_execucoes = 10
num_dados = [100, 1000, 10000, 100000, 1000000]
resultados = {
    'execucao': [],
    'num_dados': [],
    'operacao': [],
    'abordagem': [],
    'tempo_gasto': [],
    'rotacoes': [],
    'altura': []
}


def atualiza(dicionario, valores):
    for k, v in valores.items():
        dicionario[k].append(v)

    return dicionario


for dados in num_dados:
    for execucao in range(num_execucoes):
        nums = np.random.choice(np.arange(dados*2), dados, replace=False)

        bst = RedBlackTree()
        myTree = AVLTree()
        root = None

        ## INSERÇÃO
        inicio = time()
        for num in nums:
            bst.insert(num)
        fim = time() - inicio
        
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': dados,
            'operacao': 'insercao',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': bst.rotation,
            'altura': max(bst.get_height(bst.root, bst.root))+1 
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo inserção RB: {fim:.12f}, Rotações: {bst.rotation} {bst.get_height(bst.root, bst.root)}")

        inicio = time()
        for num in nums:
            root = myTree.insert_node(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': dados,
            'operacao': 'insercao',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': myTree.rotation,
            'altura': myTree.getHeight(root)
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo inserção AVL: {fim:.12f}, Rotações: {myTree.rotation} {myTree.getHeight(root)}")

        ## BUSCA
        inicio = time()
        for num in nums:
            bst.searchTree(num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': dados,
            'operacao': 'busca',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': np.nan,
            'altura': np.nan
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo pesquisa RB: {fim:.12f}")

        inicio = time()
        for num in nums:
            myTree.find(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': dados,
            'operacao': 'busca',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': np.nan,
            'altura': np.nan
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo pesquisa AVL: {fim:.12f}")

        ## EXCLUSÃO
        bst.rotation = 0
        inicio = time()
        for num in nums:
            bst.delete_node(num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao + 1,
            'num_dados': dados,
            'operacao': 'exclusão',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': bst.rotation,
            'altura': np.nan
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo exclusão RB: {fim:.12f}, Rotações: {bst.rotation}")

        myTree.rotation = 0
        inicio = time()
        for num in nums:
            root = myTree.delete_node(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': dados,
            'operacao': 'pesquisa',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.12f}",
            'rotacoes': myTree.rotation,
            'altura': np.nan
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo exclusão AVL: {fim:.12f}, Rotações: {myTree.rotation}")

pd.DataFrame(resultados).to_csv("resultados.csv", index=False)
"""
bst.print_tree()

print("\nAfter deleting an element")
bst.delete_node(40)
bst.print_tree()


    
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
"""
# myTree.printHelper(root, "", True)
