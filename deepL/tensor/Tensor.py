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

        _op: Operation that originated that tensor. If none, it means that is a leaf node.

        """
        self.data = np.array(dim)
        self.grad = np.zeros_like(self.data)

    # define the fundamental operations that can be applied to the tensor.
    def __add__(self,another):
        """
        When adding to tensors, returns a tensor such that
            - the tensor is the pointwise adition of the elements of the two tensors
            - The instruction (backward method) to calculate the
        """

    def __mul__(self,another):
        ...

    def _relu(self):
        ...


    def backward():
        pass

    
        
