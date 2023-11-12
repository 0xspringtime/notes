1.18 Definition addition, scalar multiplication
- An addition on a set $V$ is a function that assigns an element $u+v \in V$ to each pair of elements $u, v \in V$.
- A scalar multiplication on a set $V$ is a function that assigns an element $\lambda v \in V$ to each $\lambda \in \mathbf{F}$ and each $v \in V$.

1.19 Definition vector space

A vector space is a set $V$ along with an addition on $V$ and a scalar multiplication on $V$ such that the following properties hold:
commutativity
$$
u+v=v+u \text { for all } u, v \in V
$$
associativity
$$
(u+v)+w=u+(v+w) \text { and }(a b) v=a(b v) \text { for all } u, v, w \in V
$$
and all $a, b \in \mathbf{F}$;
additive identity
there exists an element $0 \in V$ such that $v+0=v$ for all $v \in V$;
additive inverse
for every $v \in V$, there exists $w \in V$ such that $v+w=0$;
multiplicative identity
$$
1 v=v \text { for all } v \in V
$$
distributive properties
$a(u+v)=a u+a v$ and $(a+b) v=a v+b v$ for all $a, b \in \mathbf{F}$ and all $u, v \in V$.

- elements of a vector space are called **vectors** or **points**

1.23 Notation $\mathbf{F}^S$
- If $S$ is a set, then $\mathbf{F}^S$ denotes the set of functions from $S$ to $\mathbf{F}$.
- For $f, g \in \mathbf{F}^S$, the sum $f+g \in \mathbf{F}^S$ is the function defined by
$$
(f+g)(x)=f(x)+g(x)
$$
for all $x \in S$.
- For $\lambda \in \mathbf{F}$ and $f \in \mathbf{F}^S$, the product $\lambda f \in \mathbf{F}^S$ is the function defined by
$$
(\lambda f)(x)=\lambda f(x)
$$
for all $x \in S$.


1.25 Unique additive identity

A vector space has a unique additive identity.

Proof Suppose 0 and $0^{\prime}$ are both additive identities for some vector space $V$. Then
$$
0^{\prime}=0^{\prime}+0=0+0^{\prime}=0,
$$
where the first equality holds because 0 is an additive identity, the second equality comes from commutativity, and the third equality holds because $0^{\prime}$ is an additive identity. Thus $0^{\prime}=0$, proving that $V$ has only one additive identity.

Each element $v$ in a vector space has an additive inverse, an element $w$ in the vector space such that $v+w=0$. The next result shows that each element in a vector space has only one additive inverse.

1.26 Unique additive inverse

Every element in a vector space has a unique additive inverse.

Proof Suppose $V$ is a vector space. Let $v \in V$. Suppose $w$ and $w^{\prime}$ are additive inverses of $v$. Then
$$
w=w+0=w+\left(v+w^{\prime}\right)=(w+v)+w^{\prime}=0+w^{\prime}=w^{\prime} .
$$

Thus $w=w^{\prime}$, as desired.


