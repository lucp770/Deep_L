import numpy as np 

class Tensor:

    """
        Tensor is an object that stores a multidimensional array, the gradient and the list of
        connected nodes in the computational graph. It is necessary to track the parent nodes
        to apply the chain rule during the backward step
    """

    def __init__(self, dim: tuple, _children =(), _op=None):
        """
        _children: The list of children of this node in the computational graph.
                    children is 
        _op: Operation that originated that tensor. If none, it means that is a leaf node.

        """
        self.data = np.array(dim)
        self.grad = np.zeros_like(self.data)
        self._backward = lambda: None #standard derivative for the tensor is an empty function
        self.__previous = _children


    # define the fundamental operations that can be applied to the tensor.
    def __add__(self,other)->'Tensor':
        """
        When adding to tensors, returns a tensor such that
            - the tensor is the pointwise adition of the elements of the two tensors
            - The instruction (backward method) to calculate the

        return: a Tensor object where 
        """

        other = other if isinstance(other, Tensor) else Tensor(other)
        output = Tensor(self.data + other.data, (self,other), op='+')

        def _backward():
            #TODO: I DONT UNDERSTAND THIS. WHY THE SUM ??
            self.grad += output.grad
            other.grad += output.grad

        output._backward = _backward

        return output

        

    def __mul__(self,other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        pass

    def _relu(self):
        ...


    def backward():
        pass

    
        
