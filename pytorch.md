# backward

- Tensor is in torch/_tensor.py 
- Tensor.backward calls  torch.autograd.backward(
            self, gradient, retain_graph, create_graph, inputs=inputs
        )
- autograd backward is in torch/autorgrad/__init__.py
- autograd.backward creates or uses a couple variables such as grad_tensors_ and retain_graph, and finally calls : _engine_run_backward(
                        tensors,
                        grad_tensors_,
                        retain_graph,
                        create_graph,
                        inputs,
                        allow_unreachable=True,
                        accumulate_grad=True,
                    )

- _engine_run_backward is in torch/autograd/graph and calls Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
            t_outputs, *args, **kwargs
        )  # Calls into the C++ engine to run the backward pass

- Variable is defined in torch/autograd/variable.py.
- Variable is a class that inherits from torch._C._LegacyVariableBase and sets _execution_engine = torch._C.ImperativeEngine()

- LegacyVariableBase and ImperativeEngine are defined on ...
