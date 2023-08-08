# [Gold V] 색종이와 공예 - 26598 

[문제 링크](https://www.acmicpc.net/problem/26598) 

### 성능 요약

메모리: 70580 KB, 시간: 1776 ms

### 분류

애드 혹, 너비 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p style="user-select: auto;">준성이는 색종이를 가위로 자르고 남은 색종이 조각들로 뭘 할지 생각해 보았다.</p>

<p style="user-select: auto;">군 생활 동안 열심히 고민해 본 결과, 색종이를 다시 이어붙여 <strong style="user-select: auto;">색종이 공예품</strong>을 만들기로 했다!</p>

<p style="user-select: auto;">준성이가 색종이를 이어 붙일 때는 다음과 같은 규칙을 따른다.</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">각 색종이 조각들은 변과 변을 맞대고 있으며, 일부 또는 전체가 겹치지 않는다.</li>
	<li style="user-select: auto;">이어 붙어진 색종이 조각들은 2차원 상에서 세로 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, 가로 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>인 빈틈없는 직사각형 모양이다.</li>
	<li style="user-select: auto;">이때, 각 색종이 조각들이 모두 가로 길이와 세로 길이가 정수인 빈틈없는 직사각형 모양이라면 예쁜<strong style="user-select: auto;"> 색종이 공예품</strong>이라고 한다.  </li>
</ol>

<p style="user-select: auto;">준성이는 열심히 만든 <strong style="user-select: auto;">색종이 공예품</strong>을 당신에게 자랑하기 위해 보여줬다.</p>

<blockquote style="user-select: auto;">
<p style="user-select: auto;"><em style="user-select: auto;">"ㅎㅎ 예쁘지?"</em></p>
</blockquote>

<p style="user-select: auto;">왠지 준성이가 기분이 좋아 보이는 것이 맘에 안 든다... 준성이가 만든 <strong style="user-select: auto;">색종이 공예품</strong>을 보고 예쁘지 않다면 놀려주도록 하자!</p>

### 입력 

 <p style="user-select: auto;">첫째 줄에 <strong style="user-select: auto;">색종이 공예품</strong>의 세로 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, 가로 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백을 두고 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N,M \leq 1\,000)$</span> </mjx-container></p>

<p style="user-select: auto;">다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 알파벳 대문자로 이루어진 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>인 문자열이 주어진다.</p>

<p style="user-select: auto;">상하좌우로 인접한 두 알파벳이 같다면 서로 같은 색종이 조각이고, 그렇지 않다면 서로 다른 색종이 조각이다.</p>

<p style="user-select: auto;">알파벳 하나의 세로 길이와 가로 길이는 모두 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>이며, 주어지는 숫자는 모두 정수다.</p>

### 출력 

 <p style="user-select: auto;">입력으로 주어진 <strong style="user-select: auto;">색종이 공예품</strong>이 예쁘다면 <code style="user-select: auto;">dd</code>를 입력하고, 그렇지 않다면 <code style="user-select: auto;">BaboBabo</code>를 출력한다.</p>

