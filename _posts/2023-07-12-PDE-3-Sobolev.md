EXERCISES WITH HINTS

(*Generate HTML with exercise container structure*)

exerciseHTML = 
  StringTemplate[
   "<div class=\"exercise-container\">\n<button class=\"exercise-button\" \
onclick=\"toggleExercise(this)\">Exercise</button>\n<div \
class=\"exercise-text\">\n{{{content}}}\n</div>\n</div>"];

finalHTML = 
  exerciseHTML[<|"content" -> exerciseContent <> "\n\n" <> hintContent|>];

(*Output the final HTML*)
finalHTML
