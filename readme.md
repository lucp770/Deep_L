Em construção ...


TODO:

1) O primeiro passo é a construção de um objeto que representa os tensores. Esse objeto precisa realizar operações simples (add, mult, exp), precisa ser também capaz de armazenar o gradiente. Para isso é necessario também ter todo o grafo que representa a estrutura da rede. É a única forma de ser capaz de aplicar a regra da cadeia dentro de toda uma estrutura complexa.

2) 



# Description

Deep_L is the most explicity (but most efficient) implementation of a automatic diferentiation engine. The purpose is to write in the most explicit form the operations that are happening behind most deep learning libraries.

Most deep learning libraries (like pytorch or tensorflow) create a computational graph using tensor operations. This computational graph is a history of the operations that created the loss function. If that history is possible to know the derivative of every node in relation to the parent nodes, therefore is possible to apply the chain rule to obtain the derivative in every node.

## main features



## Tensor

A tensor in deep_L is a class that adds extra functionality to a numpy array.

Every operation that can be applied to a tensor must also be acompanied of a way of deriving this operation. For example, if a tensor C comes from the sum of A and B. Is necessary to know that 


## computational graph

In order to apply the chain rule and obtain the derivatives of the loss function in relationship with the weights is necessary to maintain in memory the history of operations that were applied to the tensors during the foward pass