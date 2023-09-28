# Mean-reverting schemes for solving the CIR model 

S. Llamazares-Elias, A. Tocino*<br>University of Salamanca, Department of Mathematics, Pl. Merced, 1, 37008 Salamanca, Spain

## 1. A R T I C L E I N F O

## 2. Article history:

Received 30 July 2022

Received in revised form 9 March 2023

## 3. Keywords:

Stochastic differential equations

CIR model

Mean-reverting

Stochastic numerical method

## 4. A B S T R A C T

A family of methods for the numerical solution of the CIR model reproducing the meanreversion property of the exact solution is presented. The convergence of the methods in the strong and weak senses is established. In addition, a method that captures exactly the first and second long term moments of the CIR process is found.

(c) 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 5. Introduction

Stochastic differential equations are an important tool in many fields due to their applications to modeling dynamical phenomena. In Finance, several models have been proposed to describe the changes of interest rates over time, see [1] or [2] and the references therein. Since the interest rate reverts to its long-term mean, mean reversion is a desirable property of interest rate models. In this work we focus on the Cox-Ingersoll-Ross (CIR) model [3], that describes the interest rate as the solution to

$$
d X(t)=\alpha(\theta-X(t)) d t+\sigma \sqrt{X(t)} d W(t), \quad X\U {0}=x\U {0}, \quad t \geq 0,
$$

where $W(t)$ is a standard Wiener process, $\alpha, \theta, \sigma \in \mathbb{R}^{+}$and $x\U {0} \geq 0$. Although, due to its square-root coefficient, the SDE (1) does not fulfill the sufficient conditions used in general theorems [4], a specific result showing the existence and uniqueness of the strong solution can be found in [5], see Theorem 3.2 and its corollary. The solution $X(t)$ of $(1)$, called the CIR process, is mean reverting. Taking expectations in (1) gives

$$
\mathbb{E}[X(t)]=\theta+\left(\mathbb{E}\left[X\U {0}\right]-\theta\right) e^{-\alpha t}
$$

and, since $\alpha>0$,

$$
\lim \U {t \rightarrow \infty} \mathbb{E}[X(t)]=\theta
$$

i.e., the parameter $\theta$ is the long term mean of $X(t)$ and the parameter $\alpha$ represents the speed of convergence. Notice that when $X(t)>\theta$, the drift term of $(1)$ is negative, which drives $X(t)$ back towards $\theta$ and when $X(t)<\theta$, the drift term is positive, which drives $X(t)$ back towards $\theta$. Then, the drift term represents a force pulling the interest rate towards its long term mean [2].

In addition, for the CIR process $X(t)$ it can be seen [2] that

$$
\mathbb{E}\left[X(t)^{2}\right]=\theta^{2}+\frac{\sigma^{2} \theta}{2 \alpha}+e^{-2 \alpha t}\left(\mathbb{E}\left[X\U {0}^{2}\right]+\left(2 \theta+\frac{\sigma^{2}}{\alpha}\right)\left(\frac{\theta}{2}-\mathbb{E}\left[X\U {0}\right]\right)\right)+e^{-\alpha t}\left(2 \theta+\frac{\sigma^{2}}{\alpha}\right)\left(\mathbb{E}\left[X\U {0}\right]-\theta\right) .
$$

[^0] Consequently,

$$
\lim \U {t \rightarrow \infty} \mathbb{E}\left[X(t)^{2}\right]=\theta^{2}+\frac{\sigma^{2} \theta}{2 \alpha}
$$

and the long-term variance of the CIR process is

$$
\lim \U {t \rightarrow \infty} \operatorname{Var}(X(t))=\lim \U {t \rightarrow \infty} \mathbb{E}\left[X(t)^{2}\right]-\lim \U {t \rightarrow \infty} \mathbb{E}[X(t)]^{2}=\frac{\sigma^{2} \theta}{2 \alpha} .
$$

The transition density and the distribution of the CIR process are known, but a closed form of the solution is not available except when the parameters of Eq. (1) satisfy the relation $\sigma^{2}=4 \alpha \theta$, see [6]. Although the exact transition density can be simulated, see e.g. the method proposed by Glasserman in [7], its computational cost is remarkably larger than using numerical schemes when one needs to simulate the process along a time grid, see [8]. A number of general methods to solve numerically stochastic differential equations have been proposed, see [9] and the references therein. Nevertheless, most of general methods, e.g. Euler-Maruyama or Taylor schemes, are not suitable in this case due to the fact that they use evaluations of the diffusion coefficient $\sigma \sqrt{x}$ or of its derivatives which are not well-defined when negative values of the scheme appear. To overcome this problem, numerical methods specially designed to solve the CIR equation have been proposed in the literature [8,10-12].

Convergence order (weak or strong) is a main feature to assess and compare stochastic numerical methods. But in some cases, e.g. when comparing numerical methods for solving an SDE with the same convergence order, the preservation of a qualitative feature of the exact solution is a desirable property. For example, and constrained to the CIR equation (1), many proposed schemes preserve the non-negativity of the exact solution, see e.g. [13-15]; other schemes are designed to preserve the monotonicity of the CIR process, e.g. the schemes (3) and (4) in [8]; and a survey of schemes are compared numerically in [16] for the quality of their first four moments estimates of the CIR process. With this in mind, our goal here is to propose schemes that applied to the CIR problem give numerical solutions with the mean reverting property, i.e. numerical approximations $\left\{X\U {n}\right\}$ of $X(t)$ such that

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}\right]=\lim \U {t \rightarrow \infty} \mathbb{E}[X(t)]=\theta .
$$

In addition, for schemes that preserve the first long term moment, one can analyze if they also preserve the second one:

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}^{2}\right]=\lim \U {t \rightarrow \infty} \mathbb{E}\left[X(t)^{2}\right]=\theta^{2}+\frac{\sigma^{2} \theta}{2 \alpha} .
$$

To the best of our knowledge, these properties of numerical integrators have only been studied by Higham and Mao, see [17], for the modified Euler method (HM)

$$
X\U {n+1}=X\U {n}+\alpha\left(\theta-X\U {n}\right) \Delta+\sigma \sqrt{\left|X\U {n}\right|} \Delta W\U {n}
$$

here, and from now on, $\Delta>0$ denotes the step size of the scheme and $\Delta W\U {n}=W\left(t\U {n+1}\right)-W\left(t\U {n}\right)$, with $t\U {n}=n \Delta$. In [17] the authors determined that identity (4) is verified for the scheme (6) if $\Delta<2 / \alpha$. In addition, given the same restriction on $\Delta$, they show a band where the $\lim \U {i n f} \operatorname{lod}\U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}^{2}\right]$ and lim $\sup \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}^{2}\right]$ can be found. To improve the modified Euler scheme, which is a low-order method in the weak and strong senses of convergence, different numerical schemes have been proposed with better convergence rates for the CIR problem. This is particularly the case of the scheme $E(0)$

$$
X\U {n+1}=\left(\left(1-\frac{\alpha \Delta}{2}\right) \sqrt{X\U {n}}+\frac{\sigma \Delta W\U {n}}{2-\alpha \Delta}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta,
$$

proposed by Alfonsi [8]. This scheme converges in the strong sense with a logarithmic rate and in the weak sense with order 1 when

$$
\sigma^{2} \leq 4 \alpha \theta
$$

But, unlike the Euler method, $\mathrm{E}(0)$ does not preserve the long term mean: a short calculation gives for this scheme

$$
\mathbb{E}\left[X\U {n}\right]=\left(1-\frac{\alpha \Delta}{2}\right)^{2 n}\left(\mathbb{E}\left[X\U {0}\right]-\frac{4 \theta}{4-\alpha \Delta}-\frac{\Delta \sigma^{2}}{(\alpha \Delta-2)^{2}}\right)+\frac{4 \theta}{4-\alpha \Delta}+\frac{\Delta \sigma^{2}}{(\alpha \Delta-2)^{2}},
$$

which, when $\Delta<2 / \alpha$, converges to

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}\right]=\theta+\frac{\alpha \Delta \theta}{4-\alpha \Delta}+\frac{\Delta \sigma^{2}}{(\alpha \Delta-2)^{2}}>\theta,
$$

i.e., the scheme $\mathrm{E}(0)$ overestimates the long term mean (in a large amount when $\alpha \Delta \sim 2$ ). Our goal in this work is to propose schemes with the same convergence properties as $E(0)$ and which preserve the long-term mean of the CIR process. In Section 2 we propose a family of methods that contain $E(0)$ and whose members share its convergence properties. In Section 3 we obtain a class of methods, contained in the above family, that verify property (4), i.e., that preserve the mean reversion property. In Section 4 we find a scheme of this subfamily that, in addition to preserving the long-term mean, preserves the long-term variance. Finally, in Section 5 we carry out numerical experiments that confirm the theoretical results of the above sections.

## 6. A new family of methods

Taking the scheme (7) as a starting point, in this section we propose new methods with similar weak and strong convergence properties to solve numerically the CIR equation (1). From now on, we denote by $\mathcal{F}\U {t}$ the $\sigma$-algebra generated by the standard Wiener process $\{W(t)\}\U {t \geq 0}$ and, following [8] we use the extension of big $\mathcal{O}$ notation to random variables. For a family of random variables $X=\left\{X\U {n}^{\Delta}\right\}$ we will write $X=\mathcal{O}\left(\Delta^{s}\right)$ when for any $p \in \mathbb{N}$ there exist $\delta, M>0$ such that

$$
\sup \U {n} \mathbb{E}\left[\left|X\U {n}^{\Delta} / \Delta^{s}\right|^{p}\right]<M
$$

when $0<\Delta<\delta$. In the following, the superscript $\Delta$ shall be omitted when its value is clear from context.

To solve numerically Eq. (1) with parameters verifying the restriction (8) we propose the schemes defined by $X\U {0}=x\U {0}$ and

$$
X\U {n+1}:=\left(\left(1-\frac{\alpha}{2} \Delta+K\U {\Delta} \Delta^{2}\right) \sqrt{X\U {n}}+\frac{\sigma}{2} \Delta W\U {n}+S\U {\Delta} \Delta \Delta W\U {n}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
$$

for $n=0,1, \ldots$, where $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right), S\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ are deterministic.

Notice that $X\U {n} \geq 0, n \in \mathbb{N}$. Notice also that the scheme (7) is of the form (11) with $K\U {\Delta}=0, S\U {\Delta}=\alpha \sigma /(4-2 \alpha \Delta)$. We shall show that the proposed schemes (11) have uniformly bounded moments and converge to the exact solution of (1) in the strong and weak senses with the same order as $\mathrm{E}(0)$. The proofs rely on some results proven in [8].

Proposition 2.1. The schemes (11) have uniformly bounded moments.

Proof. It is clear that $\left\{X\U {n}\right\}$ is non-negative and adapted to $\left\{\mathcal{F}\U {t\U {n}}\right\}$, where $t\U {n}=n \Delta$. For all $n \in \mathbb{N}$ we have

$$
X\U {n+1}<\left(1+\tau \Delta^{2}\right) X\U {n}+\rho \sqrt{X\U {n}} \Delta W\U {n}+\mathcal{O}(\Delta)
$$

where

$$
\tau:=\frac{\alpha^{2}}{4}+\left|K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)\right|
$$

is $\mathcal{O}\left(\Delta^{0}\right)$ and positive and

$$
\rho:=\left(1-\frac{\alpha \Delta}{2}+K\U {\Delta} \Delta^{2}\right)\left(\sigma+2 \Delta S\U {\Delta}\right)
$$

is also $\mathcal{O}\left(\Delta^{0}\right)$ and $\mathcal{F}\U {t\U {n}}$-adapted. Hence, we conclude by using Lemma 2.6 in [8].

Proposition 2.2. Scheme (11) converges to the exact solution of the SDE (1) in the strong sense with logarithmic convergence rate, i.e. there exists a constant $M$ independent of $\Delta$ such that

$$
\sup \U {n} \mathbb{E}\left[\left|X\U {n}^{\Delta}-X\left(t\U {n}\right)\right|\right] \leq \frac{M}{|\log (\Delta)|} .
$$

Proof. The scheme (11) can be written as

$$
X\U {n+1}=X\U {n}+\alpha\left(\theta-X\U {n}\right) \Delta+\sigma \sqrt{X\U {n}} \Delta W\U {n}+m\U {n+1}-m\U {n}+\mathcal{O}\left(\Delta^{2}\right)
$$

where $\left\{m\U {n}\right\}$ is the discrete $\mathcal{F}\U {t\U {n}}$-adapted process, $t\U {n}=n \Delta$, defined by $m\U {0}:=0$ and

$$
m\U {n+1}:=m\U {n}+\frac{\sigma^{2}}{4}\left(\Delta W\U {n}^{2}-\Delta\right)+\left(2 S\U {\Delta}-\frac{\alpha \sigma}{2}\right) \sqrt{X\U {n}} \Delta W\U {n} \Delta ; \quad n \in \mathbb{N} .
$$

Since $m\U {n+1}-m\U {n}=\mathcal{O}(\Delta)$ and

$$
\mathbb{E}\left[m\U {n+1}-m\U {n} \mid \mathcal{F}\U {t\U {n}}\right]=0 ; \quad n \in \mathbb{N},
$$

we conclude from Proposition 3.1 in [8].

Remark 2.3. Notice that pathwise convergence with logarithmic rate is a weak result compared to the error rates known for other methods, see [12,18]. However, numerical experiments presented in Section 5 , show that our methods can attain experimental strong order similar to 1 , in line with the methods studied in $[12,18]$.

Proposition 2.4. The scheme (11) converges to the exact solution of the SDE (1) with weak order equal to 1, i.e.

$$
\mathbb{E}\left[f\left(X\U {n}^{\Delta}\right)\right]-\mathbb{E}\left[f\left(X\left(t\U {n}\right)\right)\right]=\mathcal{O}(\Delta)
$$

for any function $f: \mathbb{R}^{+} \rightarrow \mathbb{R}$ whose fourth derivative exists, is continuous and has polynomial growth. Proof. From (11)

$$
\begin{aligned}
\left(X\U {n+1}-X\U {n}\right)^{2}= & \sigma^{2} X\U {n} \Delta W\U {n}^{2}+\frac{1}{2} \sigma^{3} \sqrt{X\U {n}} \Delta W\U {n}^{3} \\
& +\left(2 \alpha \theta \sigma \sqrt{X\U {n}}-2 \alpha \sigma X\U {n}^{3 / 2}-\frac{1}{2} \sigma^{3} \sqrt{X\U {n}}\right) \Delta W\U {n} \Delta+\mathcal{O}\left(\Delta^{2}\right) .
\end{aligned}
$$

Then if $t\U {n}=n \Delta$,

$$
\mathbb{E}\left[\left(X\U {n+1}-X\U {n}\right)^{2} \mid \mathcal{F}\U {t\U {n}}\right]=\sigma^{2} X\U {n} \Delta+\mathcal{O}\left(\Delta^{2}\right) .
$$

Using (13), (14) and Proposition 4.2 in [8], we conclude.

## 7. Mean-reverting schemes

We analyze now under which conditions the schemes (11) are able to reproduce the mean-reverting property of the exact solution. Once obtained such conditions, particular examples fulfilling them are proposed.

Since $\mathbb{E}\left[\Delta W\U {n}\right]=0$ and $\mathbb{E}\left[\Delta W\U {n}{ }^{2}\right]=\Delta$, taking expectations in (11) we have

$$
\mathbb{E}\left[X\U {n+1}\right]=a(\Delta) \mathbb{E}\left[X\U {n}\right]+b(\Delta)
$$

where

$$
a(\Delta):=\left(1-\frac{\alpha}{2} \Delta+K\U {\Delta} \Delta^{2}\right)^{2}
$$

and

$$
b(\Delta):=\Delta\left(\alpha \theta+\Delta S\U {\Delta} \sigma+\Delta^{2} S\U {\Delta}^{2}\right)
$$

Therefore, if $\Delta>0$ is such that $a(\Delta) \neq 1$ then

$$
\mathbb{E}\left[X\U {n}\right]=b(\Delta) \sum\U {i=0}^{n-1} a(\Delta)^{i}+a(\Delta)^{n} \mathbb{E}\left[X\U {0}\right]=b(\Delta) \frac{1-a(\Delta)^{n}}{1-a(\Delta)}+a(\Delta)^{n} \mathbb{E}\left[X\U {0}\right] .
$$

Since $a(\Delta) \geq 0$, when $a(\Delta)<1$

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}\right]=\frac{b(\Delta)}{1-a(\Delta)},
$$

and, consequently, $\left\{X\U {n}\right\}$ has long term mean $\theta$ if and only if

$$
b(\Delta)=\theta(1-a(\Delta))
$$

Notice that the condition $a(\Delta)<1$ can be written as

$$
\frac{\alpha}{2 \Delta}-\frac{2}{\Delta^{2}}<K\U {\Delta}<\frac{\alpha}{2 \Delta} \text {. }
$$

Then if (19) holds, Eq. (18) becomes the second order equation in terms of $S\U {\Delta}$

$$
\Delta S\U {\Delta}^{2}+\sigma S\U {\Delta}+\frac{1}{4} \theta\left(\alpha^{2}+4 K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)\right)=0
$$

with solutions

$$
S\U {\Delta, \pm}:=\frac{-\sigma \pm \sqrt{\sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)}}{2 \Delta}
$$

when

$$
\sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right) \geq 0 .
$$

Since $\sigma>0$

$$
S\U {\Delta,-}=-\frac{\sigma}{\Delta}+\frac{\theta\left(\alpha^{2}+8 K\U {\Delta}\right)}{4 \sigma}+O(\Delta) \neq O\left(\Delta^{0}\right),
$$

whereas

$$
S\U {\Delta,+}=\frac{\theta\left(\alpha^{2}+8 K\U {\Delta}\right)}{4 \sigma}+O(\Delta)=O\left(\Delta^{0}\right) .
$$

For this reason we choose

$$
S\U {\Delta}:=S\U {\Delta,+}=\frac{-\sigma+\sqrt{\sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)}}{2 \Delta} .
$$

To sum up:

Theorem 3.1. Given $\Delta>0$ and $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ such that (19) and (22) hold, the scheme

$$
\begin{aligned}
X\U {n+1}= & \left(\left(1-\frac{\alpha \Delta}{2}+\Delta^{2} K\U {\Delta}\right) \sqrt{X\U {n}}+\frac{1}{2} \sqrt{\sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)} \Delta W\U {n}\right)^{2} \\
& +\Delta\left(\alpha \theta-\frac{\sigma^{2}}{4}\right)
\end{aligned}
$$

is of the form (11) and gives numerical solutions of Eq. (1) that inherit the mean-reverting property of the exact solution, i.e. $\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}\right]=\theta$.

The scheme (24) will be denoted $\mathrm{M}\left(K\U {\Delta}\right)$.

Corollary 3.2. Consider the scheme (24) for approximating the mean-reverting solution of Eq. (1) when $\sigma^{2} \leq 4 \alpha \theta$.

1. If $\sigma^{2}=4 \alpha \theta$ then for every $\Delta>0$ and $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ such that (19) holds, the scheme preserves the long-term mean $\theta$.
2. If $\sigma^{2}<4 \alpha \theta$ then for every $0<\Delta \leq \frac{4 \theta}{4 \alpha \theta-\sigma^{2}}$ and $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ such that

$$
\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}-\frac{\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}}}{\Delta^{2}} \leq K\U {\Delta} \leq \frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}+\frac{\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}}}{\Delta^{2}},
$$

the scheme preserves the long-term mean $\theta$.

Proof. According to the above theorem the scheme (24) preserves the long-term mean if conditions (19) and (22) are fulfilled.

When $\sigma^{2}=4 \alpha \theta$, condition (22) follows from condition (19), since

$$
\sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right)=-4 \Delta^{3} \theta\left(K\U {\Delta}-\frac{\alpha}{2 \Delta}\right)\left(K\U {\Delta}-\frac{\alpha}{2 \Delta}+\frac{2}{\Delta^{2}}\right) .
$$

Suppose now that $\sigma^{2}<4 \alpha \theta$ and $0<\Delta \leq 4 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$. It is clear that condition (25) implies (19). And from

$$
\begin{aligned}
& \sigma^{2}-\alpha^{2} \Delta \theta-4 \Delta \theta K\U {\Delta}\left(2-\alpha \Delta+\Delta^{2} K\U {\Delta}\right) \\
& =-4 \Delta^{3} \theta\left(K\U {\Delta}-\frac{\alpha}{2 \Delta}+\frac{1}{\Delta^{2}}-\frac{\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}}}{\Delta^{2}}\right)\left(K\U {\Delta}-\frac{\alpha}{2 \Delta}+\frac{1}{\Delta^{2}}+\frac{\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}}}{\Delta^{2}}\right)
\end{aligned}
$$

we conclude that (25) implies (22).

Remark 3.3. Conditions (19) and (25) are of the form

$$
L(\Delta)<K\U {\Delta}<U(\Delta)
$$

where

$$
\lim \U {\Delta \rightarrow 0} L(\Delta)=-\infty ; \quad \lim \U {\Delta \rightarrow 0} U(\Delta)=+\infty .
$$

Since $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$, for any $K\U {\Delta}$ there exists $\Delta\U {0}>0$ such that scheme $\mathrm{M}\left(K\U {\Delta}\right)$ applied with step size $\Delta \in\left(0, \Delta\U {0}\right)$ preserves the mean reversion property.

Now we present three particularly simple schemes of the form (11) together with sufficient conditions for their ability to reproduce the mean-reverting property.

Proposition 3.4. The numerical scheme $M\U {0}:=M(0)$

$$
X\U {n+1}=\left(\left(1-\frac{\alpha \Delta}{2}\right) \sqrt{X\U {n}}+\frac{1}{2} \sqrt{\sigma^{2}-\alpha^{2} \Delta \theta} \Delta W\U {n}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
$$

applied with step size $\Delta<\frac{\sigma^{2}}{\alpha^{2} \theta}$ to solve Eq. (1) preserves the mean-reversion property of the exact solution. Proof. Since $\sigma^{2} \leq 4 \alpha \theta$, the proposed step-size verifies $\Delta<\frac{\sigma^{2}}{\alpha^{2} \theta} \leq 4 / \alpha$. Then the result is a direct application of Theorem 3.1, since when $K\U {\Delta}=0$ condition (19) reduces to $\Delta<\frac{4}{\alpha}$ and condition (22) is $\Delta \leq \frac{\sigma^{2}}{\alpha^{2} \theta}$.

Proposition 3.5. The numerical scheme $M\U {1}$ given by the expression

$$
X\U {n+1}=\left(\sqrt{1-\alpha \Delta} \sqrt{X\U {n}}+\frac{\sigma}{2} \Delta W\U {n}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
$$

applied with step size $0<\Delta<\frac{1}{\alpha}$ to solve Eq. (1) preserves the mean-reversion property of the exact solution.

Proof. The scheme $(27)$ is $\mathrm{M}\left(K\U {\Delta}\right)$ with

$$
K\U {\Delta}=\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}+\frac{\sqrt{1-\alpha \Delta}}{\Delta^{2}} .
$$

Suppose that $0<\Delta<\frac{1}{\alpha}$. From (28), condition (19) reduces to

$$
-\frac{2}{\Delta^{2}}<-\frac{1}{\Delta^{2}}+\frac{\sqrt{1-\alpha \Delta}}{\Delta^{2}}<0
$$

that obviously holds. If $\sigma^{2}<4 \alpha \theta$ then $\Delta<\frac{1}{\alpha}<\frac{4 \theta}{4 \alpha \theta-\sigma^{2}}$ and condition (22) reduces to

$$
-\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}} \leq-\sqrt{1-\alpha \Delta} \leq \sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}},
$$

that obviously holds. Then Corollary 3.2 leads to the conclusion.

Proposition 3.6. The numerical scheme $M\U {2}$ given by the expression

$$
X\U {n+1}=\left(1-\frac{4 \alpha \Delta \theta}{\Delta \sigma^{2}+4 \theta}\right)\left(\sqrt{X\U {n}}+\frac{\sigma}{2} \Delta W\U {n}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
$$

preserves the mean-reversion property of the exact solution of Eq. (1) for all step sizes $\Delta>0$ when $\sigma^{2}=4 \alpha \theta$, and for step sizes $0<\Delta \leq 4 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$ when $\sigma^{2}<4 \alpha \theta$.

Proof. The scheme (29) is $\mathrm{M}\left(K\U {\Delta}\right)$ with

$$
K\U {\Delta}=\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}+\frac{\sqrt{1-\frac{4 \alpha \Delta \theta}{4 \theta+\Delta \sigma^{2}}}}{\Delta^{2}} .
$$

When $\sigma^{2}=4 \alpha \theta, K\U {\Delta}=\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}+\frac{1}{\Delta^{2} \sqrt{\alpha \Delta+1}}$ and condition (19) obviously holds. On the other hand, when $\sigma^{2}<4 \alpha \theta$ condition (25) reduces to

$$
-\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}} \leq \sqrt{1-\frac{4 \alpha \Delta \theta}{4 \theta+\Delta \sigma^{2}}} \leq \sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}}
$$

that obviously holds when $\Delta \leq 4 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$. Then Corollary 3.2 leads to the conclusion.

By means of the identity (17) for any scheme $X\U {n}$ of the form (11) one can calculate $\mathbb{E}\left[X\U {n}\right]$ using the corresponding $a(\Delta)$ and $b(\Delta)$. In the left plot of Fig. 1 we show the evolution of the means $\mathbb{E}\left[X\U {n}^{\mathrm{M}\U {0}}\right], \mathbb{E}\left[X\U {n}^{\mathrm{M}\U {1}}\right], \mathbb{E}\left[X\U {n}^{\mathrm{M}\U {2}}\right], n=t / \Delta$, of the schemes $\mathrm{M}\U {0}, \mathrm{M}\U {1}, \mathrm{M}\U {2}$ when solving Eq. (1) with parameters $\alpha=0.43, \theta=0.06, \sigma=0.15$ in the interval $[0,15]$ with an equidistant partition of step size $\Delta=1 / 8$ and starting point $X\U {0}=0.9 \theta$. Additionally, on the right plot of Fig. 1 , the error of each method $M$

$$
\varepsilon\U {M}\left(t\U {n}\right):=\left|\mathbb{E}\left[X\U {n}\right]-\mathbb{E}\left[X\left(t\U {n}\right)\right]\right|
$$

is shown in logarithmic scale. In both cases, the values on the grid points are extended to the whole interval by linear interpolation. As the parameters verify the conditions of Propositions 3.4-3.6 the means of all three schemes converge to the long-term mean of the exact solution. This is confirmed in the left image of Fig. 1. In the right plot it can be seen how the weak errors start off at 0 , rise sharply and then decrease exponentially along the remainder of the time interval. All three numerical approximations present similar weak errors.

## 8. Long term second moment

In the above section we developed a family of schemes conserving the long-term mean of the CIR process. In this section we explore if some of these methods also retain the long-term second moment. Recall that the proposed family
![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-07.jpg?height=456&width=1542&top\U left\U y=170&top\U left\U x=170)

Fig. 1. Evolution of means and weak errors of schemes (26), (27) and (29).

(24) depends on $K\U {\Delta}$, with $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ fulfilling (19) and (22). From (5) we must study if under these conditions the equation

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}^{2}\right]=\theta^{2}+\frac{\sigma^{2} \theta}{2 \alpha}
$$

can be solved in terms of $K\U {\Delta}$. Let us suppose that $\Delta$ and $K\U {\Delta}$ are such that (19) and (22) hold. Using that $\mathbb{E}\left[\Delta W\U {n}{ }^{4}\right]=3 \Delta^{2}$ we have that

$$
\mathbb{E}\left[X\U {n+1}^{2}\right]=c(\Delta) \mathbb{E}\left[X\U {n}^{2}\right]+d(\Delta) \mathbb{E}\left[X\U {n}\right]+e(\Delta)
$$

where

$$
\begin{aligned}
& c(\Delta):=a(\Delta)^{2}, \\
& d(\Delta):=6 a(\Delta) \Delta\left(\Delta S\U {\Delta}+\frac{\sigma}{2}\right)^{2}+2 a(\Delta) \Delta\left(\alpha \theta-\frac{\sigma^{2}}{4}\right), \\
& e(\Delta):=2 \Delta^{2}\left(\Delta S\U {\Delta}+\frac{\sigma}{2}\right)^{4}+b(\Delta)^{2},
\end{aligned}
$$

with $a(\Delta)$ and $b(\Delta)$ defined in (15) and (16) respectively. So using (17) and that $a(\Delta) \neq 1$,

$$
\begin{aligned}
\mathbb{E}\left[X\U {n+1}^{2}\right]= & c(\Delta) \mathbb{E}\left[X\U {n}^{2}\right]+d(\Delta)\left(a(\Delta)^{n}\left(\mathbb{E}\left[X\U {0}\right]-\frac{b(\Delta)}{1-a(\Delta)}\right)+\frac{b(\Delta)}{1-a(\Delta)}\right)+e(\Delta) \\
= & c(\Delta)^{n+1} \mathbb{E}\left[X\U {0}^{2}\right]+d(\Delta) a(\Delta)^{n} \frac{1-a(\Delta)^{n+1}}{1-a(\Delta)}\left(\mathbb{E}\left[X\U {0}\right]-\frac{b(\Delta)}{1-a(\Delta)}\right) \\
& +\frac{1-c(\Delta)^{n+1}}{1-c(\Delta)}\left(\frac{b(\Delta) d(\Delta)}{1-a(\Delta)}+e(\Delta)\right) .
\end{aligned}
$$

Since $0<a(\Delta)<1$ we have $0<c(\Delta)<1$ and

$$
\lim \U {n \rightarrow \infty} \mathbb{E}\left[X\U {n}^{2}\right]=\frac{\frac{b(\Delta) d(\Delta)}{1-a(\Delta)}+e(\Delta)}{1-c(\Delta)}=\frac{\theta d(\Delta)+e(\Delta)}{1-c(\Delta)} .
$$

where we have used (18). Inserting this value in (30), the approximation $\left\{X\U {n}\right\}$ will have the desired long-term second moment if and only if

$$
\theta d(\Delta)+e(\Delta)+(c(\Delta)-1)\left(\theta^{2}+\frac{\sigma^{2} \theta}{2 \alpha}\right)=0
$$

which can be written as

$$
\begin{aligned}
\left(4 \alpha \theta-\sigma^{2}\right) & \left(-2 \Delta^{8} \theta K\U {\Delta}^{4}+4 \Delta^{6} \theta(\alpha \Delta-2) K\U {\Delta}^{3}-3 \Delta^{4} \theta(\alpha \Delta-2)^{2} K\U {\Delta}^{2}\right. \\
& \left.+\Delta^{2} \theta(\alpha \Delta-2)^{3} K\U {\Delta}-\frac{\alpha}{8} \Delta^{2}\left(\alpha \theta(\alpha \Delta(\alpha \Delta-8)+8)+4 \sigma^{2}\right)\right)=0 .
\end{aligned}
$$

This equality is trivially satisfied for all $K\U {\Delta}$ when $\sigma^{2}=4 \alpha \theta$. Then, using Corollary 3.2, if $\sigma^{2}=4 \alpha \theta$ for every $\Delta>0$ and $K\U {\Delta}=\mathcal{O}\left(\Delta^{0}\right)$ such that (19) holds, the scheme preserves the long-term first and second moments. On the other hand, when $\sigma^{2}<4 \alpha \theta$ Eq. (33) reduces to a quartic equation which only has real solutions

$$
K\U {\Delta, \pm}:=\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}} \pm \frac{\sqrt[4]{\theta\left(4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2}\right)}}{\sqrt{2} \Delta^{2} \sqrt{\theta}},
$$

when $4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2} \geq 0$. Using the second-order Taylor expansion at $\Delta=0$ of $\left(\theta\left(4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2}\right)\right)^{1 / 4}$ leads to

$$
\frac{\sqrt[4]{\theta\left(4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2}\right)}}{\sqrt{2} \Delta^{2} \sqrt{\theta}}=\frac{1}{\Delta^{2}}-\frac{\alpha}{2 \Delta}-\frac{\alpha\left(2 \alpha \theta+\sigma^{2}\right)}{16 \theta}+\mathcal{O}(\Delta) ;
$$

then

$$
K\U {\Delta,-}=-\frac{2}{\Delta^{2}}+\frac{\alpha}{\Delta}+\frac{\alpha\left(2 \alpha \theta+\sigma^{2}\right)}{16 \theta}+\mathcal{O}(\Delta) ; \quad K\U {\Delta,+}=-\frac{\alpha\left(2 \alpha \theta+\sigma^{2}\right)}{16 \theta}+\mathcal{O}(\Delta) ;
$$

from here we conclude that when $\sigma^{2}<4 \alpha \theta$ and

$$
4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2} \geq 0
$$

Eq. (33) has a unique $\mathcal{O}\left(\Delta^{0}\right)$ solution,

$$
K\U {\Delta,+}=\frac{\alpha}{2 \Delta}-\frac{1}{\Delta^{2}}+\frac{\sqrt[4]{\theta\left(4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2}\right)}}{\sqrt{2} \Delta^{2} \sqrt{\theta}} .
$$

We prove now that the numerical method of the class (24) with $K\U {\Delta}=K\U {\Delta,+}$ preserves the two first moments if it is applied with a sufficiently small step-size.

Proposition 4.1. The numerical scheme MS

$$
\begin{aligned}
X\U {n+1}= & \frac{1}{4}\left(\sqrt[4]{4\left(4(1-\alpha \Delta)^{2}-\frac{\alpha \Delta^{2} \sigma^{2}}{\theta}\right) X\U {n}}+\sqrt{\frac{4 \theta(1-\alpha \Delta)+\Delta \sigma^{2}-2 \sqrt{\theta\left(4 \theta(1-\alpha \Delta)^{2}-\alpha \Delta^{2} \sigma^{2}\right)}}{\Delta} \Delta W\U {n}}\right)^{2} \\
& +\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
\end{aligned}
$$

applied with step size $\Delta \leq \frac{1}{2 \alpha}$ for solving (1) with $\sigma^{2} \leq 4 \alpha \theta$ preserves the mean-reversion property and captures the second moment limit of the exact solution.

Proof. Suppose that $\Delta \leq 1 /(2 \alpha)$. We check firstly that inequality (34),

$$
p(\Delta):=\alpha \Delta^{2}\left(4 \alpha \theta-\sigma^{2}\right)-8 \alpha \Delta \theta+4 \theta \geq 0
$$

holds. When $\sigma^{2}=4 \alpha \theta$ then $p(\Delta)=4 \theta(1-2 \alpha \Delta) \geq 0$. When $\sigma^{2}<4 \alpha \theta$,

$$
p(\Delta)=\alpha\left(4 \alpha \theta-\sigma^{2}\right)\left(\Delta-\frac{2(2 \alpha \theta-\sqrt{\alpha \theta} \sigma)}{4 \alpha^{2} \theta-\alpha \sigma^{2}}\right)\left(\Delta-\frac{2(2 \alpha \theta+\sqrt{\alpha \theta} \sigma)}{4 \alpha^{2} \theta-\alpha \sigma^{2}}\right)
$$

and then $p(\Delta) \geq 0$ for

$$
\Delta \leq \Delta^{-}=\frac{2(2 \alpha \theta-\sqrt{\alpha \theta} \sigma)}{4 \alpha^{2} \theta-\alpha \sigma^{2}} .
$$

Since

$$
\Delta^{-}-\frac{1}{2 \alpha}=\frac{4 \alpha \theta+\sigma^{2}-4 \sigma \sqrt{\alpha \theta}}{2 \alpha\left(4 \alpha \theta-\sigma^{2}\right)}=\frac{(2 \sqrt{\alpha \theta}-\sigma)^{2}}{2 \alpha\left(4 \alpha \theta-\sigma^{2}\right)} \geq 0
$$

we have that $1 /(2 \alpha) \leq \Delta^{-}$and from here $p(\Delta) \geq 0$ if $\Delta \leq 1 /(2 \alpha)$. Then we conclude that $K\U {\Delta,+}$ fulfills (34) if $\Delta \leq 1 /(2 \alpha)$.

To prove the statement we show that $K\U {\Delta,+}$ fulfills the conditions of Corollary 3.2. When $\sigma^{2}=4 \alpha \theta$ condition (19) for $K\U {\Delta,+}$ reads

$$
-\frac{1}{\Delta^{2}}<\frac{\sqrt[4]{1-2 \alpha \Delta}}{\Delta^{2}}<\frac{1}{\Delta^{2}}
$$

![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-09.jpg?height=424&width=1522&top\U left\U y=178&top\U left\U x=176)

Fig. 2. Evolution of the second moment of scheme (36) and its error $\varepsilon\U {M S}^{2}$.

which clearly holds. When $\sigma^{2}<4 \alpha \theta$ condition (25) reduces to

$$
-\sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}} \leq \frac{\sqrt[4]{\theta\left(4 \theta(\alpha \Delta-1)^{2}-\alpha \Delta^{2} \sigma^{2}\right)}}{\sqrt{2 \theta}} \leq \sqrt{1-\alpha \Delta+\frac{\Delta \sigma^{2}}{4 \theta}},
$$

which is equivalent to $0 \leq \Delta \leq 8 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$. Since

$$
\frac{1}{2 \alpha}<\frac{4 \theta}{4 \alpha \theta-\sigma^{2}}<\frac{8 \theta}{4 \alpha \theta-\sigma^{2}},
$$

(25) is fulfilled for $\Delta \leq 4 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$ and, using Corollary 3.2, we conclude that when $\sigma^{2}<4 \alpha \theta$ the numerical scheme (36) applied with step size $\Delta<4 \theta /\left(4 \alpha \theta-\sigma^{2}\right)$, in particular for any $\Delta \leq 1 /(2 \alpha)$, preserves the long-term first and second moments.

Remark 4.2. When $\sigma^{2}<4 \alpha \theta$ we have proved that the conclusion of Proposition 4.1 holds if

$$
\Delta<\min \left\{\frac{4 \theta}{4 \alpha \theta-\sigma^{2}}, \frac{2(2 \alpha \theta-\sqrt{\alpha \theta} \sigma)}{4 \alpha^{2} \theta-\alpha \sigma^{2}}\right\}=\frac{2(2 \alpha \theta-\sqrt{\alpha \theta} \sigma)}{4 \alpha^{2} \theta-\alpha \sigma^{2}}<\frac{1}{\alpha},
$$

which is a sharper result.

By means of the identity (32) we calculate $\mathbb{E}\left[X\U {n}^{2}\right]$ for the scheme MS. Its evolution when solving Eq. (1) with parameters $\alpha=0.43, \theta=0.06, \sigma=0.15$ in the interval $[0,15]$ with an equidistant partition of step size $\Delta=1 / 8$ and starting point $X\U {0}=0.9 \theta$ is shown on the left plot of Fig. 2. Additionally, on the right plot of Fig. 2, the error

$$
\varepsilon\U {M}^{2}\left(t\U {n}\right):=\left|\mathbb{E}\left[X\U {n}^{2}\right]-\mathbb{E}\left[X\left(t\U {n}\right)^{2}\right]\right|
$$

is shown in logarithmic scale. In both cases, the values on the grid points are extended to the whole interval by linear interpolation. Since the chosen parameters verify Proposition 4.1, the first two moments of MS converge to those of the CIR equation, as can be seen in the left plot of Fig. 2. The right side of this figure shows how the second moment error converges exponentially to zero.

## 9. Numerical experiments

In this section we carry out two experiments. The first one is devoted to testing the strong order of the proposed methods, whereas the second one is used to confirm the theoretical results regarding the preservation of the first two long-term moments. In addition to $H M, E(0)$, the schemes $M\U {0}, M\U {1}$ developed in Section 3, and MS proposed in Section 4, for the sake of comparison we shall use the drift-implicit method (DI) proposed by Alfonsi in [8] and the Milstein-like scheme (HH) proposed by Hefter and Herzwurm in [12].

### 9.1. Experiment 1

We solve numerically Eq. (1) for the following sets of parameters

$$
\begin{aligned}
& \alpha=0.43, \quad \theta=0.06, \quad \sigma=2 \sqrt{\alpha \theta} . \\
& \alpha=1, \quad \theta=1, \quad \sigma=\sqrt{3} . \\
& \alpha=1, \quad \theta=1, \quad \sigma=1 .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-10.jpg?height=834&width=1533&top\U left\U y=170&top\U left\U x=178)

Fig. 3. Log-log plots of the strong error (41) as a function of $\Delta \in\left\{2^{-1}, 2^{-2}, \ldots, 2^{-8}\right\}$ for methods HH, HM, E(0), DI, M 1 and MS and parameters (37) (top), and (38), (39) (bottom).

Table 1

Average slopes corresponding to the error curves shown in Fig. 3.

| Parameters | HH | HM | E $(0)$ | DI | $\mathrm{M}\U {1}$ | MS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $(37)$ | 0.479 | 0.491 | 0.823 | 0.641 | 0.672 | 0.753 |
| $(38)$ | 0.455 | 0.521 | 1.01 | 0.752 | 0.875 | 1.03 |
| $(39)$ | 0.983 | 0.575 | 1.07 | 0.962 | 1.04 | 1.09 |

and initial value $x\U {0}=\theta$. For each method, step size $\Delta \in\left\{2^{-1}, 2^{-2}, \ldots, 2^{-8}\right\}$ and set of parameters, we estimate the strong error

$$
\mathbb{E}\left|X\U {t / \Delta}-X(t)\right|
$$

at time $t=1$. The parameters (37) verify $\sigma^{2}=4 \alpha \theta$; thus, the strong solution is available in closed form, see [6]and we can use it to calculate (40). Using the same Brownian paths as for the exact solution we simulate $N=10000$ paths for the methods $\mathrm{HM}, \mathrm{E}(0), \mathrm{M}\U {0}$, MS, DI and $\mathrm{HH}$ and calculate

$$
\frac{1}{N} \sum\U {k=1}^{N}\left|X\U {t / \Delta, k}-X\U {k}(t)\right|
$$

as an approximation of (40). Parameters (38) and (39) have been chosen as in [8]. For these parameters the strong solution to (1) is not available in closed form. Therefore to calculate (41) we use an approximation of the solution: the one given by the method $\mathrm{HH}$, which has strong order $1 / 2$, with the step size $\Delta=2^{-25}$.

The results of the analysis with the three sets of parameters are shown in Fig. 3, where the log-log plots of the strong error against $\Delta$ have been plotted. To serve as a reference, dashed straight lines with slopes $\frac{1}{2}$ and 1 have been added. And for a better understanding we show in Table 1 the average slope of every method for each set of parameters. It can be seen that the DI scheme as well as our schemes $\mathrm{M}\U {1}$, MS present the lowest errors. Notice that the values for $\sigma^{2} / 4 \alpha \theta$ are $1,3 / 4$ and $1 / 4$ for (37), (38) and (39) respectively. The results show, in agreement with [6], that for increasing values of $\sigma^{2} / 4 \alpha \theta$ the experimental rate of convergence decreases. It can be seen that scheme HM (and HH except for parameters (39)) show experimental rates of strong convergence close to $1 / 2$. On the other hand, schemes $\mathrm{DI}, \mathrm{E}(0), \mathrm{M}\U {1}$ and MS present strong orders of convergence greater than $1 / 2$, and approximately equal to 1 for parameters (38) and (39).
![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-11.jpg?height=834&width=1518&top\U left\U y=173&top\U left\U x=180)

Fig. 4. Evolution of first moment (top left) and of the second moment (bottom left); evolution of the first moment error (top right) and of the second moment error (bottom right) both in logarithmic scale. All plots for parameters (42) and schemes (6), (7), (26), (36), DI and HH for solving (1).

### 9.2. Experiment 2

In this experiment we solve Eq. (1) with two new sets of parameters. In both cases we simulate $N=1.5 \times 10^{6}$ paths of each of the numerical solutions of (1) and calculate

$$
\bar{X}\U {n}:=\frac{1}{N} \sum\U {k=1}^{N} X\U {n, k} ; \quad \overline{X\U {n}^{2}}:=\frac{1}{N} \sum\U {k=1}^{N} X\U {n, k}^{2}
$$

as approximations of $\mathbb{E}\left[X\left(t\U {n}\right)\right]$ and $\mathbb{E}\left[X^{2}\left(t\U {n}\right)\right]$ respectively. From here, we calculate the errors in the first two moments of the method $M$ as

$$
\bar{\varepsilon}\U {M}\left(t\U {n}\right):=\left|\bar{X}\U {n}-\mathbb{E}\left[X\left(t\U {n}\right)\right]\right| ; \quad \overline{\varepsilon\U {M}^{2}}\left(t\U {n}\right):=\left|\overline{X\U {n}^{2}}-\mathbb{E}\left[X\left(t\U {n}\right)^{2}\right]\right| .
$$

We choose the first set of parameters, initial value and step size as

$$
\alpha=0.43, \quad \theta=0.06, \quad \sigma=0.15, \quad x\U {0}=0.054, \quad \Delta=\frac{1}{8},
$$

where $\alpha, \theta$ and $\sigma$ are the maximum likelihood estimation parameters obtained in [19] and the starting point $x\U {0}$ is chosen to be lesser than the long-term mean $\theta$. With the methods HM, E(0) M $\mathrm{M}\U {0}$, MS, DI and HH we solve (1). The values of $\bar{X}\U {n}$ and $\overline{X^{2}}{ }\U {n}$, extended by interpolation, together with the exact values of $\mathbb{E}[X(t)]$ and $\mathbb{E}\left[X^{2}(t)\right]$ are represented on the left side of Fig. 4. The corresponding errors $\bar{\varepsilon}\U {M}(t) \overline{\varepsilon\U {M}^{2}}(t)$, in logarithmic scale, are shown in the right pictures of Fig. 4.

We choose the second set of parameters, initial value and step size to be

$$
\alpha=3, \quad \theta=1, \quad \sigma=1, \quad X\U {0}=1.1, \quad \Delta=\frac{1}{4}
$$

in this case, the parameters are significantly larger than in the first set and with initial point greater than the long-term mean. With the methods (6), (7), $\mathrm{M}\U {2}$, MS, DI and HH we solve (1). The graphical representation of the sample moments and the corresponding errors are shown in Fig. 5. Notice that the two sample moments of $\mathrm{E}(0)$ do not appear in the corresponding graphs, as they are outside the plot range.

For both (42) and (43), one can observe that only the modified Euler and our proposed $M\U {0} M\U {2}$ and MS methods revert to the long-term mean, in accordance with the theoretical results of Section 3. Furthermore, these three meanreverting schemes present similar errors. In addition, it can be seen that $E(0)$ overestimates the long-term mean, as we claimed in (10). On the other hand, the only scheme whose second moment converges to that of the CIR process is our proposed scheme MS. Notice also that for both experiments the sufficient condition of Remark 4.2 holds, concluding Sample Mean
![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-12.jpg?height=776&width=742&top\U left\U y=209&top\U left\U x=190)

![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-12.jpg?height=406&width=735&top\U left\U y=200&top\U left\U x=960)

Weak Quadratic Error

![](https://cdn.mathpix.com/cropped/2023\U 09\U 28\U e7fdb60d06f1ce22d705g-12.jpg?height=330&width=705&top\U left\U y=664&top\U left\U x=985)

Fig. 5. Evolution of first moment (top left) and of the second moment (bottom left); evolution of the first moment error (top right) and of the second moment error (bottom right) both in logarithmic scale. All plots for parameters (42) and schemes (6), (7), (29), (36), DI and HH for solving (1).

that MS preserves the first and second-moment limits. Whereas the parameters (42) fulfill the condition $\Delta \leq 1 /(2 \alpha)$ of Proposition 4.1, the parameters (43) do not. This illustrates the advantage of using a sharper bound when working with sufficient conditions.

## 10. Conclusions

Mean-reversion is one of the most characteristic properties of the CIR model. We design a family of schemes tailored to conserve this property. Furthermore, we develop a scheme with the same long-term mean and variance as the CIR process. We prove that our schemes converge in the strong sense with a logarithmic rate and in the weak sense with order 1 . However, numerical experiments suggest that the proposed numerical methods have a strong order greater than $1 / 2$ and in some cases close to 1 , similar to the performance of the best methods used in the comparison. Each of the methods we develop requires a different condition on the step size in order to have the mean reversion property. Several of these methods have simple forms, notably

$$
X\U {n+1}=\left(\sqrt{1-\alpha \Delta} \sqrt{X\U {n}}+\frac{\sigma}{2} \Delta W\U {n}\right)^{2}+\left(\alpha \theta-\frac{\sigma^{2}}{4}\right) \Delta
$$

which is the choice we recommend when, the long-term variance is not of importance and $\Delta<1 / \alpha$ due to its simpler expression. If the second moment is relevant, we recommend using the scheme MS. And finally, we recommend the scheme $\mathrm{M}\U {2}$ if the previous schemes cannot be applied because of step size requirements, as this scheme is less restrictive on the step size condition.

## 11. Data availability

No data was used for the research described in the article.

## 12. Acknowledgments

We are very grateful to the anonymous referees for their detailed revision. Their comments and suggestions have helped us to improve the manuscript.

## 13. References

[1] M. Choudhry, M. Lizzio, Advanced Fixed Income Analysis, second ed., Elsevier, 2015.

[2] S.E. Shreve, Stochastic Calculus for Finance II: Continuous-Time Models, Springer, 2004.

[3] J. Cox, J. Ingersoll, S. Ross, A Theory of the Term Structure of Interest Rates, World Scientific, 2005, pp. 129-164.

[4] B. Øksendal, Stochastic Differential Equations, Springer, 2003.

[5] N. Ikeda, S. Watanabe, Stochastic Differential Equations and Diffusion Processes, Elsevier, 2014.

[6] M. Hefter, A. Herzwurm, Optimal strong approximation of the one-dimensional squared Bessel process, Commun. Math. Sci. 15 (8) (2017) 2121-2141.

[7] P. Glasserman, Monte Carlo Methods in Financial Engineering, Springer, 2004

[8] A. Alfonsi, On the discretization schemes for the CIR (and Bessel squared) processes, Monte Carlo Methods Appl. 11 (2005) 355-384.

[9] P. Kloeden, E. Platen, Stochastic Differential Equations, Springer, Heidelberg, 1992.

[10] G. Deelstra, F. Delbaen, Convergence of discretized stochastic (interest rate) processes with stochastic drift term, Appl. Stoch. Models Data Anal. 14 (1998) 77-84.

[11] S. Dereich, A. Neuenkirch, L. Szpruch, An Euler-type method for the strong approximation of the Cox-Ingersoll-Ross process, R. Soc. 468 (2012) 1105-1115.

[12] M. Hefter, A. Herzwurm, Strong convergence rates for Cox-Ingersoll-Ross processes-full parameter range, J. Math. Anal. Appl. 459 (2) (2018) 1079-1101.

[13] C. Kahl, P. Jäckel, Fast strong approximation Monte Carlo schemes for stochastic volatility models, Quant. Finance 6 (6) (2006) 513-536.

[14] H. Schurz, Numerical regularization for SDE's: construction of nonnegative solutions, Dyn. Syst. Appl. 5 (1996) $323-352$.

[15] Y. Yuan, Non-negativity preserving numerical algorithms for problems in mathematical finance, Appl. Math. 9 (2018) 313-335.

[16] O. Okhrin, G.M. Rockinger, M. Schmid, Simulating the Cox-Ingersoll-Ross and Heston processes: matching the first four moments, J. Comput. Finance 26 (2) (2022).

[17] D. Higham, X. Mao, Convergence of Monte Carlo simulations involving the mean-reverting square root process, J. Comput. Finance 8 (3) (2005) 35-61.

[18] A. Alfonsi, Strong order one convergence of a drift implicit Euler scheme: Application to the CIR process, Statist. Probab. Lett. 83 (2) (2013) 602-607.

[19] K. Kladívko, Maximum likelihood estimation of the Cox-Ingersoll-Ross process: the matlab implementation, Tech. Comput. Prague 7 (8) (2007) $1-8$.


[^0]:    * Corresponding author.

    E-mail addresses: samirllamazares@usal.es (S. Llamazares-Elias), bacon@usal.es (A. Tocino).

