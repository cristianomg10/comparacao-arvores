from RedBlackTree import RedBlackTree
from AVLTree import AVLTree
from time import time
import numpy as np
import pandas as pd

num_execucoes = 10
num_dados = [10, 100, 1000, 10000, 100000, 1000000]
resultados = {
    'execucao': [],
    'num_dados': [],
    'operacao': [],
    'abordagem': [],
    'tempo_gasto': []
}


def atualiza(dicionario, valores):
    for k, v in valores.items():
        dicionario[k].append(v)

    return dicionario


for dados in num_dados:
    for execucao in range(num_execucoes):
        nums = np.random.choice(np.arange(10000000), dados, replace=False)
        bst = RedBlackTree()

        ## INSERÇÃO
        inicio = time()
        for num in nums:
            bst.insert(num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': num_dados,
            'operacao': 'insercao',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.8f}"
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo inserção RB: {fim:.8f}")

        myTree = AVLTree()
        root = None

        inicio = time()
        for num in nums:
            root = myTree.insert_node(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': num_dados,
            'operacao': 'insercao',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.8f}"
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo inserção AVL: {fim:.8f}")

        ## PESQUISA
        inicio = time()
        for num in nums:
            bst.searchTree(num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': num_dados,
            'operacao': 'pesquisa',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.8f}"
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo pesquisa RB: {fim:.8f}")

        for num in nums:
            myTree.find(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': num_dados,
            'operacao': 'pesquisa',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.8f}"
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo pesquisa AVL: {fim:.8f}")

        ## EXCLUSÃO
        inicio = time()
        for num in nums:
            bst.delete_node(num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao + 1,
            'num_dados': num_dados,
            'operacao': 'exclusão',
            'abordagem': 'Red Black',
            'tempo_gasto': f"{fim:.8f}"
        })

        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo exclusão RB: {fim:.8f}")

        for num in nums:
            root = myTree.delete_node(root, num)
        fim = time() - inicio
        resultados = atualiza(resultados, {
            'execucao': execucao+1,
            'num_dados': num_dados,
            'operacao': 'pesquisa',
            'abordagem': 'AVL',
            'tempo_gasto': f"{fim:.8f}"
        })
        print(f"Numero dados: {dados}, Execucao {execucao}, Tempo exclusão AVL: {fim:.8f}")

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
myTree.printHelper(root, "", True)
"""