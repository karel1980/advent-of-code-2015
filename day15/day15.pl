/*use_module(library(clpfd)).*/

day15(MaxScore) :- 
	fd_domain(IF,0,100),
	fd_domain(IB,0,100),
	fd_domain(IC,0,100),
	fd_domain(IS,0,100),
   	IF+IC+IB+IS #= 100,
	Cap #= IF*4-IB,
	Dur #= IF*(-2)+IC*5,
	Fla #= IC*(-1)+IB*5+IS*(-2),
	Tex #= IB*5+IS*2,
	Cap #> 0,
	Dur #> 0,
	Fla #> 0,
	Tex #> 0,
	Score #= Cap*Dur*Fla*Tex.
	fd_max(Score, MaxScore),
	labeling([MaxScore],[MaxScore]).
	
