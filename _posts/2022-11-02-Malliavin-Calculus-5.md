---
layout: post
title: Study of densities part 1
subtitle: Part 6 of the series on Malliavin calculus
thumbnail-img: /assets/img/Malliavin.jpg
share-img: /assets/img/Malliavin.jpg
tags: [Malliavin calculus, Densities]
authorpost: L.Llamazares
---
#  Three line summary

-   A Malliavin differentiable random variable $X\in \mathbb{D}^{1,2}$
    is supported in intervals.

-   If $\norm{DX}\U {L^2(I)}$ is almost nowhere zero, then $X$ has a density
    $p$.

-   If $X$ is smooth then $p$ is smooth.

# Why should I care?

The density of a random variable (if it exists) gives us complete
information about it and is the fundamental goal of statistical
inference.

# Notation

Same as other posts, we recall in particular that $\mathbb{D}^\infty$ is
the space of Malliavin smooth random variables. Additionally, to
simplify many expressions, we introduce the notation

<div>
 $$H:=L^2(I).$$
</div>



# Introduction

Our goal is to establish some fundamental properties on the existence of
densities using Malliavin calculus. This is one of the first reasons why
Malliavin calculus was conceived. Firstly, we recall that given a random
variable $X:\Omega\to M$ valued in some metric space $M$, the support of
$X$ is defined to be the set of points $x\in M$ such that


<div>
 $$\mathbb{P}\U X(B\U \epsilon(x))>0,\quad\forall \epsilon>0.$$
</div>

  That is, $X$
has a positive probability of falling in any ball that contains $x$. Our
first result characterizes the support of real-valued Malliavin
differentiable random variables.


**Proposition 1**. Let $X\in \mathbb{D}^{1,2}$, then the support of $X$
is an interval.



Proof. Suppose not, then there must exist $a<x<b$ where $a,b$ are in
the support of $X$ and $x$ isn't. In particular, there exists
$\epsilon >0$ such that

<div>
 $$\label{sup}
            \mathcal{P}\U X([ x-\epsilon ,x+\epsilon ] )=0.$$
</div>

  Where we also
take $\epsilon$ small enough so that $a<x-\epsilon<x+\epsilon<b$. Now
take a smooth and bounded function $\varphi$ with $\varphi(y)=0$ for
$y<x-\epsilon$ and with $\varphi(y)=1$ for $y>x+\epsilon$. By
the previousequation it holds that
(almost everywhere) $\varphi(X)=1\U {X>x+\epsilon}$. Combining
[Proposition 4][https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-3/#:~:text=%28.-,Proposition%204,-(Chain%20rule).%20Consider] and [Corollary 2](https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-3/#:~:text=proved%20the%20following-,Corollary%202,-.%20Given) of a previous post, we
obtain that $1\U {X>x+\epsilon}$ is either $0$ or $1$ almost everywhere.
That is,



<div>
 $$\mathbb{P}(X>x+\epsilon)=0\quad \text{or}\quad \mathbb{P}(X\leq x+\epsilon)<0 .$$
</div>


But this contradicts that both $a,b$ are in the support of $X$. This
concludes the proof. ◻


Ok, now we know the support of Malliavin differentiable functions are
nicely shaped intervals. But what about densities, when can we guarantee
their existence? Consider for example the simplest of all cases,
$X=x\in {\mathbb R}$. That is $X$ always takes the value $x$. Then $X$
is Malliavin differentiable, however, it admits no density (no, the
$\delta$ function does not count as a density). Let's consider a case
that is a bit less trivial, set


<div>
 $$X=I\U 1(f)= \int\U {I}f(t) dW(t),\quad f \in H.$$
</div>

  Then, we have that $X$
is a Gaussian random variable with


<div>
 $$X\sim \mathcal{N}(0,\norm{f}^2\U {H}).$$
</div>

  As a result, we obtain that $X$
will fail to have a density if (and only if)
$\norm{f}\U {H}=\norm{DX}\U {H}=0$. Notice that, in the previously
considered case where $X$ failed to have a density, we also had that
$\norm{DX}\U {H}$ became $0$. The next proposition shows that this is not
a fluke.


**Theorem 1** (Existence of densities). Let $X\in \mathbb{D}^{1,2}$. If
$\norm{DX}\U {H}>0$ almost everywhere, then $X$ has a density.



Proof. By the [Radon Nikodyn theorem](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem#Formal_description:~:text=%5Bedit%5D-,Radon%E2%80%93Nikodym%20theorem,-%5Bedit%5D) all we need to do is show
that $\mathbb{P}\U X$ is absolutely continuous with respect to the
Lebesgue measure $\lambda$. That is, we must show that if,
$\lambda (A)=0$ then also $\mathbb{P}\U X(A)=0$. Let us set $g(y):=1\U A(y)$
and

<div>
 $$\varphi(x):=\int\U {-\infty}^x g(y)dy.$$
</div>

  Then, by construction
$\varphi=0$, so also $\varphi(X)=0$. Suppose now that $g$ were
continuous. Then we would have that, by the fundamental theorem of
calculus $\varphi'(x)=g(x)$. So by the [chain rule](https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-3/#:~:text=%28.-,Proposition%204,-(Chain%20rule).%20Consider)


<div>
 $$0=D \varphi(X)=\varphi'(X)DX=g(X)DX.$$
</div>

  By taking $H$ norms on each
side, we would deduce that, since $DX$ is non-zero, $g(X)=1\U A(X)$ must
be zero. That is, $\mathbb{P}\U X(A)=0$, as desired. Of course, in
general, $g$ will not be differentiable (unless $A$ is actually $0$
everywhere). So to complete the proof, all that remains is to
approximate $g$ by continuous functions $g\U n$ and take limits. See
[1](https://books.google.co.uk/books?hl=zh-CN&lr=&id=l\U 1uDwAAQBAJ&oi=fnd&pg=PR11&dq=nualart+introduction+malliavin&ots=\U JuMhMkTMt&sig=Tx5y00u4kMNs73jLtMEs-kyXAuU&redir\U esc=y#v=onepage&q=nualart\%20introduction\%20malliavin&f=false) page 120 for the details. ◻


The question is, can we give an explicit formula for the density of $X$.
The answer is (under some stricter conditions) yes, and the proof uses a
similar trick as our last one.


**Theorem 2** (Density expression). Let $X\in \mathbb{D}^{1,2}$ such
that $\norm{DX}\U {H}$ is non-zero almost everywhere. Suppose further that
$DX/\norm{DX}^2\U {H}\in \text{dom} (\delta )$. Then $X$ has a density


<div>
 $$p(x):=\mathbb{E}\left[1\U {X\leq x}\delta \left(\frac{DX}{\norm{DX}\U {H}^2}\right) \right] .$$
</div>





Proof. Let us consider $g\in C\U c^\infty({\mathbb R})$ and set as
before

<div>
 $$\varphi(X):=\int\U {-\infty}^x g(x)dx.$$
</div>

  Then by the chain rule and the fundamental theorem of calculus, we have that


<div>
 $$\left\langle D\varphi(X),\frac{DX}{\norm{DX}^2\U {H}}\right\rangle\U {H}=g(X).$$
</div>


By taking expectations on both sides, and using that [the Skorohod
integral is the adjoint of the Malliavin derivative](https://nowheredifferentiable.com/2022-07-02-Malliavin-Calculus-4/#:~:text=result%20is%20fundamental.-,Theorem%201,-.%20The%20Skorokhod%20integral), and Fubini
we obtain,

<div>
 $$\begin{gathered}
  \mathbb{E}[ g(x)] =\mathbb{E}[ \langle D\varphi(X),\frac{DX}{\norm{DX}^2\U {H}}\rangle\U {H}] =\mathbb{E}[ \varphi(X)\delta(\frac{DX}{\norm{DX}\U {H}^2})]                                  \\
 =\mathbb{E}[ (\int\U{{\mathbb R}} 1\U {X\leq x} g(x)dx)\delta(\frac{DX}{\norm{DX}^2\U {H}})] =\int\U{\mathbb{R}} g(x)\mathbb{E}[ 1\U {X\leq x}\delta (\frac{DX}{\norm{DX}\U {H}^2}) ]
   \\=\int\U{\mathbb{R}} g(x)p(x).
        \end{gathered}$$
</div>

  Since $g$ was any smooth function this concludes
the proof (as we can always approximate indicator functions
$1\U A\in L^2({\mathbb R})$ by smooth functions). ◻


To show the differentiability of $p(x)$ we need the following lemma
which will let us transfer- derivatives onto the density $p$.


**Lemma 1** (Integration by parts). Let $X\in \mathbb{D}^{\infty}$ be
such that $\norm{DX}\U {H}>0$ almost everywhere. Then, given any
$Y\in \mathbb{D}^\infty$ and $\varphi \in C\U b^\infty({\mathbb R})$,
there exists $H\U {k}(X,Y)\in \mathbb{D}^\infty$ such that


<div>
 $$\mathbb{E}[ \varphi^{(k)}(X)Y] =\mathbb{E}[ \varphi(X)H\U k(X,Y)] .$$
</div>




Proof. We proceed by induction and consider first the case $k=1$. We
want to integrate parts in a probabilistic integral, as opposed to a
classical deterministic one, against the Lebesgue measure. The idea is
therefore to find a way to introduce the Malliavin differential and then
use the Skorohod integral to move derivates. To do so, we use one of our
previous tricks to write


<div>
 $$\varphi'(X)=\left\langle D\varphi(X),\frac{DX}{\norm{DX}}\U {H}\right\rangle\U {H}.$$
</div>


By now taking expectations, moving $Y$ into the inner product on $H$,
and using that Skorohod integral is the adjoint of the Malliavin
derivative, we get that


<div>
 $$\mathbb{E}[ \varphi'(X)Y] =\mathbb{E}\left[ \varphi(X)\delta \left(\frac{DX}{\norm{DX}}\U {H}Y\right)\right] =:\mathbb{E}[ \varphi(X)H\U 1(X,Y)] .$$
</div>


Where $H\U 1(X,Y)\in \mathbb{D}^\infty$ because the Skorohod integral maps
$\mathbb{D}^\infty$ into $\mathbb{D}^\infty$. This resembles the fact
that the derivative maps the Schwartz space to itself. A proof of this
can be found in Hairer's online notes [2](https://books.google.co.uk/books?hl=zh-CN&lr=&id=l\U 1uDwAAQBAJ&oi=fnd&pg=PR11&dq=nualart+introduction+malliavin&ots=\U JuMhMkTMt&sig=Tx5y00u4kMNs73jLtMEs-kyXAuU&redir\U esc=y#v=onepage&q=nualart\%20introduction\%20malliavin&f=false) page 15.
Now suppose that the lemma holds for $k=n$, then by the same procedure,


<div>
 $$\begin{aligned}
                E[ \varphi^{(n+1)}X]  & =E[ \varphi'(X) H\U n(X,Y)] =\mathbb{E}[ \varphi(X)H\U 1(X,H\U n(X,Y))]  \\&=:\mathbb{E}[ \varphi(X)H\U {n+1}(X,Y)] .
            \end{aligned}$$
</div>

  By the previous comment, since
$H\U n(X,Y)\in \mathbb{D}^\infty$ also
$H\U {n+1}(X,Y)\in \mathbb{D}^\infty$, which concludes the proof. ◻



We now finally show that, if $X$ can be differentiated multiple times,
then so can its density.


**Theorem 3** (Smooth variables have smooth densities). Let
$X\in \mathbb{D}^\infty$ such that $\norm{DX}\U {H}>0$ almost everywhere,
then $X$ has a smooth density with respect to the Lebesgue measure.



Proof. By Theorem [2](https://nowheredifferentiable.com/2022-11-02-Malliavin-Calculus-5/#:~:text=our%20last%20one.-,Theorem%202,-(Density%20expression).%20Let) we know that $X$ has a density $p(x)$. To show
that $p$ is smooth, by [Sobolev embedding](https://mathworld.wolfram.com/SobolevEmbeddingTheorem.html) it is sufficient to show
that $p$ is weakly differentiable with order $n$ for all
$n \in \mathbb{N}$. That is, for all
$\varphi\in C\U b^\infty({\mathbb R})$ there exists a function $p^{(n)}$
such that


<div>
 $$\mathbb{E}\zl \varphi^{(n)}(X)\zr =\int\U\mathbb{R}\varphi^{(n)}(x)p(x) dx=(-1)^n\int\U\mathbb {R}\varphi(x) p^{(n)}(x) dx.$$
</div>


Where the first equality just holds by definition of density, so we only
have to prove the second. The idea will be to integrate by parts, using
the previous lemma to move derivatives off $\varphi$ and onto $1$ (as
strange as that may sound). We know that for any smooth
$\phi\in C\U b^\infty({\mathbb R})$


<div>
 $$\mathbb{E}[ \phi^{(n+1)}(X)] =E[ \phi'(X)H\U n(X,1)] .$$
</div>

  If we apply this to
$\phi(x):=\int\U {-\infty}^x \varphi(y) dy$ where $\varphi$ is any
function in $C\U c^\infty({\mathbb R})$ (and in particular
$\varphi=\phi'$) we obtain that, by Fubini

<div>
$$
\mathbb{E}[ \varphi^{(n)}(X)] =E[ \varphi(X)H\U n(X,1)] = E\left[ \left(\int\U\mathbb{R} 1\U {[ -\infty,X] }(x) \varphi(x)dx\right) H\U n(X,1)\right] \\=\int\U\mathbb{R} \varphi(x)\mathbb{E}\left[ 1\U {[ -\infty,X] }(x)H\U n(X,1)\right]  dx=:(-1)^n \int\U {\mathbb R}\varphi(x) p^{(n)}(x) dx
        $$
</div>

  This proves the theorem. ◻


Finally, we comment that all these theorems carry over to the case where
$X$ is a vector-valued random variable (as opposed to real-valued). In
this case, the condition for the existence of densities becomes that the
matrix of derivatives $(\left\langle DX\U i,DX\U j\right\rangle\U {H})\U {i,j}$
has non-zero determinant almost everywhere. We refer the reader to
[1](https://books.google.co.uk/books?hl=zh-CN&lr=&id=l\U 1uDwAAQBAJ&oi=fnd&pg=PR11&dq=nualart+introduction+malliavin&ots=\U JuMhMkTMt&sig=Tx5y00u4kMNs73jLtMEs-kyXAuU&redir\U esc=y#v=onepage&q=nualart\%20introduction\%20malliavin&f=false)  Chapter $7$ or
[2](https://www.hairer.org/notes/Malliavin.pdf) chapter $4$ for the multidimensional theory.
