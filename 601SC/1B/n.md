### State Machines

- State Machines: method of modeling systems whose output depends on the entire history of their inputs, and not just on the most recent input

-  can think of the job of an embedded system as performing a transduction from a stream (infinite sequence) of input values to a stream of output values

- We can represent a transducer as a state machine (SM) using the following KaTeX notation:

$$\text{{Transducer}} = (S, I, O, n, o, s_0)$$

where:
- $S$ represents the set of states,
- $I$ represents the set of inputs (input vocabulary),
- $O$ represents the set of outputs (output vocabulary),
- $n(it, st) \to st+1$ represents the next-state function, mapping the input at time $t$ and the state at time $t$ to the state at time $t+1$,
- $o(it, st) \to ot$ represents the output function, mapping the input at time $t$ and the state at time $t$ to the output at time $t$, and
- $s_0$ represents the initial state, which is the state at time 0.

- Cascade Composition:  take two machines and use the output of the first one as the input to the second

- Parallel Composition: two machines run side by side with output of of composite machine being pair of outputs by individual machines

- ParallelAdd: just like Parallel, except that it has a single output whose value is the sum of the outputs of the constituent machines

- Plant: factory or other external environment that we might wish to control; output usually thought of as sensory observations

