---
layout: post
title: The Malliavin Derivative 1
subtitle: Part 3 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin derivative, Chaos Expansion, Malliavin calculus]
authorpost: L. Llamazares-Elias
---

#  Three line summary

-   The Malliavin derivative is an operator defined by manipulating the
    chaos expansion of a square-integrable random variable.

-   The Malliavin derivative transforms square-integrable variables into
    square integrable processes.

-   The Malliavin derivative shares some properties with the classic
    derivative such as the product rule and chain rule, but the
    fundamental theorem of calculus only holds in some special cases.

# Why should I care?

The Malliavin derivative is (somewhat unsurprisingly) a fundamental
object of Malliavin calculus and has many applications in finance,
numerical methods, and optimal control.

# Notation

The same as in previous [posts](https://nowheredifferentiable.com/2022-05-26-Malliavin-Calculus-1/#:~:text=Iterated%20integrals-,We%20will%20write,-F). Furthermore we will shorten the notation
$L^2(\Omega,\mathcal{F}\U T)$ and
$L^2(I\times\Omega,\mathcal{B}(I)\otimes \mathcal{F}\U T)$ to
$L^2(\Omega)$ and $L^2(I\times\Omega)$ respectively.

# Introduction

The Malliavin derivative was originally introduced as an operator
associated with the Fréchet differential of random variables
$X: C(I)\to {\mathbb R}$. The aforementioned construction provides some
motivation behind the Malliavin derivative and will be developed in the
next post. However, a more general construction can be obtained via the
chaos expansion.


**Definition 1**. Given $X=\sum\U {n=0}^{\infty} I\U n(f\U n)\in L^2(\Omega)$
we say that $X$ is Malliavin differentiable if


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}:=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}<\infty,$$
</div>


and denote the space of Malliavin differentiable functions by


<div>
 $$\mathbb{D}\U {1,2}:=\{X\in L^2(\Omega):\|X\|\U {\mathbb{D}\U {1,2}}<\infty\}.$$
</div>


Furthermore, we define the Malliavin derivative of $X$ as


<div>
 $$D\U tX:=\sum\U {n=1}^{\infty} n I\U {n-1}(f\U {n}(\cdot ,t)),$$
</div>



These kinds of manipulations of the terms in the chaos expansion should be familiar from our [definition of the Skorohod integral](https://nowheredifferentiable.com/2022-06-10-Malliavin-Calculus-2/#:~:text=the%20Skorohod%20integral.-,Definition%201.%20Let,-X%E2%88%88). Note for example that $f\U {n}(\cdot ,t)$ is a square integrable symmetric function of $n-1$ variables and thus the terms $I\U {n-1}(f\U {n}(\cdot ,t))$ make sese. This checked, the first questions to be asked is: "what kind of object is the
Malliavin derivative of a random variable? What is the link between
$\mathbb{D}\U {1,2}$ and $D\U t$? Is $\|\cdot \|\U {\mathbb{D}\U {1,2}}$ even a
norm?" We answer this in the next proposition and corollary.


**Proposition 1**. The Malliavin derivative is well defined on
$\mathbb{D}\U {1,2}$ and establishes a linear isometry

<div>
 $$\begin{aligned}
        D: (\mathbb{D}\U {1,2},\|\cdot \|\U {\mathbb{D}\U {1,2}}) & \longrightarrow L^2(I\times\Omega,\|\cdot \|\U {L^2(I\times\Omega)}) \\
        X                                                   & \longmapsto D  X
        .\end{aligned}$$
</div>





Proof. The proof of the first part of the proposition is a
straightforward application of Itô's $n$-th isometry and the monotone
convergence theorem as we have that

<div>
 $$\begin{gathered}
        \|D  X\|^2\U {L^2(I\times\Omega)}=\int\U {I}\|\sum\U {n=1}^{\infty} n I\U {n-1}(f\U {n}(\cdot ,t))\|\U {L^2(\Omega)}^2 d t\\=\sum\U {n=1}^{\infty} n^2(n-1)!\int\U {I}\|f\U n(\cdot ,t)\| dt=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}=\norm{X}\U {\mathbb{D}\U {1,2}}.
    \end{gathered}$$
</div>

  Finally, the linearity of $D$ follows from the
linearity of the iterated Itô integrals (which itself is a consequence
of the linearity of the Itô integral). ◻


In summary, the Malliavin derivative turns a square-integrable random
variable into a possibly non-adapted, stochastic process. You may recall
from our previous posts that we had an operator that went in the
opposite direction. The Skorohod integral $\delta$. In fact, the
Malliavin derivative and the Skorohod integral are adjoint operators in
a sense that will be made precise in the next post. For now, we show
that, as occurs with the ordinary derivative, a random variable has
Malliavin derivative $0$ if and only if it is constant.


**Corollary 1**. $(\mathbb{D}\U {1,2},\norm{\cdot }\U {\mathbb{D}\U {1,2}})$ is
a seminormed space. Furthermore


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}=0 \iff DX=0\iff X\in {\mathbb R}.$$
</div>





Proof. The triangle inequality and the absolute homogeneity are direct
consequences of the isometry of the previous proposition. This shows
that $\norm{\cdot }\U {\mathbb{D}\U {1,2}}$ is a seminorm. The second part
follows from the fact that


<div>
 $$\|X\|\U {\mathbb{D}\U {1,2}}=\sum\U {n=1}^{\infty} n n!\|f\U {n}\|\U {L^2(\zl 0,T\zr ^n)}.$$
</div>


So $\norm{X}\U {\mathbb{D}\U {1,2}}=0$ if and only if $f\U n=0$ for all
$n\geq 1$, which in turn is equivalent to $X=I\U 0(f\U 0):=f\U 0$. Where we
recall that by convention $L^2 (S_0):={\mathbb R}$ and $I\U 0$ was
defined as the identity on ${\mathbb R}$. This concludes the proof. ◻


Before moving on we show a motivating example. Let us consider some
deterministic function $f\in L^2(I)$ and set


<div>
 $$X:=\delta(f)= \int\U I f(s)dW(s).$$
</div>

  Then, by construction, we have
$X=I\U 1(f)$ so

<div>
 $$D\U t X= I\U 0(f(t))=f(t).$$
</div>

  This is a nice result and it
might suggest something akin to the fundamental theorem of calculus such
as $D\U t(\delta Y)=Y(t)$ for any Skorohod integrable process $Y$. However,
this will not hold in general and as, will be seen in the next post,
occurs if and only if $Y$ is a deterministic function in $L^2(\Omega)$.\
\
This said, we now show that $\mathbb{D}\U {1,2}$ is closed in the sense
that: given a convergent sequence $X\U m\to X$, if the derivatives
$DX\U m$ converge then also $D X\U m\to D X$.


**Proposition 2**. Let $X\U m \in \mathbb{D}\U {1,2}$ such that $X\U m$ is a
Cauchy sequence in both $L^2(\Omega)$ and in $\mathbb{D}\U {1,2}$. Then,
there exists $X \in \mathbb{D}\U {1,2}$ such that


<div>
 $$\lim\U {m \to \infty}\|X\U m-X\|\U {L^2(\Omega)}=\lim\U {n \to \infty}\|DX\U m-DX\|\U {L^2(I\times\Omega)}.$$
</div>





Proof. First of all, we note that since $L^2(\Omega)$ is complete
$X\U m$ must converge to some $X\in L^2(\Omega)$. Let us write the
respective chaos expansions as


<div>
 $$X=\sum\U {n=0}^{\infty} I\U n(f\U n);\quad X\U m=\sum\U {n=0}^{\infty} I\U n(f\U n^{(m)}).$$
</div>


By Itô's isometry and the convergence $X\U m\to X\in L^2(\Omega)$ we
deduce that also $f^{(m)}\U n\to f\U n\in L^2(I^n)$ for each $n$. By now
applying Fatou's lemma and the fact that $X\U m$ is by hypothesis Cauchy
in $\mathbb{D}\U {1,2}$ we obtain that

<div>
 $$\begin{gathered}
        \lim\U {m \to \infty}\|X-X\U m\|\U {\mathbb{D}\U {1,2}}=\lim\U {m \to \infty}\sum\U {n=1}^{\infty} n!n \|f\U n(x)-f\U n^{(m)}\|\U {L^2(I^n)}\\\leq \lim\U {m \to \infty}\liminf\U {k \to \infty}\sum\U {n=1}^{\infty} n!n \|f\U n^{(k)}(x)-f\U n^{(m)}\|\U {L^2(I^n)}=\lim\U {m \to \infty}\liminf\U {k \to \infty}\norm{X\U m-X\U k}\U {\mathbb{D}\U {1,2}}=0.
    \end{gathered}$$
</div>

  As desired. ◻


We now conclude this post by stating two properties of the Malliavin
derivative that are analogous to those verified by the derivative of
ordinary functions. Firstly, an analog to the chain rule for the
ordinary derivative. The proof can be found on page $29$ of Nunno and
Øksendal's book [1](https://link.springer.com/book/10.1007/978-3-540-78572-9) but is rather technical and relies
on Hermite polynomials which were not discussed previously, so we omit
it.


**Definition 2**. We write $\mathbb{D}\U {1,2}^0\subset L^2(\Omega)$ for
the space of square integrable random variables
$X=\sum\U {n=0}^{\infty} I\U n(f\U n)$ such that $f\U n=0$ for all but finitely
many $n$.



**Proposition 3** (Product rule). Given $X\U 1,X\U 2\in \mathbb{D}^0\U {1,2}$
it holds that

<div>
 $$D(X\U 1X\U 2)=X\U 1DX\U 2+X\U 2DX\U 1.$$
</div>




Finally, though we shall not use it, we mention that if
$\Omega=\mathcal{S}^\star({\mathbb R})$ is the dual of the Schwartz space
and we construct a probability measure $\mathbb{P}$ called the [white
noise probability measure](https://en.wikipedia.org/wiki/White_noise_analysis#:~:text=In%20probability%20theory%2C%20a%20branch,based%20on%20the%20Wiener%20process.) then the following version of the chain rule
also holds (see [2](https://link.springer.com/book/10.1007/978-3-540-78572-9) page $89$).


**Proposition 4** (Chain rule). Consider
$\varphi\in C\U 1({\mathbb R}^d)$ with
$\nabla \varphi\in {L^\infty({\mathbb R}^d\to{\mathbb R}^d)}$ and
$X=(X\U 1,\ldots,X\U d)$ such that $X\U i\in \mathbb{D}\U {1,2}$ for each
$i=1,\ldots,d$. Then it holds that $\varphi(X)\in \mathbb{D}\U {1,2}$ with


<div>
 $$D\varphi(X)=\sum\U {i=0}^{d} \frac{\partial \varphi}{\partial x\U i}(X)D(X\U i) .$$
</div>

# Extending past p=2

The Malliavin derivative lets us define a derivative on a subset of
$L^2(\Omega)$. However, it may also be useful to have a concept of
derivative on random variables in $L^p(\Omega)$. We now explain how to
do this via an alternative construction of the Malliavin derivative.
First of all, consider the set of *cylindrical variables*
$$\mathbb{W}:=\left\{\varphi\qty(\int_{I}h(t) dW(t)):\varphi\in C_b^\infty({\mathbb R}^n), h\in L^2(I\to{\mathbb R}^n), n \in \mathbb{N}\right\}$$
That is, $\mathbb{W}$ is the set of all smooth functions with bounded
derivatives of Wiener integrals of deterministic functions. Let us use
the abbreviation $W(h):=\int_{I}h(t) dW(t)$. Then, the results in the
previous section show that the Malliavin differential of a cylindrical
variable is
$$D_t\varphi(W(h))=\nabla\varphi(W(h))\cdot h(t)=\sum_{i=1}^{n} \frac{\partial \varphi}{\partial x_i}(W(h))h_i(t).$$
One can also start directly with the above equation as the defintion of
Malliavin differential. In this case it is not clear that $D_t$ is well
defined (that is, independent of the representation of
$X=\varphi(W(h))$). However it is, see [@hairer2021introduction] page
10. Analogously to how one defines the norm on Sobolev spaces, we now
take any $1\leq p< \infty$ and define a norm on $\mathbb{W}$ by
$$\norm{X}_{\mathbb{D}^{1,p}}:=\norm{X}_{L^p(\Omega)}+\norm{DX}_{L^p(\Omega\to L^2(I))},\quad X\in \mathbb{W}.$$
Then, $D$ is a continuous linear operator on
$(\mathbb{W},\norm{\cdot }_{\mathbb{D}^{1,p}})$ to
$L^2(\Omega\to L^2(I))$. As a result, $D$ may be extended to the closure
of $(\mathbb{W},\norm{\cdot }_{\mathbb{D}^{1,p}})$. We denote this
closure by $\mathbb{D}^{1,p}$ and by abuse of notation also write $D$
for the continuous extension of $D$ to $\mathbb{D}^{1,p}$. Note that by
definition of the norm $\norm{\cdot }_{\mathbb{D}^{1,p}}$, necessarily
$\mathbb{D}^{1,p}$ is a subset of $L^p(\Omega)$. In this way, we have
been able to extend the Malliavin differential to
$\mathbb{D}^{1,p}\subset L^p(\Omega)$. Explicitly, we have that
$$D X:=\lim_{n \to \infty}D X_n \in L^p(\Omega\to L^2(I)).$$ Where
$X_n \in \mathbb{W}$ is a sequence converging to $X$ in
$\mathbb{D}^{1,p}$. Furthermore, we note that by the previous discussion
$D$ coincides with our previous definition of the Malliavin differential
when $p=2$. For the case $p=\infty$ we define
$$D^{1,\infty}:=\bigcap_{p=1} ^\infty \mathbb{D}^{1,p}.$$

We now conclude with an extension of the chain rule which can be used
even when $\varphi$ does not have bounded derivative.

::: proposition
**Proposition 5** (Chain rule for $\mathbb{D}^{1,p}$). *Let
$X\in \mathbb{D}^{1,p}$ and consider $\varphi\in C^1({\mathbb R}^n)$
such that $\norm{\nabla\varphi(x)}\leq C(1+\norm{x}^\alpha)$ for some
$0\leq \alpha\leq p-1$. Then $\varphi(X)\in \mathbb{D}^{1,q}$, where
$q=p/(\alpha+1)$. Furthermore,
$$D\varphi(X)=\nabla \varphi(X) \cdot D X.$$*
:::

::: proof
*Proof.* By the mean value inequality we have that
$$\abs{\varphi(x)}\leq C'(1+\norm{x}^{\alpha+1})=C'(1+\norm{x}^{\frac{p}{q}}).$$
As a result we have that $$\label{in1}
        \varphi(X) \in L^q(\Omega).$$ Furthermore, by Hölder's
inequality applied to $r=(\alpha+1) / \alpha, s=\alpha+1$ we have that
$$\label{in2}
        \nabla \varphi(X) \cdot D X \in L^q(\Omega\to L^2(I)).$$ We now
take a sequence of cylindrical random variables $X_n$ converging to $X$
in $\mathbb{D}^{1,p}$ and an approximation to the identity $\delta_n$.
Let us set $\varphi_n:=\varphi \cdot \delta_n$ $$\begin{gathered}
        D \varphi(X)=\lim_{n \to \infty} D [\varphi_n(X_n)]=\lim_{n \to \infty} (\nabla \varphi_n)(X_n)\cdot DX_n\\=    (\nabla \varphi)(X)\cdot DX \in L^q(\Omega\to L^2(I)).
    \end{gathered}$$ Where the final equality is due to the same method
that gave inclusions [\[in1\]](#in1){reference-type="eqref"
reference="in1"}-[\[in2\]](#in2){reference-type="eqref" reference="in2"}
and the way $X_n,\varphi_n$ converge to $X,\varphi$ respectively. ◻
:::

Essentially the previous proposition says that, if $X$ is differentiable
and the derivative of $\varphi$ doesn't grow to fast (depending on the
integrability of $DX$), then $\varphi(X)$ is also differentiable and we
can apply the chain rule. The integrability of $D\varphi(X)$ depending
on the integrability of $DX$ and the growth of $\nabla \varphi$.

## Example application

For example, in the case $p=2$ we could take $\varphi(x)=x^2$ to deduce
that $$D(X^2)=2XDX,\quad\forall X\in \mathbb{D}^{1,2}.$$ If $X=1_A$ is
an indicator function for some $A\in \mathcal{F}$ we obtain that
$$D(1_A)=D(1_A^2)=21_AD(1_A).$$ From here we deduce that $D1_A=0$. As we
have seen, this occurs if and only if $1_A$ is constant, so necessarily
$1_A=0$ or $1_A=1$. Identifying sets with functions, we have just proved
the following

::: corollary
**Corollary 2**. *Given $A\in \mathcal{F}$ we have that
$1_A\in \mathbb{D}^{1,2}$ if and only if (almost everywhere)
$A=\emptyset$ or $A=\Omega$.*
:::

## Multiple derivatives

Finally we comment on how it is possible to iterate the Malliavin
derivative. Given a cylindrical process $X=\varphi(W(h))\in \mathbb{W}$
we should have that, with Einstein notation
$$D_{t_1}D_{t_2}X=D_{t_1}(\partial_i \varphi(X)h_i(t_2))=D_{t_1}(\partial_i \varphi(X))h_i(t_2)=(\partial_i\partial _j \varphi)(X)h_i(t_1)h_j(t_2).$$
As a result, we define given $X\in \mathbb{W}$
$$D^k_{t_1,\ldots,t_k} X:= \sum_{i_1,\ldots,i_k=1}^{n}  \frac{\partial \varphi}{\partial x_{i_1}\ldots\partial x_{i_k}}(X)h_{i_1}(t_1)\ldots h_{i_k}(t_k) .$$
In the same fashion as before, we can now define the $k$-th differential
norm as
$$\norm{X}_{\mathbb{D}^{k,p}}:=\sum_{i=0}^{k}  \norm{D^j X}_{L^p(\Omega\to L^2(I^k))}.$$
Where we use the convention $D^0 X:=X, L^2(I^0):= {\mathbb R}$. Then we
simply define $\mathbb{D}^{p,k}$ to be the completion of $\mathbb{W}$
with this norm. Finally, we define
$$\mathbb{D}^{\infty,p}:= \bigcap_{k=1}^\infty \mathbb{D}^{k,p};\quad \mathbb{D}^{\infty}:= \mathbb{D}^{\infty,\infty} .$$
